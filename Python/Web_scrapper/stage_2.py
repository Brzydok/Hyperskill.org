import requests
from bs4 import BeautifulSoup

url = input()
if 'articles' in url and 'nature.com' in url:
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
else:
    print('Invalid page!')
    response = None

if response and response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string.strip()
    summary = soup.find('meta', {'name': 'description'}).get('content')
    print(f'"title": {title}, "description": {summary}')
elif response:
    print('Invalid page!')
