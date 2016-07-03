#! /usr/bin/python
# -*- coding : utf-8 -*-

import sys
import json
import locale
from dateutil import parser
from utils import read_event_fromfile

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

with open(filename, 'rU') as f:
    with open(filename.replace("json", "filtered.json"), "a") as out:
        for line in f:
            if "euro2016" in line.lower():
                tweet = json.loads(line)
                tweet_out = {}
                tweet_out["text"] = tweet["text"]
                tweet_out["retweet_count"] = tweet["retweet_count"]
                tweet_out["created_at"] = tweet["created_at"]

                out.write(json.dumps(tweet_out))
                out.write("\n")