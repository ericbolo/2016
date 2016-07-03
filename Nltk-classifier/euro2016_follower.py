#!/usr/bin/python2
from __future__ import print_function, division
import json
import logging
import time
import random
import datetime
import sys
import re
import requests
import dateutil.parser
from utils import read_tweets, get_category, country_codes
from collections import Counter


def get_tweets_around(time, data, delta=120):
    res = []
    delta_ = datetime.timedelta(seconds=delta)
    for tweet in data:
        if time >= tweet['time'] >= time - delta_:
            res.append(tweet)
    return res


def parse_tweets(tweets, event_name='BUT'):
    if event_name == 'BUT':
        countries = {}   # reversed country codes
        for country_name, codes in country_codes.iteritems():
            for code in codes:
                countries[code] = country_name

        regex = r'(?:^|\s)({0})\s+(\d)(?:-|\s)(\d)\s+({0})(?:$|\s)'.format(
            r'|'.join(countries.keys())
        )

        scores = []

        for tweet in tweets:
            match = re.search(regex, tweet['text'], flags=re.IGNORECASE)
            if match:
                country1, score1, score2, country2 = match.groups()
                country1 = countries[country1.lower()]
                country2 = countries[country2.lower()]
                scores.append((country1, score1, country2, score2))

        return scores
    else:
        return None


def follow_euro_2016(user_data, callback, data, delta=60):
    # logging.info('following Euro2016')
    # goal at 22:17
    current_time = dateutil.parser.parse(
        '06/10/2016 22:14:00 +0200'
    )

    current_counter = Counter()
    last_goal = None
    min_time = datetime.timedelta(minutes=4)
    previous_score = 0, 0

    while True:
        tweets = get_tweets_around(current_time, data, delta)

        categories = [
            get_category(tweet['text']) for tweet in tweets
        ]
        counter = Counter(categories)

        # logging.info('%s %s', current_time, counter)
        if (counter['BUT'] > current_counter['BUT'] + 50 and
                (last_goal is None or current_time >= last_goal + min_time)):
            # for tweet in random.sample(tweets, 10):
            #    logging.debug(tweet['text'])
            scores = parse_tweets(tweets)
            scores = Counter(scores)
            if scores:
                country1, score1, country2, score2 = max(scores, key=scores.get)
                score1 = int(score1)
                score2 = int(score2)

                prev_score1, prev_score2 = previous_score
                if score1 - prev_score1 + score2 - prev_score2 == 1:
                    scorer = country1 if score1 > prev_score1 else country2

                    previous_score = score1, score2
                    yield country1, score1, country2, score2, scorer
                    last_goal = current_time

        time.sleep(delta)
        current_time += datetime.timedelta(seconds=delta)
        current_counter = counter


if __name__ == '__main__':
    tweet_filename = 'data/France_Roumanie_2016-06-10_21h_en.filtered.json'
    data = read_tweets(tweet_filename)
    for country1, score1, country2, score2, scorer in follow_euro_2016(None, None, data):
        scored_against = country1 if scorer == country2 else country2
        print('{scorer} just scored against {against}! - new score: {country1} {score1}-{score2} {country2}'.format(
            scorer=scorer, against=scored_against, country1=country1, country2=country2,
            score1=score1, score2=score2
        ))
        sys.stdout.flush()