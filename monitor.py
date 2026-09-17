import smtplib
import os
***m email.mime.text import MIMETex***sender = os.getenv("EMAIL_ADDRES***
password = os.getenv("EMAIL_PAS***RD")
recipient = os.getenv("EMAI***ECIPIENT")

msg = MIMEText(
    ***ccess!\n\nYour Nike Job Monitor ***il test worked."
)

msg["Subject***= "Nike Job Monitor Test"
msg["F***"] = sender
msg["To"] = recipien***with smtplib.SMTP_SSL("smtp.gmai***om", 465) as server:
    server.***in(sender, password)
    server***ndmail(sender, [recipient], msg.***string())

print("Email sent suc***sfully")
