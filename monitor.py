import requests
import re
import smtplib
import os
from email.mime.text import MIMEText

url = "https://careers.nike.com/jobs?filter%5Bcategory%5D%5B0%5D=Product%20Creation%2C%20Development%20%26%20Management"

html = requests.get(url).text

current_jobs = set(re.findall(r'R-\d+', html))

with open("seen_jobs.txt", "r") as f:
    seen_jobs = set(line.strip() for line in f if line.strip())

new_jobs = current_jobs - seen_jobs

sender = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")
recipient = os.getenv("EMAIL_RECIPIENT")

if new_jobs:

    body = "NEW NIKE JOBS FOUND:\n\n"

    for job in sorted(new_jobs):
        body += f"{job}\n"

    subject = f"Nike Job Alert ({len(new_jobs)} new jobs)"

else:

    body = (
        "Nike Job Monitor Update\n\n"
        "No new jobs found in Product Creation, Development & Management."
    )

    subject = "Nike Job Monitor - No New Jobs"

msg = MIMEText(body)

msg["Subject"] = subject
msg["From"] = sender
msg["To"] = recipient

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, password)
    server.sendmail(sender, [recipient], msg.as_string())

print("Email sent successfully")
