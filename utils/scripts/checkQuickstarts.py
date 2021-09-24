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

def checkInstallPlanIsDoc(directory):
    # installPlan types: targetedInstall, nerdlet, link
    # Check if it is proper install plan or a docs link
    with open(directory + "/" + "config.yml") as f:
        config = yaml.load(f, Loader=SafeLoader)
        if 'installPlans' in config and len(config['installPlans']) > 0:
            for plan in config['installPlans']:
                if 'docs' in plan or 'third-party' in plan:
                    return True

    return False

def listToString(s): 
    str = "" 
    for ele in s: 
        str += ele + ", "  
    return str 

countTotal = 0
countDashboardYesPlanNo = 0
countDashboardYesPlanYes = 0
countDashboardYesPlanYesOnlyDoc = 0
countDashboardNoPlanNo = 0
countDashboardNoPlanYes = 0
countDashboardNoPlanYesOnlyDoc = 0

def checkDir(directory):
    global countTotal
    global countDashboardYesPlanNo
    global countDashboardYesPlanYes
    global countDashboardYesPlanYesOnlyDoc
    global countDashboardNoPlanNo
    global countDashboardNoPlanYes
    global countDashboardNoPlanYesOnlyDoc
    packsRoot = os.listdir(directory)
    for pack in packsRoot:
        if isPack(directory + pack):
            countTotal += 1
            if hasDashboardOrAlerts(directory + pack):
                if not hasInstallPlan(directory + pack):
                    countDashboardYesPlanNo += 1
                    print(pack + ": DASHB YES INSTALL NO")
                else:
                    if checkInstallPlanIsDoc(directory + pack):
                        countDashboardYesPlanYesOnlyDoc += 1
                        print(pack + ": DASHB YES INSTALL YES DOCONLY")
                    else:                       
                        countDashboardYesPlanYes += 1
                        print(pack + ": DASHB YES INSTALL YES")
            else:
                if not hasInstallPlan(directory + pack):
                    countDashboardNoPlanNo += 1
                    print(pack + ": DASHB NO INSTALL NO")
                else:
                    if checkInstallPlanIsDoc(directory + pack):
                        countDashboardNoPlanYesOnlyDoc += 1
                        print(pack + ": DASHB NO INSTALL YES DOCONLY")
                    else:
                        countDashboardNoPlanYes += 1
                        print(pack + ": DASHB NO INSTALL YES")
        else:
            checkDir(directory + pack + "/")

checkDir("../../quickstarts/")

print("**** RESULTS *****")
print("Total quickstarts: " + str(countTotal))
print("Dashboard/alerts YES, Install Plan NO: " + str(countDashboardYesPlanNo))
print("Dashboard/alerts YES, Install Plan YES: " + str(countDashboardYesPlanYes))
print("Dashboard/alerts YES, Install Plan YES, Doc ONLY: " + str(countDashboardYesPlanYesOnlyDoc))
print("Dashboard/alerts NO, Install Plan NO: " + str(countDashboardNoPlanNo))
print("Dashboard/alerts NO, Install Plan YES: " + str(countDashboardNoPlanYes))
print("Dashboard/alerts NO, Install Plan YES, Doc ONLY: " + str(countDashboardNoPlanYesOnlyDoc))
