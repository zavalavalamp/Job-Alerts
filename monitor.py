import requests

url = "https://careers.nike.com/jobs?filter%5Bcategory%5D%5B0%5D=Product%20Creation%2C%20Development%20%26%20Management"

response = requests.get(url)

print("Status code:", response.status_code)
print("Page length:", len(response.text))
