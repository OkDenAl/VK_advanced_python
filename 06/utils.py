from collections import Counter

import requests
from bs4 import BeautifulSoup


def get_common_words(top_words, url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    words = soup.text.split()
    most_common_words = dict(Counter(words).most_common(top_words))

    return most_common_words
