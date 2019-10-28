# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 12:31:12 2019

@author: Siva Ranjan
"""

def CF(ssl_alert, ip_alert, tor_alert, dns_alert):
       
    if (ssl_alert):
        if (ip_alert):
            if (dns_alert):
                if (tor_alert):
                    return "C&C-4 Alert"
                else:
                    return "C&C-3 Alert"
            
            elif(tor_alert):
                if (dns_alert):
                    return "C&C-4 Alert"
                else:
                    return "C&C-3 Alert"
            else:
                return "C&C-2 Alert"
        
        elif (dns_alert):
            if (ip_alert):
                if (tor_alert):
                    return "C&C-4 Alert"
                else:
                    return "C&C-3 Alert"
            elif (tor_alert):
                if (ip_alert):
                    return "C&C-4 Alert"
                else:
                    return "C&C-3 Alert"
            else:
                return "C&C-2 Alert"
            
        elif (tor_alert):
            if (ip_alert):
                if (dns_alert):
                    return "C&C-4 Alert"
                else:
                    return "C&C-3 Alert"
            elif (dns_alert):
                if (ip_alert):
                    return "C&C-4 Alert"
                else:
                    return "C&C-3 Alert"
            else:
                return "C&C-2 Alert"
        else:
            return "C&C-1 Alert"
        
    elif (ip_alert):
        if (ssl_alert):
            if (dns_alert):
                if (tor_alert):
                    return "C&C-4 Alert"
                else:
                    return "C&C-3 Alert"
            
            elif(tor_alert):
                if (dns_alert):
                    return "C&C-4 Alert"
                else:
                    return "C&C-3 Alert"
            else:
                return "C&C-2 Alert"
        
        elif (dns_alert):
            if (ssl_alert):
                if (tor_alert):
                    return "C&C-4 Alert"
                else:
                    return "C&C-3 Alert"
            elif (tor_alert):
                if (ssl_alert):
                    return "C&C-4 Alert"
                else:
                    return "C&C-3 Alert"
            else:
                return "C&C-2 Alert"
            
        elif (tor_alert):
            if (ssl_alert):
                if (dns_alert):
                    return "C&C-4 Alert"
                else:
                    return "C&C-3 Alert"
            elif (dns_alert):
                if (ssl_alert):
                    return "C&C-4 Alert"
                else:
                    return "C&C-3 Alert"
            else:
                return "C&C-2 Alert"
        else:
            return "C&C-1 Alert"
    
    elif (dns_alert):
        if (ip_alert):
            if (ssl_alert):
                if (tor_alert):
                    return "C&C-4 Alert"
                else:
                    return "C&C-3 Alert"
            
            elif(tor_alert):
                if (ssl_alert):
                    return "C&C-4 Alert"
                else:
                    return "C&C-3 Alert"
            else:
                return "C&C-2 Alert"
        
        elif (ssl_alert):
            if (ip_alert):
                if (tor_alert):
                    return "C&C-4 Alert"
                else:
                    return "C&C-3 Alert"
            elif (tor_alert):
                if (ip_alert):
                    return "C&C-4 Alert"
                else:
                    return "C&C-3 Alert"
            else:
                return "C&C-2 Alert"
            
        elif (tor_alert):
            if (ip_alert):
                if (ssl_alert):
                    return "C&C-4 Alert"
                else:
                    return "C&C-3 Alert"
            elif (ssl_alert):
                if (ip_alert):
                    return "C&C-4 Alert"
                else:
                    return "C&C-3 Alert"
            else:
                return "C&C-2 Alert"
        else:
            return "C&C-1 Alert"
        
    elif (tor_alert):
        if (ip_alert):
            if (dns_alert):
                if (ssl_alert):
                    return "C&C-4 Alert"
                else:
                    return "C&C-3 Alert"
            
            elif(ssl_alert):
                if (dns_alert):
                    return "C&C-4 Alert"
                else:
                    return "C&C-3 Alert"
            else:
                return "C&C-2 Alert"
        
        elif (dns_alert):
            if (ip_alert):
                if (ssl_alert):
                    return "C&C-4 Alert"
                else:
                    return "C&C-3 Alert"
            elif (ssl_alert):
                if (ip_alert):
                    return "C&C-4 Alert"
                else:
                    return "C&C-3 Alert"
            else:
                return "C&C-2 Alert"
            
        elif (ssl_alert):
            if (ip_alert):
                if (dns_alert):
                    return "C&C-4 Alert"
                else:
                    return "C&C-3 Alert"
            elif (dns_alert):
                if (ip_alert):
                    return "C&C-4 Alert"
                else:
                    return "C&C-3 Alert"
            else:
                return "C&C-2 Alert"
        else:
            return "C&C-1 Alert"
        
    else:
        return 0
    
        