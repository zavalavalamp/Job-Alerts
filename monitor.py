import requests
import re

url = "https://careers.nike.com/jobs?filter%5Bcategory%5D%5B0%5D=Product%20Creation%2C%20Development%20%26%20Management"

html = requests.get(url).text

job_ids = sorted(set(re.findall(r'R-\d+', html)))

print("Found", len(job_ids), "unique jobs")

for job in job_ids:
    print(job)
