#! /usr/bin/python
# -*- coding : utf-8 -*-

import json
import sys
import locale
from dateutil import parser
from utils import read_event_fromfile

import matplotlib.pyplot as plt
import json

def plot_graph(tweets_by_min, groundtruth):
    y = []
    labels = []
    for key, item_nb in tweets_by_min.iteritems():
        labels.append(key)
        y.append(item_nb)

    print labels
    x = range(len(labels))

    plt.plot(x, y, 'ro-')
    plt.xticks(x, labels, rotation='vertical')
    # Pad margins so that markers don't get clipped by the axes
    plt.margins(0.02)
    # Tweak spacing to prevent clipping of tick-labels
    plt.subplots_adjust(bottom=0.15)
    for i, j in groundtruth.iteritems():
        plt.axvline(x=labels.index(i), label=j)
        plt.text(labels.index(i), min(y)+1.5, j,rotation=90)
    plt.show()

def count_tweet_by_minute(tweet, tweets_by_min):
    if "created_at" in tweet:
        created_at = tweet['created_at']
        datetime = parser.parse(created_at)
        minute = int(datetime.strftime("%H"))*60 + int(datetime.strftime("%M"))
        if minute in tweets_by_min:
            tweets_by_min[minute] +=1
        else:
            tweets_by_min[minute] = 1
    return tweets_by_min

#
# usage checking
#

if len(sys.argv) < 2:
    print "usage : ./plot.py name_of_json_file"
    sys.exit()

# locale settings for strptime
locale.setlocale(locale.LC_ALL, "en_US.utf8")

#
# main program
#

filename = sys.argv[1]
tsv_filename = filename.replace("json", "tsv")
tweets_by_min = {}

groundtruth = read_event_fromfile(tsv_filename)
print groundtruth

with open(filename, 'rU') as f:
    for line in f:
        if "euro2016" in line.lower():
            tweet = json.loads(line)
            count_tweet_by_minute(tweet, tweets_by_min)

plot_graph(tweets_by_min, groundtruth)
