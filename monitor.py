import os

print("EMAIL_ADDRESS exists:", os.getenv("EMAIL_ADDRESS") is not None)
print("EMAIL_PASSWORD exists:", os.getenv("EMAIL_PASSWORD") is not None)
print("EMAIL_RECIPIENT exists:", os.getenv("EMAIL_RECIPIENT") is not None)

recipient = os.getenv("EMAIL_RECIPIENT")

if recipient:
    print("Recipient length:", len(recipient))
    print("Recipient starts with:", recipient[:5])
