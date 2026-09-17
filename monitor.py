import os

recipient = os.getenv("EMAIL_RECIPIENT", "MISSING")

print("Recipient value exists:", recipient != "")
print("Recipient length:", len(recipient))
print("Recipient first 3 chars:", recipient[:3])
