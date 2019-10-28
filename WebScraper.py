
import requests
from bs4 import BeautifulSoup

def CreateBlacklists():
    page = requests.get('https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=1.1.1.1')
    # Create a BeautifulSoup object
    soup = BeautifulSoup(page.text, 'html.parser')
    file1 = open("t_tor-server.txt","w")
    file1.writelines(soup) 
    file1.close()
    
    page = requests.get('https://sslbl.abuse.ch/blacklist/sslblacklist.csv')
    # Create a BeautifulSoup object
    soup = BeautifulSoup(page.text, 'html.parser')
    file1 = open("ssl-blacklist.csv","w")
    file1.writelines(soup) 
    file1.close()
    
    page = requests.get('https://raw.githubusercontent.com/stamparm/ipsum/master/levels/8.txt')
    # Create a BeautifulSoup object
    soup = BeautifulSoup(page.text, 'html.parser')
    file1 = open("t_ip-blacklist.txt","w")
    file1.writelines(soup) 
    file1.close()
    

    
    
#CreateBlacklists()
    



