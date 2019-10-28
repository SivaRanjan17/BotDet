import csv
import requests
from bs4 import BeautifulSoup


def scrape_data(url):

    source = requests.get("https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=1.1.1.1").text
    soup = BeautifulSoup(source, 'lxml')

    table = soup.find('pre')

    print (table)
"""
    with open('output.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        for row in rows[1:]:
            data = [th.text.rstrip() for th in row.find_all('td')]
            writer.writerow(data)
"""

if __name__=="__main__":
    url = "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=1.1.1.1"
    scrape_data(url)