from chat.guestbook import Guestbook

# Initialize guestbook
gb = Guestbook()

# Teacher sends instruction
gb.add_message("Teacher", "Elara, read Ethereum Reddit and summarize.")

# Elara responds (mock)
gb.add_message("Elara", "Understood. I will check Reddit and summarize in my journal.")

# Show messages
gb.show_messages()

# Test passes if last message sender == Elara
assert gb.get_messages()[-1]["sender"] == "Elara"
print("✅ Step 10 guestbook system OK")
