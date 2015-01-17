#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

# Define global variables and functions

def request_page(url):
    try:
        r = requests.get(url)
    except requests.exceptions.MissingSchema as e:
        return
    except requests.exceptions.InvalidSchema as e:
        return
    response = r.text
    html = BeautifulSoup(response)
    return html

def get_domain(url):
    domain = url.split('/')
    print "The domain: ", domain[2]
    return domain[2]

# Foxbat class

class Foxbat:
    def __init__(self, entry):
        self.entry = entry
        self.crawled_urls = []
        self.loaded_urls = []
        self.html = BeautifulSoup("<p>response</p>")
        self.current_url = ""
        self.current_domain = ""

        # Temporary lists for removing items from the main list variables
        self.crawled_urls_temp = []
        self.loaded_urls_temp = []

    def takeoff(self):
        self.current_url = self.entry
        self.current_domain = get_domain(self.entry)
        self.html = request_page(self.entry)
        for link in self.html.find_all('a'):
            if (link.get("href") not in self.loaded_urls):
                self.loaded_urls.append(link.get("href"))
            print "Takeoff: ", link.get("href"), '\n'

    def get_page(self):
        if (self.loaded_urls[1] == None):
            self.loaded_urls = self.loaded_urls[1:]
            return
        '''
        if (self.loaded_urls[1].startswith('#') == True):
            temp_str = self.current_url +""+ self.loaded_urls[1]
            self.loaded_urls[1] = temp_str
        if ("http://" or "https://" not in self.loaded_urls[1]):
            self.current_domain = get_domain(self.loaded_urls[1])
            temp_str = self.current_domain +""+ self.loaded_urls[1]
        '''
        self.html = request_page(self.loaded_urls[1])
        self.crawled_urls.append(self.loaded_urls[1])
        try:
            for link in self.html.find_all('a'):
                if (link.get("href") not in self.loaded_urls and link.get("href") not in self.crawled_urls):
                    href = link.get("href")

                    if (href.startswith('#') == True):
                        temp_str = self.current_url +""+ href
                        href = temp_str
                    if (href.startswith('/') == True):
                        self.current_domain = get_domain(self.loaded_urls[1])
                        temp_str = self.current_domain +""+ href
                        href = temp_str

                    #if (link.get("href").startswith('#')):
                        #href = link.get("href")
                    #    href = self.current_url +""+ link.get("href")
                    self.loaded_urls.append(href)
                    print "Get page: ", href, '\n'
        except AttributeError:
            self.loaded_urls = self.loaded_urls[1:]
            return

        # Remove the first item of the loaded url list
        self.loaded_urls = self.loaded_urls[1:]

    def crawl(self):
        try:
            for item in self.html.find_all('p'):
                print item.get_text()
        except AttributeError:
            return

        # Debugging - Don't delete commented code below here!
        print "The current domain is:", self.current_domain
        #for item in self.loaded_urls:
        #    print "Loaded URLs: ", item
        for item in self.crawled_urls:
            print "Crawled URLs: ", item
