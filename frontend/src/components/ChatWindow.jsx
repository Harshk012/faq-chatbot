import React, { useRef, useEffect } from "react";
import { Toast } from "primereact/toast";
import { ScrollPanel } from "primereact/scrollpanel";
import ChatHeader from "./ChatHeader";
import MessageBubble from "./MessageBubble";
import TypingIndicator from "./TypingIndicator";
import ChatInput from "./ChatInput";
import SuggestedQuestions from "./SuggestedQuestions";
import { useChat } from "../hooks/useChat";

const ChatWindow = () => {
  const { messages, isLoading, error, sendMessage, clearChat } = useChat();
  const scrollRef = useRef(null);
  const toast = useRef(null);
  const messagesEndRef = useRef(null);

  // Show only welcome message means new session — show suggestions
  const showSuggestions = messages.length === 1 && messages[0].id === "welcome";

  // Auto-scroll to bottom on new messages
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, isLoading]);

  // Show error toast
  useEffect(() => {
    if (error) {
      toast.current?.show({
        severity: "error",
        summary: "Connection Error",
        detail: error,
        life: 5000,
      });
    }
  }, [error]);

  const handleClear = async () => {
    await clearChat();
    toast.current?.show({
      severity: "info",
      summary: "Conversation Cleared",
      detail: "Starting a new session.",
      life: 3000,
    });
  };

  return (
    <div className="chat-window">
      <Toast ref={toast} position="top-right" />

      <ChatHeader onClear={handleClear} />

      <div className="chat-messages-area">
        <ScrollPanel ref={scrollRef} className="chat-scroll-panel">
          <div className="chat-messages-list">
            {messages.map((msg) => (
              <MessageBubble key={msg.id} message={msg} />
            ))}

            {isLoading && <TypingIndicator />}

            <div ref={messagesEndRef} />
          </div>
        </ScrollPanel>

        <SuggestedQuestions
          visible={showSuggestions && !isLoading}
          onSelect={sendMessage}
        />
      </div>

      <ChatInput onSend={sendMessage} isLoading={isLoading} />
    </div>
  );
};

export default ChatWindow;