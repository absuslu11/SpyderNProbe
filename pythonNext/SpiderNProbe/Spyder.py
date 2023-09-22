from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from urllib import *

visitedURLS = set()

def spyder(url, keyword):

    try:
        response = requests.get(url)
    except:
        print(f"request failed {url}")
        return
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        aTag = soup.find_all("a")
        urls = []

        for tag in aTag:
            href = tag.get("href")
            if href is not None and href != "":
                urls.append(href)
        #print(urls)

        for url2 in urls:
            if url2 not in visitedURLS:
                visitedURLS.add(url2)
                urlJoin =urljoin(url,url2)
                if keyword in urlJoin:
                    print(urlJoin)
                    spyder(urlJoin, keyword)
            else:
                pass











url = input("enter the URL you want scraped: ")
keyword = input("Enter the keyword to search for in the URL provided: ")
spyder(url, keyword)







