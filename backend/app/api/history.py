from fastapi import APIRouter, HTTPException
from app.db.mongo import get_db
from app.models.chat import ConversationSession, ChatMessage

router = APIRouter()


@router.get("/history/{session_id}")
async def get_history(session_id: str):
    """Retrieve conversation history for a session."""
    db = get_db()
    if db is None:
        raise HTTPException(status_code=503, detail="Database unavailable")

    session = await db.conversations.find_one(
        {"session_id": session_id}, {"_id": 0}
    )
    if not session:
        return {"session_id": session_id, "messages": []}

    return session


@router.delete("/history/{session_id}")
async def clear_history(session_id: str):
    """Clear conversation history for a session."""
    db = get_db()
    if db is None:
        raise HTTPException(status_code=503, detail="Database unavailable")

    result = await db.conversations.delete_one({"session_id": session_id})
    return {
        "session_id": session_id,
        "deleted": result.deleted_count > 0,
        "message": "Conversation cleared successfully." if result.deleted_count > 0 else "Session not found.",
    }