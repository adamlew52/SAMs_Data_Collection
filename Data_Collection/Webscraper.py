from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urlparse, unquote
import requests
import re
import time


response = urlopen('https://sam.gov/opp/92723584c1884ce2a01a81835d42f5f3/view')
status_code = response.getcode(); assert status_code == 200

soup = BeautifulSoup(response.read(), 'html.parser')


def WebpageNavigation(rootURL):
    print("Navigating")

def Scraper():
    print("scraping")

# Handle URL parsing and encoding


class ScrapeFunctions:
    def Find():
        title = soup.find('title').text
        links = [a.get('href') for a in soup.find_all('a', href=True)]
        url_parts = urlparse('https://sam.gov/opp/92723584c1884ce2a01a81835d42f5f3/view')
        decoded_query = unquote(url_parts.query)
        print(f'title: {title}')
        print(f'links: {links}')
        return title, links, decoded_query
        
    # Store scraped data
    def StoreData():
        title = ScrapeFunctions.Find()[0]
        links = ScrapeFunctions.Find()[1]
        decoded_query = ScrapeFunctions.Find()[2]


        with open('/Users/adam/Documents/SAMS/Data_Collection/scraped_data.csv', 'a') as f:
            f.write(f'Title: {title}\nLinks: {links}\nQuery: {decoded_query}')

    def ContractContaining(keyword):
        title = soup.find('title').texts
        links = [a.get('href') for a in soup.find_all('a', href=True)]
        for link in links:
            if link.contains(keyword):
                with open(f'Contracts_for_Test.csv', 'w+') as f:
                    f.write(f'Title: {title}\nLinks: {links}\nQuery: {ScrapeFunctions.decoded_query}')

    def FindContracts(keywordAddress):
        with open(keywordAddress, 'r') as keywordList:
            keywordListArray = keywordList.readlines()
            for keyword in keywordListArray:
                #print(keyword)
                ScrapeFunctions.ContractContaining(keyword)

class Stolen:
    # Replace with the webpage's URL
    url = 'https://sam.gov/search/?index=_all&page=1&pageSize=25&sort=-modifiedDate&sfm%5BsimpleSearch%5D%5BkeywordRadio%5D=ALL&sfm%5BsimpleSearch%5D%5BkeywordTags%5D%5B0%5D%5Bkey%5D=forestry&sfm%5BsimpleSearch%5D%5BkeywordTags%5D%5B0%5D%5Bvalue%5D=forestry&sfm%5Bstatus%5D%5Bis_active%5D=true'

    # Fetch the webpage's HTML
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all links on the webpage
    links = soup.find_all('a')
    print(links)

    # Extract link URLs
    link_urls = [link.get('href') for link in links]

    print(link_urls)  # Print the list of extracted link URLs

class OtherStolen:
    source_code = requests.get('https://sam.gov/opp/92723584c1884ce2a01a81835d42f5f3/view')
    soup = BeautifulSoup(source_code.content, 'lxml')
    data = []
    links = []


    def remove_duplicates(l): # remove duplicates and unURL string
        for item in l:
            match = re.search("(?P<url>https?://[^\s]+)", item)
            if match is not None:
                links.append((match.group("url")))

    for link in soup.find_all('a', href=True):
        data.append(str(link.get('href')))
    flag = True
    remove_duplicates(data)
    while flag:
        try:
            for link in links:
                for j in soup.find_all('a', href=True):
                    temp = []
                    source_code = requests.get(link)
                    soup = BeautifulSoup(source_code.content, 'lxml')
                    temp.append(str(j.get('href')))
                    remove_duplicates(temp)

                    if len(links) > 162: # set limitation to number of URLs
                        break
                if len(links) > 162:
                    break
            if len(links) > 162:
                break
        except Exception as e:
            print(e)
            if len(links) > 162:
                break

    for url in links:
        print(url)

#ScrapeFunctions.FindContracts('/Users/adam/Documents/SAMS/Data_Collection/Keyword_List.txt')
#ScrapeFunctions.StoreData()
    
OtherStolen