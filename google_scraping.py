import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
import time


def get_source(url):
    """Return the source code for the provided URL. 

    Args: 
        url (string): URL of the page to scrape.

    Returns:
        response (object): HTTP response object from requests_html. 
    """

    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)


def scrape_google(query):
    MAX =270 #Define the global google query page to scrape
    STEP=10  #Step
    query = urllib.parse.quote_plus(query)
    links =[]
    for i in range(1,MAX,STEP):
        response = get_source("https://www.google./search?q=" + query)
        response = get_source(url)
        links += list(response.html.absolute_links)
        time.sleep(2)
        print(i)
    google_domains = ('https://www.google.', 
                      'https://google.', 
                      'https://webcache.googleusercontent.', 
                      'http://webcache.googleusercontent.', 
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')

    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)


    return links



if __name__ == '__main__':
    #Open the file where to save the url list downloaded from google
    f = open('filenaname.txt', 'a')
    #Use the google dorks in order to increase the results
    for link in scrape_google("site:site.com filetype:pdf"):
        f.write(str(link) + "\n")
        print(link)
    f.close()
