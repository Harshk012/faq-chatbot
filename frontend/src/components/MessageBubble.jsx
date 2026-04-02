import React from "react";
import { Avatar } from "primereact/avatar";
import ReactMarkdown from "react-markdown";

const formatTime = (timestamp) => {
  try {
    return new Date(timestamp).toLocaleTimeString([], {
      hour: "2-digit",
      minute: "2-digit",
    });
  } catch {
    return "";
  }
};

const MessageBubble = ({ message }) => {
  const isUser = message.role === "user";
  const isError = message.isError;

  return (
    <div className={`message-row ${isUser ? "message-row--user" : "message-row--bot"}`}>
      {!isUser && (
        <Avatar
          image="/logo-icon.png"
          icon={!"/logo-icon.png" ? "pi pi-shield" : undefined}
          className="message-avatar message-avatar--bot"
          shape="circle"
          size="normal"
        />
      )}

      <div className={`message-bubble ${isUser ? "message-bubble--user" : "message-bubble--bot"} ${isError ? "message-bubble--error" : ""}`}>
        <div className="message-content">
          {isUser ? (
            <p className="message-text">{message.content}</p>
          ) : (
            <div className="message-markdown">
              <ReactMarkdown>{message.content}</ReactMarkdown>
            </div>
          )}
        </div>
        <span className="message-time">{formatTime(message.timestamp)}</span>
      </div>

      {isUser && (
        <Avatar
          icon="pi pi-user"
          className="message-avatar message-avatar--user"
          shape="circle"
          size="normal"
        />
      )}
    </div>
  );
};

export default MessageBubble;