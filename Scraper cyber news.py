from bs4 import BeautifulSoup
import requests
import time

def cyber_news():
    html_text = requests.get('https://thehackernews.com/').text
    soup = BeautifulSoup(html_text, 'lxml')
    articles = soup.find_all('div', class_ = 'body-post clear')
    for article in articles:
        news_name = article.find('h2', class_ = 'home-title').text
        date = article.find('div', class_ = 'item-label').text.replace('', ' Author: ').replace('\ue802', '').replace('\n', '')
        description = article.find('div', class_ = 'home-desc').text
        link = article.a['href']

        print(f"The Hacker News: {news_name, date}")
        print(f"{description}")
        print(f'Link: {link}')

        print('')
if __name__ == '__main__':
    while True:
        cyber_news()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)