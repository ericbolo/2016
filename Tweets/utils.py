#! /usr/bin/python
# -*- coding : utf-8 -*-

import re
from datetime import datetime, timedelta

def read_players_team_file(filepath="team_composition.txt", team=None):
    regex_team = "#+\s+TEAM\s+(\w+)\s+#+"
    regex_player = "--\s+\d+"
    teams = {}
    current_team = None
    with open(filepath, 'rU') as f:
        for line in f:
            m = re.match(regex_team, line)
            if m:
                current_team = m.group(1)
            if re.match(regex_player, line):
                f.next()
                player = f.next().strip()
                if current_team in teams:
                    teams[current_team].append(player)
                else:
                    teams[current_team] = [player]
    return teams


def read_event_fromfile(tsv_filename):
    groundtruth = {}
    with open(tsv_filename, 'rU') as f:
        next(f)
        for line in f:
            time = datetime.strptime(line.split("\t")[0], "%H:%M:%S")
            time = time - timedelta(hours=2)
            minute = int(time.strftime("%H")) * 60 + int(time.strftime("%M"))
            groundtruth[minute] = line.split("\t")[1]
        return groundtruth


print read_players_team_file()