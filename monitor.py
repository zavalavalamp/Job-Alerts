import requests
import re

url = "https://careers.nike.com/jobs?filter%5Bcategory%5D%5B0%5D=Product%20Creation%2C%20Development%20%26%20Management"

html = requests.get(url).text

current_jobs = set(re.findall(r'R-\d+', html))

with open("seen_jobs.txt", "r") as f:
    seen_jobs = set(line.strip() for line in f)

new_jobs = current_jobs - seen_jobs

if new_jobs:
    print("NEW JOBS FOUND:")
    for job in sorted(new_jobs):
        print(job)
else:
    print("No new jobs found.")
