import React from "react";
import { Button } from "primereact/button";
import { Tag } from "primereact/tag";

const ChatHeader = ({ onClear, sessionId }) => {
  return (
    <div className="chat-header">
      <div className="chat-header__brand">
        <div className="chat-header__logo">
          <i className="pi pi-shield" />
        </div>
        <div className="chat-header__info">
          <h1 className="chat-header__title">ICICI Prudential</h1>
          <div className="chat-header__subtitle">
            <Tag
              value="Online"
              severity="success"
              rounded
              className="status-tag"
            />
            <span className="chat-header__agent-name">AI Assistant · Powered by Neuro-SAN</span>
          </div>
        </div>
      </div>

      <div className="chat-header__actions">
        <Button
          icon="pi pi-refresh"
          className="p-button-text p-button-rounded p-button-plain header-action-btn"
          tooltip="New conversation"
          tooltipOptions={{ position: "bottom" }}
          onClick={onClear}
          aria-label="Clear conversation"
        />
      </div>
    </div>
  );
};

export default ChatHeader;