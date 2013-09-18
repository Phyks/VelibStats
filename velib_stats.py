#! /usr/bin/env python3.3

import sys
import os
import datetime
import urllib3
import xml.etree.ElementTree as ET

# Change working directory if necessary
file_path = os.path.dirname(__file__)
if file_path != "":
    os.chdir(file_path)

if len(sys.argv) != 2:
    exit('Usage : velib_stats.py Station_number')

# Parameters
station_number = int(sys.argv[1])
url = ('http://www.velib.paris.fr/service/stationdetails/paris/' +
       str(station_number))

# Initialize libraries
http = urllib3.PoolManager()
today = datetime.datetime.now()

# Get the response from velib REST API
r = http.request('GET', url)

if r.status == 200:
    station_xml = ET.fromstring(r.data)

    # Get station status
    write = today.strftime('%H\t\t%M')

    for child in station_xml.iter('available'):
        write += "\t\t"+child.text
    for child in station_xml.iter('free'):
        write += "\t\t"+child.text

    try:
        # If file exists, check last updated day
        with open('data/'+str(station_number), 'r') as fh:
            lines = fh.readlines()
            for line in reversed(lines):
                if "Jour" in line:
                    previous_day = line[7:]
        # If today != last day of update, add a header
        previous_day = previous_day.split("/")
        if (previous_day[0] != today.strftime('%d') and
           previous_day[1] != today.strftime('%m')):
            write = ("Jour = "+today.strftime('%d/%m')+"\n" +
                     "======================\n" +
                     "Heure\t\tMin\t\tDispos\t\tPlaces\n" +
                     write)

        # Write content to file
        with open('data/'+str(station_number), 'a') as fh:
            fh.write("\n"+write)
            print(write)
    except IOError:
        # If file doesn't exist, create it
        write = ("Données pour la station n°"+str(station_number)+"\n" +
                 "==============================================\n\n" +
                 "Jour = "+today.strftime('%d/%m')+"\n" +
                 "======================\n" +
                 "Heure\t\tMin\t\tDispos\t\tPlaces\n" +
                 write)
        with open('data/'+str(station_number), 'w') as fh:
            fh.write(write)
            print(write)

else:
    exit('Erreur lors de la récupération des infos sur la station' +
         station_number)
