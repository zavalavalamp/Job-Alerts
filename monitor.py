import requests

url = "https://careers.nike.com/jobs?filter%5Bcategory%5D%5B0%5D=Product%20Creation%2C%20Development%20%26%20Management"

response = requests.get(url)

text = response.text

keywords = [
    "api",
    "jobs",
    "search",
    "graphql",
    "__NEXT_DATA__",
    "jobId",
    "opening"
]

for keyword in keywords:
    print(f"\n=== SEARCHING FOR: {keyword} ===")
    print(keyword.lower() in text.lower())
