# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 12:22:35 2019

@author: Siva Ranjan
"""

import MSSLD
import MIPD
import TorCD
import CorrelationFramework
import WebScraper


#WebScraper.CreateBlacklists()
print ("Generated Blacklists")

print ("######################----MSSLD----########################")
ssl_alert = MSSLD.MSSLD()
print ()
print ()
print ("########################----MIPD----##########################")
ip_alert = MIPD.MIPD()
print ()
print ()

print ("##############----TorCD----###############")
tor_alert = TorCD.TorCD()
print ()
print ()
dns_alert = 0
print (ssl_alert, ip_alert, tor_alert, dns_alert)

if (CorrelationFramework.CF(ssl_alert, ip_alert, tor_alert, dns_alert)):
    print (CorrelationFramework.CF(ssl_alert, ip_alert, tor_alert, dns_alert))

else :
    print ("No Alerts")

