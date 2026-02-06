from datetime import datetime
from pathlib import Path

JOURNAL_DIR = Path("memory/journal/entries")
JOURNAL_DIR.mkdir(parents=True, exist_ok=True)


def write_journal_entry(text: str, now: datetime | None = None) -> Path:
    now = now or datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    filename = JOURNAL_DIR / f"{date_str}.md"

    entry = f"""# Journal — {date_str}

{text}

---
Written at {now.isoformat()}
"""

    filename.write_text(entry, encoding="utf-8")
    return filename
