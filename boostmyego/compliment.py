import random
import json
from urllib.request import urlopen

COMPLIMENTS = "https://raw.githubusercontent.com/datarootsio/foc-building-a-python-package/master/compliments.json"


def fetch_compliments():
    jsonurl = urlopen(COMPLIMENTS)
    compliments = json.loads(jsonurl.read())
    return compliments


def give_compliment(compliments: list) -> list:
    return random.choice(compliments)
