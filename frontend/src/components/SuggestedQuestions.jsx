import React from "react";
import { Button } from "primereact/button";

const SUGGESTIONS = [
  "How do I pay my premium online?",
  "How do I change my bank account?",
  "How do I file a death claim?",
  "Can I make a partial withdrawal?",
  "What is the free look period?",
  "How can I switch funds in my ULIP?",
];

const SuggestedQuestions = ({ onSelect, visible }) => {
  if (!visible) return null;

  return (
    <div className="suggestions-container">
      <p className="suggestions-label">
        <i className="pi pi-bolt" style={{ marginRight: "6px" }} />
        Quick questions
      </p>
      <div className="suggestions-grid">
        {SUGGESTIONS.map((q) => (
          <Button
            key={q}
            label={q}
            className="p-button-outlined p-button-sm suggestion-chip"
            onClick={() => onSelect(q)}
            icon="pi pi-arrow-right"
            iconPos="right"
          />
        ))}
      </div>
    </div>
  );
};

export default SuggestedQuestions;