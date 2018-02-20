from bs4 import BeautifulSoup
import requests
import time
import urllib

def continue_crawl(search_history, target_url, max_steps=25):
    if search_history[-1] == target_url:
        print("We've found the target article!")
        return False
    elif len(search_history) > max_steps:
        print("The search has gone on suspiciously long, aborting search!")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("We've arrived at an article we've already seen, aborting search!")
        return False
    else:
        return True
def find_first_link(url):
    # get the HTML from "url", use the requests library
    response=requests.get(url)
    html=response.text
    # feed the HTML into Beautiful Soup
    soup=BeautifulSoup(html,"html.parser")
    # find the first link in the article
    first_relative_link=None
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            first_relative_link = element.find("a", recursive=False).get('href')
            break
    if not first_relative_link:
        return 
    else:
        first_relative_link = urllib.parse.urljoin('https://en.wikipedia.org/', first_relative_link)      
        return first_relative_link    
    # return the first link as a string, or return None if there is no link        
search_history=['https://en.wikipedia.org/wiki/Jackass_Flat,_Victoria']    
target_url="https://en.wikipedia.org/wiki/Philosophy"    
while continue_crawl(search_history,target_url):
    # download html of last article in article_chain
    link=find_first_link(search_history[-1])
    print(link)
    search_history.append(link)
    # find the first link in that html
    # add the first link to article_chain
    # delay for about two seconds
    time.sleep(2)
print (search_history)    