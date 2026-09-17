import smtplib
import os

sender = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")
recipient = os.getenv("EMAIL_RECIPIENT")

subject = "Nike Job Monitor Test"

body = """
Success!

If you received this email, GitHub Actions can send Gmail notifications successfully.
"""

message = f"Subject: {subject}\n\n{body}"

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(sender, password)
    smtp.sendmail(sender, recipient, message)

print("Email sent successfully")
