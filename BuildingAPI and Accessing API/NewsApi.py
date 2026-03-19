import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_news(topic,from_date,to_date,language='en',api=os.getenv("API_TOKEN")):
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api}'
    r=requests.get(url)
    content=r.json()
    articles=content['articles']
    results=[]  
    for article in articles:
        results.append(f"TITLE\n {article['title']}'\nDescription\n'{article['description']}")
    return results

print(get_news(topic='space',from_date='2026-03-15',to_date='2026-03-19'))