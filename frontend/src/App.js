import React from "react";
import { PrimeReactProvider } from "primereact/api";

// PrimeReact theme + icons + flex
import "primereact/resources/themes/lara-light-blue/theme.css";
import "primereact/resources/primereact.min.css";
import "primeicons/primeicons.css";
import "primeflex/primeflex.css";

import "./styles/global.css";
import ChatWindow from "./components/ChatWindow";

function App() {
  return (
    <PrimeReactProvider>
      <div className="app-root">
        {/* Decorative background blobs */}
        <div className="bg-blob bg-blob--1" aria-hidden="true" />
        <div className="bg-blob bg-blob--2" aria-hidden="true" />

        <main className="app-main">
          {/* Side panel - branding */}
          <aside className="app-sidebar">
            <div className="sidebar-brand">
              <div className="sidebar-logo">
                <i className="pi pi-shield" />
              </div>
              <h2 className="sidebar-title">ICICI Prudential</h2>
              <p className="sidebar-subtitle">Life Insurance</p>
            </div>

            <div className="sidebar-features">
              <div className="sidebar-feature">
                <i className="pi pi-bolt feature-icon" />
                <div>
                  <p className="feature-title">Instant Answers</p>
                  <p className="feature-desc">Powered by Neuro-SAN agentic AI</p>
                </div>
              </div>
              <div className="sidebar-feature">
                <i className="pi pi-comments feature-icon" />
                <div>
                  <p className="feature-title">Multi-turn Conversations</p>
                  <p className="feature-desc">Contextual memory across your session</p>
                </div>
              </div>
              <div className="sidebar-feature">
                <i className="pi pi-lock feature-icon" />
                <div>
                  <p className="feature-title">Secure & Private</p>
                  <p className="feature-desc">Your data stays in your session</p>
                </div>
              </div>
            </div>

            <div className="sidebar-topics">
              <p className="sidebar-topics-label">I can help with</p>
              {[
                "Premium payments",
                "Claims & settlement",
                "Fund switching",
                "Policy loans",
                "Bank account updates",
                "Policy maturity",
              ].map((topic) => (
                <span key={topic} className="sidebar-topic-chip">
                  {topic}
                </span>
              ))}
            </div>

            <div className="sidebar-footer">
              <p>© 2024 ICICI Prudential Life Insurance</p>
              <p>1860-266-7766 · lifeline@iciciprulife.com</p>
            </div>
          </aside>

          {/* Main chat interface */}
          <section className="app-chat">
            <ChatWindow />
          </section>
        </main>
      </div>
    </PrimeReactProvider>
  );
}

export default App;