import { Link } from 'react-router-dom';

export default function Nav() {
  return (
    <div className="sidebar">
      <h2>🔧 BLACKBOX AI</h2>
      
      {/* Navigation Links */}
      <nav className="nav-links">
        <Link to="/chat" className="nav-btn active">
          💬 Chat
        </Link>
        <Link to="/blackbox" className="nav-btn">
          🖥️ Terminal
        </Link>
      </nav>

      {/* Actions */}
      <div className="nav-actions">
<button className="new-chat-btn" onClick={() => window.clearChat ? window.clearChat() : alert('New chat cleared!')}>+ New Chat</button>
        <button className="pdf-btn">📄 Export</button>
      </div>
    </div>
  );
}

