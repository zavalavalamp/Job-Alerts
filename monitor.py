import os

recipient = os.getenv("EMAIL_RECIPIENT")

print("Recipient raw:")
print(repr(recipient))

print("Length:")
print(len(recipient))
