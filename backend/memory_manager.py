from collections import deque

class MemoryManager:
    def __init__(self, max_history=5):
        self.sessions = {}
        self.max_history = max_history

    def get_session(self, session_id):
        if session_id not in self.sessions:
            self.sessions[session_id] = {
                "history": deque(maxlen=self.max_history),
                "context": {}
            }
        return self.sessions[session_id]

    def add_message(self, session_id, role, text):
        session = self.get_session(session_id)
        session["history"].append({"role": role, "text": text})

    def update_context(self, session_id, key, value):
        session = self.get_session(session_id)
        session["context"][key] = value

    def get_context(self, session_id):
        return self.get_session(session_id)["context"]

    def get_history(self, session_id):
        return list(self.get_session(session_id)["history"])
