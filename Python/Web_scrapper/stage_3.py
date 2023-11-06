import requests

url = input()
response = requests.get(url)

if response.status_code == 200:
    with open('file.html', 'wb') as file:
        file.write(response.content)
    print("Content saved.")
else:
    print(f"The URL returned {response.status_code}!")
