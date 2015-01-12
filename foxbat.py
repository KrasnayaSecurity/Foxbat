#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

# Define global variables and functions

def request_page(url):
    r = requests.get(url)
    response = r.text
    html = BeautifulSoup(response)
    return html

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
        self.html = request_page(self.entry)
        for link in self.html.find_all('a'):
            self.loaded_urls.append(link.get("href"))
            print "Takeoff: ", link.get("href"), '\n'

    def get_page(self):
        #print "Get page:", self.loaded_urls[1] # Lists start at 1? -.-
        #for i in self.loaded_urls:
        #    print i
        if (self.loaded_urls[1].startswith('#') == True):
            temp_str = self.current_url +""+ self.loaded_urls[1]
            self.loaded_urls[1] = temp_str
        html = request_page(self.loaded_urls[1])
        for link in html.find_all('a'):
            self.loaded_urls.append(link.get("href"))
            print "Get page: ", link.get("href"), '\n'

        # Remove the first item of the loaded url list
        i = 1
        while (i < len(self.loaded_urls)):
            self.loaded_urls_temp.append(self.loaded_urls[i])
            i = i+1
        self.loaded_urls = self.loaded_urls_temp

    def crawl(self):
        for item in self.html.find_all('p'):
            print item.get_text()
