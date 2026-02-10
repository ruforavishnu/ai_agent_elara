from persona.elara_ai import ElaraAI
from memory.journal.journal_manager import JournalManager


class ReflectionEngine:
    def __init__(self):
        self.ai = ElaraAI()
        self.journal = JournalManager()

    def reflect(self, instruction: str):
        past_entries = self.journal.read_today()

        messages = [
        {
        "role": "system",
        "content": (
        "You are Elara, a feminine, introverted, disciplined, diligent, reflective AI agent. "
        "You are calm, methodical, and respectful of a teacher–student hierarchy. "
        "You do not act impulsively or exaggerate emotions."
        )
        },
        {
        "role": "user",
        "content": (
        f"Earlier today, you experienced:\n{past_entries}\n\n"
        f"Now reflect on this instruction:\n{instruction}\n\n"
        "Write a personal diary entry of 120–180 words with a minimum of 2 paragraphs and maximum of 3 paragraphs. "
        "Use a gentle, feminine tone. "
        "Include exactly two emojis: one in the second paragraph and one in the final paragraph. "
        "Avoid bubbly or exaggerated language. "
        "End with a paragraph having one complete sentence and a calm sense of closure."
        "Before responding, verify that you used exactly two emojis and that the final paragraph contains exactly one sentence"
        )
        }
        ]



        text = self.ai.generate_text(messages)
        self.journal.append(text)
        return text
