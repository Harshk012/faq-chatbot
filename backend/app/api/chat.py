from fastapi import APIRouter, HTTPException
from datetime import datetime
from app.models.chat import ChatRequest, ChatResponse, ChatMessage, MessageRole
from app.services.neuro_san_service import invoke_faq_agent
from app.db.mongo import get_db

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Main chat endpoint. Accepts a user message + session_id,
    invokes the Neuro-SAN FAQ agent, persists the conversation to MongoDB,
    and returns the bot's reply.
    """
    if not request.message or not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty.")

    db = get_db()

    # Fetch existing conversation from DB for multi-turn context
    existing_session = None
    history = []
    if db is not None:
        existing_session = await db.conversations.find_one({"session_id": request.session_id})
        if existing_session:
            history = [ChatMessage(**m) for m in existing_session.get("messages", [])]

    # Merge client-sent history with DB history (prefer DB as source of truth)
    if not history and request.conversation_history:
        history = request.conversation_history

    # Invoke Neuro-SAN agent
    try:
        bot_reply = await invoke_faq_agent(
            user_message=request.message.strip(),
            conversation_history=history,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Agent error: {str(e)}")

    now = datetime.utcnow()

    user_msg = ChatMessage(role=MessageRole.USER, content=request.message.strip(), timestamp=now)
    bot_msg = ChatMessage(role=MessageRole.BOT, content=bot_reply, timestamp=now)

    # Persist to MongoDB
    if db is not None:
        if existing_session:
            await db.conversations.update_one(
                {"session_id": request.session_id},
                {
                    "$push": {"messages": {"$each": [user_msg.dict(), bot_msg.dict()]}},
                    "$set": {"updated_at": now},
                },
            )
        else:
            await db.conversations.insert_one(
                {
                    "session_id": request.session_id,
                    "messages": [user_msg.dict(), bot_msg.dict()],
                    "created_at": now,
                    "updated_at": now,
                }
            )

    return ChatResponse(
        session_id=request.session_id,
        reply=bot_reply,
        timestamp=now,
    )