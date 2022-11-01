from time import sleep
from requests_html import HTMLSession

session = HTMLSession()
url = 'https://thehackernews.com/'

r = session.get(url)

r.html.render(sleep=1)