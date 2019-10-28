# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:45:56 2019

@author: Siva Ranjan
"""

import csv
import sqlite3
import datetime


def TorCD():
    aFlag = 0
    with open('test.csv') as csv_file1:
        csv_reader1 = csv.reader(csv_file1, delimiter=',')
        for row1 in csv_reader1:
            #sslConnections = open("sslTest.txt", "r")
            #sslCert = sslConnections.readline()
            destID = row1[1]   
            srcID = row1[0]
            #print (destID)
            with open('t_tor_server.txt') as csv_file2:
                csv_reader2 = csv.reader(csv_file2, delimiter=',')
                for row2 in csv_reader2:
                    if (destID == row2[0]):
                        #print("HELLO")
                        with open('networkHosts.txt') as csv_file3:
                            csv_reader3 = csv.reader(csv_file3, delimiter=',')
                            for row3 in csv_reader3:
                                if row3 == []:
                                    break
                                elif (srcID == row3[0]):
                                    print ("Connection to Tor Server Detected!")
                                    print (srcID, destID)
                                    raiseAlert(srcID, destID)
                                    return aFlag
                    elif (srcID == row2[0]):
                        with open('networkHosts.txt') as csv_file3:
                            csv_reader3 = csv.reader(csv_file3, delimiter=',')
                            for row3 in csv_reader3:
                                if row3 == []:
                                    break
                                elif (destID == row3[0]):
                                    print ("Connection from Tor Server Detected!")
                                    print (srcID, destID)
                                    aFlag = raiseAlert(srcID, destID)
                                    print (aFlag)
                                    return aFlag
                        
                        
                                    

def raiseAlert(srcID, destID):
    connection = sqlite3.connect("alert.db")
    connection.execute("""CREATE TABLE IF NOT EXISTS tor_alerts
                               (AlertID INT NOT NULL UNIQUE,
                               AlertTime DATETIME NOT NULL,
                               SourceIP VARCHAR(100) NOT NULL,
                               DestIP VARCHAR(100) NOT NULL);""") 
    alertime = datetime.datetime.now()
    cursor = connection.execute("Select * from tor_alerts")
    for row in cursor:
        time1 =  datetime.datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S.%f')
        timedelta = alertime - time1
        if (timedelta.total_seconds() / 3600 > 6):
            print ("New Alert!") 
            file = open("TorID.txt", "r")
            alertID = int(file.readline())
            #print(alertID)
            alertID += 1
            file.close()
            file = open("TorID.txt", "w")
            file.write(str(alertID))
            connection.execute("INSERT INTO ip_alerts VALUES (?, ?, ?, ?)", (alertID, alertime, srcID, destID))
            connection.commit()
            connection.close()
            return 1
    else:
        print("Alert Issued in the last 24 hours")
        connection.close()
        return 0
    #cursor = connection.execute("Select * from ssl_alerts")
    #for row in cursor:
    #    print (row[0], row[1], row[2], row[3], row[4])
    #    #print ( datetime.datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S.%f'))
    #    #print (datetime.now())
    #    print ("Raise Alert")

    #else:
    #   print ("No alert")       
    
    connection.close()
    
    
#print (TorCD())