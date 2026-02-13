import { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import { Send, Bot, User, Cpu, Hash } from 'lucide-react';
import './App.css';

const API_BASE = 'http://localhost:8001';

function App() {
  const [messages, setMessages] = useState([
    { role: 'bot', text: 'Hello! I am Aura, your context-aware React assistant. How can I help you today?' }
  ]);
  const [input, setInput] = useState('');
  const [sessionId, setSessionId] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSend = async (e) => {
    e.preventDefault();
    if (!input.trim() || isLoading) return;

    const userMsg = input.trim();
    setInput('');
    setMessages(prev => [...prev, { role: 'user', text: userMsg }]);
    setIsLoading(true);

    try {
      const response = await axios.post(`${API_BASE}/chat`, {
        message: userMsg,
        session_id: sessionId
      });

      const data = response.data;
      setSessionId(data.session_id);
      setMessages(prev => [...prev, {
        role: 'bot',
        text: data.response,
        meta: {
          intent: data.intent,
          confidence: data.confidence,
          entities: data.entities
        }
      }]);
    } catch (error) {
      console.error('Error:', error);
      setMessages(prev => [...prev, { role: 'bot', text: 'I am sorry, I am having trouble connecting to my brain right now.' }]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-header">
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <Bot size={28} color="#818cf8" />
          <h1>Aura AI v2.0</h1>
        </div>
        <div className="status-indicator">
          <div className="status-dot"></div>
          <span>Systems Online</span>
        </div>
      </div>

      <div className="messages-area">
        {messages.map((msg, idx) => (
          <div key={idx} className={`message-wrapper ${msg.role}`}>
            <div className="message">
              {msg.text}
            </div>
            {msg.meta && (
              <div className="meta-info">
                <span title="Intent Detected" style={{ marginRight: '8px', display: 'inline-flex', alignItems: 'center', gap: '2px' }}>
                  <Cpu size={10} /> {msg.meta.intent} ({(msg.meta.confidence * 100).toFixed(0)}%)
                </span>
                {msg.meta.entities.length > 0 && (
                  <span title="Entities Extracted" style={{ display: 'inline-flex', alignItems: 'center', gap: '2px' }}>
                    <Hash size={10} /> {msg.meta.entities.map(e => e.word).join(', ')}
                  </span>
                )}
              </div>
            )}
          </div>
        ))}
        {isLoading && <div className="typing">Aura is thinking...</div>}
        <div ref={messagesEndRef} />
      </div>

      <form className="input-area" onSubmit={handleSend}>
        <div className="input-wrapper">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask me anything..."
            disabled={isLoading}
            autoFocus
          />
        </div>
        <button type="submit" className="send-btn" disabled={!input.trim() || isLoading}>
          <Send size={20} />
        </button>
      </form>
    </div>
  );
}

export default App;
