const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');
const messagesArea = document.getElementById('messages-area');

let sessionId = null;

function addMessage(text, role, meta = null) {
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('message');
    msgDiv.classList.add(role === 'user' ? 'user-message' : 'bot-message');

    let content = text;
    if (meta && role === 'bot') {
        content += `<div class="meta-info">Intent: ${meta.intent} (${(meta.confidence * 100).toFixed(1)}%)</div>`;
        if (meta.entities.length > 0) {
            const ents = meta.entities.map(e => `${e.entity}: ${e.word}`).join(', ');
            content += `<div class="meta-info">Entities: ${ents}</div>`;
        }
    }

    msgDiv.innerHTML = content;
    messagesArea.appendChild(msgDiv);
    messagesArea.scrollTop = messagesArea.scrollHeight;
}

chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const message = userInput.value.trim();
    if (!message) return;

    // Clear input
    userInput.value = '';

    // Add user message to UI
    addMessage(message, 'user');

    try {
        const response = await fetch('http://localhost:8000/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                message: message,
                session_id: sessionId
            })
        });

        const data = await response.json();
        sessionId = data.session_id;

        // Add bot response to UI
        addMessage(data.response, 'bot', {
            intent: data.intent,
            confidence: data.confidence,
            entities: data.entities
        });
    } catch (error) {
        console.error('Error:', error);
        addMessage('Sorry, I am having trouble connecting to the server.', 'bot');
    }
});
