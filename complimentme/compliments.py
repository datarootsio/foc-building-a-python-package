import requests
import random

def fetch_compliments(url):
    """Fetch compliment list from a remote source"""
    try:
        with requests.get(url) as req:
            if req.status_code == 200:
                compliments = req.json()
            else:
                compliments = ['You are awesome! Something is wrong with the compliments database tho :/']
    except requests.exceptions.ConnectionError:
        compliments = ['You are an amazing person <3 unlike your internet connection...']

    return compliments


def main():
    url = 'https://raw.githubusercontent.com/datarootsio/foc-building-a-python-package/master/compliments.json'
    compliments = fetch_compliments(url)
    print(random.choice(compliments))
