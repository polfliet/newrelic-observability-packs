import csv
import pandas
from ruamel.yaml import YAML
import os
from os import path
import pathlib
from yaml.loader import SafeLoader
import sys
import math


# Reading whole csv file with panda library.
yaml = YAML()
yaml.width = 4096
df = pandas.read_csv('quickstarts-descriptions.csv', sep=',')

description_map = {
    #"<TECHNOLOGY>": ["<SUMMARY>", "DESCRIPTION"],
    "dotnet": [],
    "ruby": [],
    "python": [],
    "java": [
        "Monitor <QUICKSTART_NAME> with New Relic's Java agent",
        "java.md"
    ],
    "aws": [],
    "os": [],
    "mobile": [],
    "apache": [],
    "zookeeper": [],
    "azure": [],
    "browser": [],
    "c": [],
    "c++": [],
    "php": [],
    "cassandra": [],
    "couchbase": [],
    "docker": [],
    "golang": [],
    "elasticsearch": [],
    "node.js": [],
    "f5": [],
    "gcp": [],
    "haproxy": [],
    "jmx": [],
    "kafka": [],
    "kubernetes": [],
    "logstash": [],
    "mariadb": [],
    "memcached": [],
    "micrometer": [],
    "mongodb": [],
    "mssql": [],
    "mysql": [],
    "nagios": [],
    "nginx": [],
    "oracle": [],
    "windows": [],
    "postgres": [],
    "prometheus": [],
    "rabbitmq": [],
    "redis": [],
    "snmp": [],
    "statsd": [],
    "synthetics": [],
    "varnish": [],
    "esxi": [],
    "tanzu": []
}

def dumpToYaml(path, pack_install_key):
    with open(path, 'r+') as outfile:
        documents = yaml.load(outfile)

        if pack_install_key in description_map and len(description_map[pack_install_key]) == 2:           
            summary = description_map[pack_install_key][0]
            descriptionFile = description_map[pack_install_key][1]
            # Read .md file
            file = open("mds/" + descriptionFile)
            description = file.read()
            file.close()

            # Replace placeholders
            summary = summary.replace('<QUICKSTART_NAME>', documents['title'])
            description = description.replace('<QUICKSTART_NAME>', documents['title'])
            description = description.replace('<ORIGINAL_QUICKSTART_SUMMARY>', documents['summary'])
        
            documents['summary'] = summary
            documents['description'] = description      
            outfile.seek(0) # Move position in outfile to front. 
            yaml.indent(sequence=4, offset=2)
            yaml.dump(documents, outfile)
        else:
            print(f'{pack_install_key} not defined')
    outfile.close()

for index, row in df.iterrows(): # Iterates the csv file.
    print('**** Pack ****')
    pack_path = str.lower(row['PATH']).replace(' ', '-') # Path of the pack
    pack_name = row['NAME'] # Name of the pack
    pack_install_key = row['INSTALL_PLAN'] # Install plan for the pack

    # Find the pack
    print(f'Path: {pack_path}')
    path = f'../../packs/{pack_path}/config.yml'
    
    if os.path.exists(path): # Check if the pack exists
        print(f'Pack {pack_name} was found, updating...')
        dumpToYaml(path, pack_install_key)        
    else:
        print(f'Pack {pack_name} was not found at {path}')
    print('\n')