import requests

url = 'http://127.0.0.1:8000/api/'
headers = {
    'Authorization': f'Token d2c8213ed117253083cc9e3fb54d2e30d72b6c37',
}

response = requests.get(url, headers=headers)
print(response.text)
