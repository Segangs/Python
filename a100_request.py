import requests


url ="https://naver.com"
response = requests.get(url)

print("status", response.status_code)
print("text", response.text)
