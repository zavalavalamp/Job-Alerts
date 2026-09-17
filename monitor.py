import smtplib
import os
from email.message import EmailMessage

sender = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")
recipient = os.getenv("EMAIL_RECIPIENT")

msg = EmailMessage()
msg["Subject"] = "Nike Job Monitor Test"
msg["From"] = sender
msg["To"] = recipient

msg.set_content(
    "Success!\n\nIf you received this email, your Nike Job Monitor email notifications are working."
)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(sender, password)
    smtp.send_message(msg)

print("Email sent successfully")
