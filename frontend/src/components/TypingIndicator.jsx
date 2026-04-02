import React from "react";
import { Avatar } from "primereact/avatar";

const TypingIndicator = () => (
  <div className="message-row message-row--bot">
    <Avatar
      icon="pi pi-shield"
      className="message-avatar message-avatar--bot"
      shape="circle"
      size="normal"
    />
    <div className="message-bubble message-bubble--bot typing-bubble">
      <span className="typing-dot" />
      <span className="typing-dot" />
      <span className="typing-dot" />
    </div>
  </div>
);

export default TypingIndicator;