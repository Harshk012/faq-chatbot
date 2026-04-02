import { useState, useCallback, useRef } from "react";
import { v4 as uuidv4 } from "uuid";
import { sendChatMessage, clearHistory } from "../services/api";

const SESSION_KEY = "faq_chatbot_session_id";

const getOrCreateSessionId = () => {
  let id = sessionStorage.getItem(SESSION_KEY);
  if (!id) {
    id = uuidv4();
    sessionStorage.setItem(SESSION_KEY, id);
  }
  return id;
};

export const useChat = () => {
  const [messages, setMessages] = useState([
    {
      id: "welcome",
      role: "bot",
      content:
        "Hello! I'm your ICICI Prudential Life Insurance assistant. I can help you with questions about premium payments, claims, fund switching, policy loans, and more. How can I assist you today?",
      timestamp: new Date().toISOString(),
    },
  ]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const sessionId = useRef(getOrCreateSessionId());

  const getHistory = useCallback(() => {
    return messages
      .filter((m) => m.id !== "welcome")
      .map((m) => ({ role: m.role, content: m.content, timestamp: m.timestamp }));
  }, [messages]);

  const sendMessage = useCallback(
    async (text) => {
      if (!text.trim() || isLoading) return;

      const userMsg = {
        id: uuidv4(),
        role: "user",
        content: text.trim(),
        timestamp: new Date().toISOString(),
      };

      setMessages((prev) => [...prev, userMsg]);
      setIsLoading(true);
      setError(null);

      try {
        const data = await sendChatMessage(sessionId.current, text.trim(), getHistory());
        const botMsg = {
          id: uuidv4(),
          role: "bot",
          content: data.reply,
          timestamp: data.timestamp || new Date().toISOString(),
        };
        setMessages((prev) => [...prev, botMsg]);
      } catch (err) {
        const errMsg =
          err?.response?.data?.detail || "Something went wrong. Please try again.";
        setError(errMsg);
        setMessages((prev) => [
          ...prev,
          {
            id: uuidv4(),
            role: "bot",
            content: `⚠️ Error: ${errMsg}`,
            timestamp: new Date().toISOString(),
            isError: true,
          },
        ]);
      } finally {
        setIsLoading(false);
      }
    },
    [isLoading, getHistory]
  );

  const clearChat = useCallback(async () => {
    try {
      await clearHistory(sessionId.current);
    } catch (_) {
      // Ignore clear errors
    }
    // Reset session
    const newId = uuidv4();
    sessionStorage.setItem(SESSION_KEY, newId);
    sessionId.current = newId;
    setMessages([
      {
        id: "welcome",
        role: "bot",
        content:
          "Conversation cleared! How can I help you today?",
        timestamp: new Date().toISOString(),
      },
    ]);
    setError(null);
  }, []);

  return { messages, isLoading, error, sendMessage, clearChat, sessionId: sessionId.current };
};