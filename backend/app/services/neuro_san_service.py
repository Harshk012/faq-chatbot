import os
import warnings
from typing import Optional, List
from app.models.chat import ChatMessage
from app.services.faq_data import FAQ_DATA

warnings.filterwarnings("ignore", category=RuntimeWarning)

# Set the manifest location
REGISTRIES_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "registries")
MANIFEST_PATH = os.path.join(REGISTRIES_PATH, "manifest.hocon")
os.environ["AGENT_MANIFEST_FILE"] = MANIFEST_PATH


def _build_conversation_context(history: List[ChatMessage]) -> str:
    """Build a context string from conversation history for multi-turn support."""
    if not history:
        return ""
    context_lines = ["\n\nConversation so far:"]
    for msg in history[-6:]:  # Last 6 messages for context window efficiency
        role_label = "User" if msg.role == "user" else "Assistant"
        context_lines.append(f"{role_label}: {msg.content}")
    return "\n".join(context_lines)


async def invoke_faq_agent(
    user_message: str,
    conversation_history: Optional[List[ChatMessage]] = None,
) -> str:
    """
    Invoke the Neuro-SAN FAQ agent and return its response.
    Supports multi-turn conversation via injected history context.
    """
    try:
        from neuro_san.client.agent_session_factory import DirectAgentSessionFactory

        # Build the enriched prompt with FAQ data and conversation context
        context = _build_conversation_context(conversation_history or [])
        
        # The HOCON instructions use {faq_content} placeholder — we pass it via sly_data
        # and also embed it in the message for agents that don't support sly_data templating
        enriched_message = (
            f"FAQ Knowledge Base:\n{FAQ_DATA}\n"
            f"{context}\n\n"
            f"Current user question: {user_message}"
        )

        factory = DirectAgentSessionFactory()
        session = factory.create_session(
            agent_name="faq_chatbot",
            use_direct=True,
            metadata={},
        )

        request_payload = {
            "user_message": {"text": enriched_message},
            "sly_data": {"faq_content": FAQ_DATA},
        }

        stream = session.streaming_chat(request_payload)
        messages = []
        for chat_msg in stream:
            messages.append(chat_msg)
            if chat_msg.get("done") is True:
                break

        if messages and messages[-1].get("response"):
            return messages[-1]["response"]["text"]
        return "I'm sorry, I couldn't process your request. Please try again."

    except ImportError:
        # Fallback: If neuro-san is not installed, use a simple keyword-based FAQ lookup
        return _fallback_faq_lookup(user_message, conversation_history)
    except Exception as e:
        print(f"[Neuro-SAN Error] {e}")
        return _fallback_faq_lookup(user_message, conversation_history)


def _fallback_faq_lookup(
    user_message: str,
    conversation_history: Optional[List[ChatMessage]] = None,
) -> str:
    """
    Fallback FAQ lookup when Neuro-SAN / LLM is unavailable.
    Uses simple keyword matching against the FAQ dataset.
    """
    msg_lower = user_message.lower()
    faq_lines = FAQ_DATA.split("\n")

    # Find relevant Q&A pairs
    relevant_answers = []
    i = 0
    while i < len(faq_lines):
        line = faq_lines[i].strip()
        if line.startswith("Q:"):
            question = line[2:].strip().lower()
            # Check if user message keywords match the question
            question_words = set(question.split())
            user_words = set(msg_lower.split())
            overlap = question_words & user_words
            # Filter out common stop words
            stop_words = {"how", "can", "i", "the", "a", "is", "my", "do", "what", "are", "to", "in", "of", "for"}
            meaningful_overlap = overlap - stop_words
            if len(meaningful_overlap) >= 2 or any(kw in msg_lower for kw in ["premium", "claim", "fund", "switch", "withdraw", "loan", "surrender", "bank", "account", "maturity", "contact"]):
                # Collect the answer
                answer_lines = []
                j = i + 1
                while j < len(faq_lines) and not faq_lines[j].strip().startswith("Q:") and not faq_lines[j].strip().startswith("==="):
                    if faq_lines[j].strip().startswith("A:"):
                        answer_lines.append(faq_lines[j].strip()[2:].strip())
                    elif answer_lines:
                        answer_lines.append(faq_lines[j].strip())
                    j += 1
                if answer_lines and len(meaningful_overlap) >= 1:
                    relevant_answers.append((len(meaningful_overlap), "\n".join(a for a in answer_lines if a)))
        i += 1

    if relevant_answers:
        relevant_answers.sort(key=lambda x: x[0], reverse=True)
        return relevant_answers[0][1]

    return (
        "I don't have specific information on that query. "
        "Please contact ICICI Prudential customer care at **1860-266-7766** "
        "(Monday–Saturday, 9 AM–7 PM) or email **lifeline@iciciprulife.com** for assistance."
    )