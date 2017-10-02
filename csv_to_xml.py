#Tested on Python 3.5.2
#Author: Nathaniel Charlebois
import csv
import threading
import sys
from xml.etree import ElementTree as et

CSV_FILENAME_CONSTANT = 'house.csv'
XML_FILENAME_CONSTANT = 'house.xml'
TIME_CONSTANT = 60*15  #seconds*minutes


def csv_to_xml():
    """
    Reads the next entry in CSV_FILENAME_CONSTANT and writes the time
        and current load to XML_FILENAME_CONSTANT.
    A thread is then instantiated to execute csv_to_xml() after the attached
        TIME_CONSTANT has elapsed.
    Once EOF is reached, the program will throw an exception and terminate.
    """
    current = next(reader, None) #If python 2.7 use reader.next()
    time = current[0]
    load = current[1]

    tree = et.parse(XML_FILENAME_CONSTANT)
    tree.find('.//currentload').text = load
    tree.find('.//time').text = time
    tree.write(XML_FILENAME_CONSTANT)
    threading.Timer(TIME_CONSTANT, csv_to_xml).start()
    pass

#Open the csv file
csv_file = open(CSV_FILENAME_CONSTANT,'r')
reader = csv.reader(csv_file)
headers = next(reader, None) #If python 2.7 use reader.next()
#Read the first csv entry
csv_to_xml()
