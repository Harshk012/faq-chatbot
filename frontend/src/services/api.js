import axios from "axios";

const API_BASE = process.env.REACT_APP_API_URL || "http://localhost:8000/api";

const api = axios.create({
  baseURL: API_BASE,
  timeout: 60000,
  headers: { "Content-Type": "application/json" },
});

/**
 * Send a chat message to the backend (Neuro-SAN agent).
 * @param {string} sessionId - Unique session identifier
 * @param {string} message - User's message
 * @param {Array} conversationHistory - Prior messages for context
 * @returns {Promise<{reply: string, session_id: string, timestamp: string}>}
 */
export const sendChatMessage = async (sessionId, message, conversationHistory = []) => {
  const response = await api.post("/chat", {
    session_id: sessionId,
    message,
    conversation_history: conversationHistory,
  });
  return response.data;
};

/**
 * Fetch conversation history for a session.
 * @param {string} sessionId
 */
export const fetchHistory = async (sessionId) => {
  const response = await api.get(`/history/${sessionId}`);
  return response.data;
};

/**
 * Clear conversation history for a session.
 * @param {string} sessionId
 */
export const clearHistory = async (sessionId) => {
  const response = await api.delete(`/history/${sessionId}`);
  return response.data;
};

export default api;