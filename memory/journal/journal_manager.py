import os
from datetime import date

JOURNAL_DIR = "memory/journal/entries"


class JournalManager:
    def __init__(self):
        os.makedirs(JOURNAL_DIR, exist_ok=True)

    def _today_path(self) -> str:
        today = date.today().isoformat()
        return os.path.join(JOURNAL_DIR, f"{today}.md")

    def read_today(self) -> str:
        path = self._today_path()
        if not os.path.exists(path):
            return ""
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    def append(self, text: str):
        path = self._today_path()
        with open(path, "a", encoding="utf-8") as f:
            f.write(text.strip() + "\n\n")
