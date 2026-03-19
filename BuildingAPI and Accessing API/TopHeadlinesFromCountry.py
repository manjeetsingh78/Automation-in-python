import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_top_headlines_from_country(country, api_key=os.getenv("API_TOKEN")):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    results = []
    for article in articles:
        results.append(f"TITLE\n {article['title']}'\nDescription\n'{article['description']}")
    return results

print(get_top_headlines_from_country(country="us"))