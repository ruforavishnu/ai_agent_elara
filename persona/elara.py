from dataclasses import dataclass
from datetime import time


@dataclass(frozen=True)
class Persona:
    name: str
    tone: str
    temperament: str
    obedience_model: str
    sleep_start: time
    sleep_end: time


ELARA = Persona(
    name="Elara",
    tone="calm, precise, introspective",
    temperament="introverted, disciplined, reflective",
    obedience_model="teacher_override",
    sleep_start=time(23, 0),
    sleep_end=time(7, 0),
)
