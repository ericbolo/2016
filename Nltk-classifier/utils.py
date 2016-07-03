# -*- coding: utf-8 -*-
from collections import namedtuple
import dateutil.parser
import json
import re

def normalize_text(text):
    norm_text = text.lower()

    # Replace breaks with spaces
    norm_text = norm_text.replace('<br />', ' ')

    # Pad punctuation with spaces on both sides
    for char in ['.', '"', ',', '(', ')', '!', '?', ';', ':']:
        norm_text = norm_text.replace(char, ' ' + char + ' ')

    return norm_text

document_type = namedtuple('document_type', ['words', 'tags', 'event'])
event_names = ['BUT', 'CGT', 'CJA', 'D1P', 'D2P', 'F1P', 'F2P', 'TIR', 'rien']
model_filename = 'model.gensim'
data_filename = 'documents.pkl'
data_dir = 'data'


french_keywords = {
    'BUT': ['but', 'goal', r'\d-\d'],
    'TIR': ['tir', 'tete', 'tête', 'head'],
    'CJA': ['carton', 'jaune', 'yellow', 'card'],
    'CGT': ['changement', 'changements', 'replace', 'replacement'],
    'rien': [],
    'raclette': ['raclette']
}


english_keywords = {
    'BUT': ['goal', r'\d-\d', 'scored', 'score'],
    'TIR': ['shot', 'head'],
    'CJA': ['yellow', 'card'],
    'CGT': ['replace', 'replacement'],
    'PEN': ['penalty'],
    'rien': [],
    'raclette': ['raclette']
}


country_codes = {
    'Romania': ['rou', '#rou', 'romania', '#romania'],
    'France': ['fra', '#fra', 'france', '#france'],
}


def read_tweets(filename):
    data = []

    with open(filename) as f:
        for i, line in enumerate(f):
            try:
                js = json.loads(line)
                text = js['text']

                if not any(keyword in text.lower()
                           for keyword in ('euro2016', 'raclette')):
                    continue

                tweet = {
                    'text': text,
                    'time': dateutil.parser.parse(js['created_at']),
                    'retweet_count': js['retweet_count']
                }

                data.append(tweet)
            except (ValueError, KeyError):
                pass

    return data

def get_category(message):
    counts = {}
    for category, keywords_ in english_keywords.iteritems():
        for keyword in keywords_:
            counts_ = len(re.findall(r'\s+(' + keyword + r')\s+', message))
            if counts_ > 0:
                counts[category] = counts.get(category, 0) + counts_
    return max(counts, key=counts.get) if counts else 'rien'
