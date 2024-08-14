import requests
from bs4 import BeautifulSoup
import pywebcopy

#url = 'https://www.geeksforgeeks.org/'
#url = 'https://sam.gov/search/?index=_all&page=1&pageSize=25&sort=-modifiedDate&sfm%5BsimpleSearch%5D%5BkeywordRadio%5D=ALL&sfm%5BsimpleSearch%5D%5BkeywordTags%5D%5B0%5D%5Bkey%5D=forestry&sfm%5BsimpleSearch%5D%5BkeywordTags%5D%5B0%5D%5Bvalue%5D=forestry&sfm%5Bstatus%5D%5Bis_active%5D=true'
#url = "https://www.youtube.com/"
url = 'https://www.google.com?'

reqs = requests.get(url)
#print(f"{reqs}")
soup = BeautifulSoup(reqs.text, 'html.parser')
#print(f"{soup}")

urls = []

h = open("trackData.txt", 'a')

#for link in soup.find_all('a'):
#    h.write(str(link))
#    print(link.get('href'))


def CopyHTML(urls):
    #urls = 'https://www.geeksforgeeks.org/'
    grab = requests.get(urls)
    soup = BeautifulSoup(grab.text, 'html.parser')
    
    # opening a file in write mode
    f = open("test1.txt", "a")
    g = open("trackData.txt", "a")
    # traverse paragraphs from soup
    for link in soup.find_all("a"):
        data = link.get('href')
        #g.write(f"\n{link},{grab},{soup}")
        g.write(data)
        g.write("\n")
    #g.write(f"\n{link},{data},{grab},{soup}")
    
    f.close()
    g.close()

CopyHTML('https://sam.gov/search/?index=_all&page=1&pageSize=25&sort=-modifiedDate&sfm%5BsimpleSearch%5D%5BkeywordRadio%5D=ALL&sfm%5BsimpleSearch%5D%5BkeywordTags%5D%5B0%5D%5Bkey%5D=forestry&sfm%5BsimpleSearch%5D%5BkeywordTags%5D%5B0%5D%5Bvalue%5D=forestry&sfm%5Bstatus%5D%5Bis_active%5D=true')