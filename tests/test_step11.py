from persona.elara_ai import ElaraAI

try:
    # Initialize AI agent
    elara = ElaraAI()

    # Example message for diary entry
    messages = [
        {"role": "system", "content": "You are Elara, a feminine, introverted AI agent."},
        {"role": "user", "content": "Write a short diary entry about your free time activities today."}
    ]

    # Generate text
    text = elara.generate_text(messages)
    print("Generated text:\n", text)

    # Simple check
    assert len(text) > 0
    print("✅ Step 11 persona-aware LLM output OK")

except Exception as e:
    print("❌ Step 11 test failed:", e)
