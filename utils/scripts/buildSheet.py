#!/usr/bin/env python3

import csv
import pandas
from ruamel.yaml import YAML
import os
from os import path
import pathlib
from yaml.loader import SafeLoader
import sys
import math
import shutil

yaml = YAML()
yaml.width = 4096
f = open('quickstart-dump.csv', 'w')
writer = csv.writer(f)

def isPack(directory):
    return os.path.exists(directory + "/" + "config.yml")

def hasDashboardOrAlerts(directory):
    dashboards = os.path.exists(directory + "/dashboards") and len(os.listdir(directory + "/dashboards")) > 0
    alerts = os.path.exists(directory + "/alerts") and len(os.listdir(directory + "/alerts")) > 0
    return dashboards or alerts

def hasInstallPlan(directory):
    with open(directory + "/" + "config.yml") as f:
        config = yaml.load(f, Loader=SafeLoader)
        if 'installPlans' in config and len(config['installPlans']) > 0:
            return True

def getPackConfig(directory):
    with open(directory + "/" + "config.yml") as configFile:
        config = yaml.load(configFile)
        return config

writer.writerow(['NAME', 'PATH', 'KEYWORDS', 'LEVEL', 'AUTHORS'])

def findPack(directory):
    packsRoot = os.listdir(directory)
    for pack in packsRoot:
        if isPack(directory + pack):
            config = getPackConfig(directory + pack)
            keywords = []
            if 'keywords' in config:
                keywords = config['keywords']
            writer.writerow([pack, directory + pack, keywords, config['level'] , config['authors']])
        else:
            findPack(directory + pack + "/")

findPack("../../packs/")

f.close()