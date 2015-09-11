__author__ = 'saurabh'

import csv,sys
from src.conf import loggingmix
from src.conf.conf import database

def write_data(data):
    status = False
    try :
        with open(database+'mikudb.csv', 'a') as csvfile:
            fieldnames = ['title','filename','fbid']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            check_status = get_data(data["fbid"])
            if check_status != True:
                status = True
                writer.writerow(data)
        print "check database status " , status
    except Exception as e:
        loggingmix.ERROR("FileName : database.py :Function :Write Data Error:"+str(e))
        pass


    return status

def get_data(fbid):
    status = False
    with open(database+'mikudb.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["fbid"]==fbid:
                status = True

    return status

# print write_data({'title': 'Checking A File', 'filename':"filexyz.png", "fbid":"11211121_4564789"})
