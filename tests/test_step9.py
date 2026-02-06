from persona.elara import ELARA
from persona.schedule import is_free_time
from persona.reflection import generate_reflection
from memory.journal.writer import write_journal_entry


import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)


print("Agent:", ELARA.name)
print("Temperament:", ELARA.temperament)

reflection = generate_reflection()
assert isinstance(reflection, str)
assert len(reflection) > 20

path = write_journal_entry(reflection)
print("Journal path:", path)

print("Free time now:", is_free_time())

print("✅ Step 9 journal system OK")
