import requests
from bs4 import BeautifulSoup
import string

# Get the webpage
url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3'
response = requests.get(url)

# Parse the content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all articles
articles = soup.find_all('article')

# Initialize list to store saved articles
saved_articles = []

# Iterate over articles
for article in articles:
    # Check if the article is of type 'News'
    if 'News' in article.find('span', {'data-test': 'article.type'}).text:
        # Get the link to the article
        article_link = article.find('a', {'data-track-action': 'view article'})['href']

        # Access the article page
        article_response = requests.get('https://www.nature.com' + article_link)
        article_soup = BeautifulSoup(article_response.content, 'html.parser')

        # Extract the title and content
        article_title = article_soup.find('h1').text.strip()

        # Check if the article__body exists before extracting text
        if article_soup.find('div', {'class': 'article__body'}):
            article_body = article_soup.find('div', {'class': 'article__body'}).text.strip()
        else:
            article_body = 'No content available.'

        # Remove punctuation from the title
        for char in string.punctuation:
            article_title = article_title.replace(char, '')

        # Replace whitespaces in the title with underscores
        article_title = article_title.replace(' ', '_')

        # Save the article content to a file
        with open(f'{article_title}.txt', 'wb') as file:
            file.write(article_body.encode('utf-8'))

        # Add the saved article to the list
        saved_articles.append(f"{article_title}.txt")

# Print the list of saved articles
print("Saved articles: ", saved_articles)
