import React, { useState, useRef } from "react";
import { InputTextarea } from "primereact/inputtextarea";
import { Button } from "primereact/button";

const ChatInput = ({ onSend, isLoading }) => {
  const [value, setValue] = useState("");
  const textareaRef = useRef(null);

  const handleSend = () => {
    const trimmed = value.trim();
    if (!trimmed || isLoading) return;
    onSend(trimmed);
    setValue("");
    setTimeout(() => textareaRef.current?.focus(), 50);
  };

  const handleKeyDown = (e) => {
    // Send on Enter (without Shift)
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="chat-input-bar">
      <div className="chat-input-wrapper">
        <InputTextarea
          ref={textareaRef}
          value={value}
          onChange={(e) => setValue(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Ask about premiums, claims, fund switching…"
          autoResize
          rows={1}
          className="chat-input-textarea"
          disabled={isLoading}
          maxLength={1000}
        />
        <Button
          icon={isLoading ? "pi pi-spin pi-spinner" : "pi pi-send"}
          className="p-button-rounded send-button"
          onClick={handleSend}
          disabled={!value.trim() || isLoading}
          aria-label="Send message"
          tooltip={isLoading ? "Thinking…" : "Send (Enter)"}
          tooltipOptions={{ position: "top" }}
        />
      </div>
      <p className="chat-input-hint">
        Press <kbd>Enter</kbd> to send · <kbd>Shift+Enter</kbd> for new line
      </p>
    </div>
  );
};

export default ChatInput;