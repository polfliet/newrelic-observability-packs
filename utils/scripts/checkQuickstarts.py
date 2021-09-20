#!/usr/bin/env python3

import os
import yaml
from yaml.loader import SafeLoader

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

    return False

def getInstallPlans(directory):
    #installPlan types: targetedInstall, nerdlet, link
    with open(directory + "/" + "config.yml") as f:
        config = yaml.load(f, Loader=SafeLoader)
        if 'installPlans' in config and len(config['installPlans']) > 0:
            return config['installPlans']

    return []

def listToString(s): 
    str = "" 
    for ele in s: 
        str += ele + ", "  
    return str 

countTotal = 0
countDyesIno = 0
countDyesIyes = 0
countDnoIno = 0
countDnoIyes = 0

def checkDir(directory):
    global countTotal
    global countDyesIno
    global countDyesIyes
    global countDnoIno
    global countDnoIyes
    packsRoot = os.listdir(directory)
    for pack in packsRoot:
        if isPack(directory + pack):
            countTotal += 1
            if hasDashboardOrAlerts(directory + pack):
                if not hasInstallPlan(directory + pack):
                    countDyesIno += 1
                    print(pack + ": DASHB YES INSTALL NO")
                else:
                    countDyesIyes += 1                   
                    print(pack + ": DASHB YES INSTALL YES " + listToString(getInstallPlans(directory + pack)))
            else:
                if not hasInstallPlan(directory + pack):
                    countDnoIno += 1
                    print(pack + ": DASHB NO INSTALL NO")
                else:
                    countDnoIyes += 1
                    print(pack + ": DASHB NO INSTALL YES " + listToString(getInstallPlans(directory + pack)))
        else:
            checkDir(directory + pack + "/")

checkDir("../../packs/")

print("**** RESULTS *****")
print("Total quickstarts: " + str(countTotal))
print("Dashboard/alerts YES, Install Plan NO: " + str(countDyesIno))
print("Dashboard/alerts YES, Install Plan YES: " + str(countDyesIyes))
print("Dashboard/alerts NO, Install Plan NO: " + str(countDnoIno))
print("Dashboard/alerts NO, Install Plan YES: " + str(countDnoIyes))
