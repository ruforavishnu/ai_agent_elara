import json
from datetime import datetime
from pathlib import Path

GUESTBOOK_PATH = Path("memory/guestbook/messages.json")

class Guestbook:
    def __init__(self):
        # Create file if it does not exist
        if not GUESTBOOK_PATH.exists():
            GUESTBOOK_PATH.parent.mkdir(parents=True, exist_ok=True)
            GUESTBOOK_PATH.write_text(json.dumps([]))
        self.load_messages()

    def load_messages(self):
        with open(GUESTBOOK_PATH, "r") as f:
            self.messages = json.load(f)

    def save_messages(self):
        with open(GUESTBOOK_PATH, "w") as f:
            json.dump(self.messages, f, indent=2)

    def add_message(self, sender: str, content: str):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "sender": sender,
            "content": content
        }
        self.messages.append(entry)
        self.save_messages()

    def get_messages(self, last_n: int = 10):
        return self.messages[-last_n:]

    def show_messages(self):
        for msg in self.messages:
            print(f"[{msg['timestamp']}] {msg['sender']}: {msg['content']}")
