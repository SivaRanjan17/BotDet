# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 23:11:28 2019

@author: Siva Ranjan
"""
import csv
import sqlite3
import datetime


def MIPD():
    aFlag = 0
    with open('test.csv') as csv_file1:
        csv_reader1 = csv.reader(csv_file1, delimiter=',')
        for row1 in csv_reader1:
            #sslConnections = open("sslTest.txt", "r")
            #sslCert = sslConnections.readline()
            destID = row1[1]   
            srcID = row1[0]
            #print (destID)
            with open('t_ip_blacklist.txt') as csv_file2:
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
                                    print ("Malicious Destination IP Address Detected!")
                                    print (srcID, destID)
                                    raiseAlert(srcID, destID)
                    elif (srcID == row2[0]):
                        with open('networkHosts.txt') as csv_file3:
                            csv_reader3 = csv.reader(csv_file3, delimiter=',')
                            for row3 in csv_reader3:
                                if row3 == []:
                                    break
                                elif (destID == row3[0]):
                                    print ("Malicious Source IP Address Detected!")
                                    print (srcID, destID)
                                    aFlag = raiseAlert(srcID, destID)
                                    return aFlag
                        
                        
                                    

def raiseAlert(srcID, destID):
    connection = sqlite3.connect("alert.db")
    connection.execute("""CREATE TABLE IF NOT EXISTS ip_alerts
                               (AlertID INT NOT NULL UNIQUE,
                               AlertTime DATETIME NOT NULL,
                               SourceIP VARCHAR(100) NOT NULL,
                               DestIP VARCHAR(100) NOT NULL);""") 
    alertime = datetime.datetime.now()
    cursor = connection.execute("Select * from ip_alerts")
    for row in cursor:
        time1 =  datetime.datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S.%f')
        timedelta = alertime - time1
        if (timedelta.total_seconds() / 3600 > 6):
            print ("New Alert!") 
            file = open("IPID.txt", "r")
            alertID = int(file.readline())
            #print(alertID)
            alertID += 1
            file.close()
            file = open("IPID.txt", "w")
            file.write(str(alertID))
            connection.execute("INSERT INTO ip_alerts VALUES (?, ?, ?, ?)", (alertID, alertime, srcID, destID))
            connection.commit()
            connection.close()
            return 1
    else:
        print("Alert Issued in the last 24 hours")
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
    
    
#MIPD()
