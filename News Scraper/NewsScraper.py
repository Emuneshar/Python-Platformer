import requests
from bs4 import BeautifulSoup

urls = [
    "https://abcnews.go.com/", 
    "https://www.cnn.com/", 
    "https://www.foxnews.com/", 
    "https://www.nbcnews.com/"  
]

def scraper(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    if "abcnews.go.com" in url:
        articles = soup.find_all("a", class_="AnchorLink")

    elif "cnn.com" in url:
        articles = soup.find_all("h3", class_="cd__headline")

    elif "foxnews.com" in url:
        articles = soup.find_all("h2", class_="title")

    elif "nbcnews.com" in url:  
        articles = soup.find_all("h3", class_="tease-card__headline")

    else:
        print(f"No URL pattern found for the provided site: {url}")
        return

    for article in articles:
        title = article.text.strip()

        parent_a = article.find_parent('a')
        if parent_a and 'href' in parent_a.attrs:
            link = parent_a['href']
        elif 'href' in article.attrs:
            link = article['href']
        else:
            continue

        
        if not link.startswith('http'):
            if "abcnews.go.com" in url:
                link = 'https://abcnews.go.com' + link
            elif "cnn.com" in url:
                link = 'https://www.cnn.com' + link
            elif "foxnews.com" in url:
                link = 'https://www.foxnews.com' + link
            elif "nbcnews.com" in url:
                link = 'https://www.nbcnews.com' + link

        print(f"Title: {title}")
        print(f"Link: {link}")
        print('-' * 80)

for url in urls:
    print(f"Getting headlines from {url}")
    scraper(url)
