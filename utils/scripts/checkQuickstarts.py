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

def checkDir(directory):
    packsRoot = os.listdir(directory)
    for pack in packsRoot:
        if isPack(directory + pack):
            if hasDashboardOrAlerts(directory + pack):
                if not hasInstallPlan(directory + pack):
                    print(pack + ": No installation plan found")
                else:
                    print(pack + ": Installation plan found")
            else:
                if not hasInstallPlan(directory + pack):
                    print(pack + ": No dashboards or alerts, no installation plan found")
                else:
                    print(pack + ": No dashboards or alerts, only an installation plan found")
        else:
            checkDir(directory + pack + "/")

checkDir("../../packs/")
