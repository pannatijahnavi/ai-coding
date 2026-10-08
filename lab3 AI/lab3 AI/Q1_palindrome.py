email = "Here is the monthly newsletter for your information."

if "down" in email.lower() or "failure" in email.lower() or "urgent" in email.lower():
    priority = "High Priority"
elif "schedule" in email.lower() or "tomorrow" in email.lower():
    priority = "Medium Priority"
else:
    priority = "Low Priority"

print(priority)