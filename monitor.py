import smtplib
import os
from email.mime.text import MIMEText

sender = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")
recipient = os.getenv("EMAIL_RECIPIENT")

msg = MIMEText(
    "Success!\n\nYour Nike Job Monitor email test worked."
)

msg["Subject"] = "Nike Job Monitor Test"
msg["From"] = sender
msg["To"] = recipient

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, password)
    server.sendmail(sender, [recipient], msg.as_string())

print("Email sent successfully")
