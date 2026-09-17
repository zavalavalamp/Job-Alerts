import os

print("EMAIL_ADDRESS =", repr(os.getenv("EMAIL_ADDRESS")))
print("EMAIL_PASSWORD =", "EXISTS" if os.getenv("EMAIL_PASSWORD") else "MISSING")
print("EMAIL_RECIPIENT =", repr(os.getenv("EMAIL_RECIPIENT")))
