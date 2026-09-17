import requests
import re

url = "https://careers.nike.com/jobs?filter%5Bcategory%5D%5B0%5D=Product%20Creation%2C%20Development%20%26%20Management"

html = requests.get(url).text

matches = re.findall(r'/job/[^"\']+', html)

print("Found:", len(matches), "job links")

for m in matches[:20]:
    print(m)
