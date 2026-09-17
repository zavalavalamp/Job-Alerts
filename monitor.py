import requests
import re

url = "https://careers.nike.com/jobs?filter%5Bcategory%5D%5B0%5D=Product%20Creation%2C%20Development%20%26%20Management"

html = requests.get(url).text

job_ids = set(re.findall(r'R-\d+', html))

print("Found", len(job_ids), "jobs")

with open("seen_jobs.txt", "w") as f:
    for job in sorted(job_ids):
        f.write(job + "\n")

print("Saved all job IDs")
