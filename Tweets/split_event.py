#! /usr/bin/python
# -*- coding : utf-8 -*-

import sys
import json
import locale
from dateutil import parser
from utils import read_event_fromfile


def split_tweets_by_event(tweet, groundtruth):
    groundtruth_expanded = {}
    for minute, event in groundtruth.iteritems():
        filename_pretty = event + ".json"
        groundtruth_expanded[minute - 1] = filename_pretty
        groundtruth_expanded[minute] = filename_pretty
        groundtruth_expanded[minute + 1] = filename_pretty

    if "created_at" in tweet:
        created_at = tweet['created_at']
        datetime = parser.parse(created_at)
        minute = int(datetime.strftime("%H")) * 60 + int(datetime.strftime("%M"))
        if minute in groundtruth_expanded:
            with open(groundtruth_expanded[minute], "a") as myfile:
                myfile.write(json.dumps(tweet))
                myfile.write("\n")
        else:
            with open("rien.json", "a") as myfile:
                myfile.write(json.dumps(tweet))
                myfile.write("\n")
#
# usage checking
#

if len(sys.argv) < 2:
    print "usage : ./plot.py name_of_json_file"
    sys.exit()
# Locale settings for strptime
locale.setlocale(locale.LC_ALL, "en_US.utf8")

#
# main program
#

filename = sys.argv[1]
tsv_filename = filename.replace("json", "tsv")

groundtruth = read_event_fromfile(tsv_filename)
print groundtruth

with open(filename, 'rU') as f:
    for line in f:
        if "euro2016" in line.lower():
            tweet = json.loads(line)
            split_tweets_by_event(tweet, groundtruth)