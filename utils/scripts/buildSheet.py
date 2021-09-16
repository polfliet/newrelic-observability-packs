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
# create the csv writer
writer = csv.writer(f)

# Get a list of files in a directory
dirName = '../../packs/'
listOfFiles = list()
for (dirpath, dirnames, filenames) in os.walk(dirName):
    #listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    listOfFiles.append({'dir': dirpath, 'files': filenames})
        
# Print the files   
templates = ['dotnet', 'ruby', 'python', 'java', 'golang', 'node.js', 'php', 'aws', 'azure', 'gcp', 'c', 'c++'] 
writer.writerow(['NAME', 'PATH', 'KEYWORDS', 'TEMPLATE'])
for elem in listOfFiles:
    if len(elem['files']) > 1 and 'config.yml' in elem['files']:
        print('Quickstart found at ' + elem['dir'])
        with open(elem['dir'] + '/config.yml', 'r+') as qsfile:
            qs = yaml.load(qsfile)
            if 'keywords' in qs:
                if any(item in qs['keywords'] for item in templates):
                    writer.writerow([qs['name'], elem['dir'], qs['keywords'], 'NO'])
                else:
                    writer.writerow([qs['name'], elem['dir'], qs['keywords'], 'YES'])
            else:
                writer.writerow([qs['name'], elem['dir'], '', 'YES'])
        qsfile.close()

f.close()
# # Reading whole csv file with panda library.
# yaml = YAML()
# yaml.width = 4096
# df = pandas.read_csv('quickstarts-dashboards.csv', sep=',')

# def copyDashboardsAndAlerts(path, pack_copy_from):
#     # Copy dashboards if it does not exist yet
#     if not os.path.exists(path + '/dashboards'):
#         src = "../../packs/" + pack_copy_from + "/" + pack_copy_from + "/dashboards/"
#         if os.path.exists(src):
#             shutil.copytree(src, path + '/dashboards/') # APM packs are currently always in name/name
#         else:
#             print(f'Dashboards for {pack_copy_from} not found')
        
#     # Copy alerts if it does not exist yet
#     if not os.path.exists(path + '/alerts'):
#         src = "../../packs/" + pack_copy_from + "/" + pack_copy_from + "/alerts/"
#         if os.path.exists(src):
#             shutil.copytree(src, path + '/alerts/') # APM packs are currently always in name/name
#         else:
#             print(f'Alerts for {pack_copy_from} not found')

# def isNaN(string):
#     return string != string

# for index, row in df.iterrows(): # Iterates the csv file.
#     print('**** Pack ****')
#     pack_path = str.lower(row['PATH']).replace(' ', '-') # Path of the pack
#     pack_name = row['NAME'] # Name of the pack
#     pack_copy_from = row['DASHBOARD_COPY'] # Where to copy dashboards & alerts from

#     if not isNaN(pack_copy_from):
#         # Find the pack
#         print(f'Path: {pack_path}')
#         path = f'../../packs/{pack_path}'
        
#         if os.path.exists(path): # Check if the pack exists
#             print(f'Pack {pack_name} was found, updating...')
#             copyDashboardsAndAlerts(path, pack_copy_from)        
#         else:
#             print(f'Pack {pack_name} was not found at {path}')

#         print('\n')