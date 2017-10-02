##############################################################################
#
#Class:             xml_to_db.py
#Project:           N/A
#Author:            Jason Van Kerkhoven
#Date of Update:    02/10/2017
#Version:           1.0.0
#
#Purpose:           Scan xml file for changes periodically.
#                   Save changes to SQLite database
#
#Update Log:        v1.0.0
#                       - null
#
##############################################################################



#import external libraries
import sqlite3
import sys
import time
from time import gmtime, strftime
import xml.etree.ElementTree as et



#Program constants
YEAR_CONSTANT = '20'



#call using xml_to_db.py mydatabase.db myxml.xml checkfreq
############################| MAIN RUNTIME |##################################
#connect to database
connection = sqlite3.connect(sys.argv[1])
curser = connection.cursor()

#get program params
xml = sys.argv[2]
wait = int(sys.argv[3])


prevTime = '00-00-00 hh:mm'
#main run loop
while(True):
    #open XML file and get timestamp
    tree = et.parse(xml)
    newTime = tree.find('.//time').text

    if (newTime != prevTime):
        #save info to db
        print('New timestamp found! Saving to database...')
        load = tree.find('.//currentload').text
        houseID = tree.find('.//homeid').text
        prevTime = newTime

        #parse date-time into correct format
        dateTime = prevTime.split(' ')
        dmy = dateTime[0].split('-')
        dateFormated = YEAR_CONSTANT + dmy[2] + '-' + dmy[1] + '-' + dmy[0]

        #insert to db
        insert = "INSERT INTO usages values(date('" + dateFormated + "'),time('" + dateTime[1] + "')," + houseID + "," + load + ")"
        print(insert)
        curser.execute(insert)
        connection.commit()
    else:
        print('Checking...')
    
    #
    time.sleep(wait)



