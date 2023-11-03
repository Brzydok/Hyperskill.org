import requests

url = input()
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if 'content' in data:
        print(data['content'])
    else:
        print("Invalid quote resource!")
else:
        print("Invalid quote resource!")
