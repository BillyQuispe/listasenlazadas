#!/usr/bin/env python

import sys
import requests
import json
from urllib.parse import urljoin
class nodo:
    def __init__(self, text, href):
        self.text = text
        self.href = href
        self.next = None     
flag = False
def extract_links(lmt=8):
    apikey = "YWIxZjAwZDktOTEwMS00NmNiLWFmN2ItNDdlOWRiM2IzZDEz";    global flag;
    search_term = "excited"
    r = requests.get("https://reqres.in/api/users/%s&limit=%s" % (search_term, lmt))
    if r.status_code == 200:
        top_8gifs = json.loads(r.content)
        for x in range (240):
            for x in range(len(top_8gifs['results'])):
                if flag == False:
                    head = nodo(top_8gifs['results'][x]['id'], top_8gifs['results'][x]['media'][0]['webm']['preview'])
                    flag = True;    
                    temp = head
                else:
                    temp.next = nodo(top_8gifs['results'][x]['id'], top_8gifs['results'][x]['media'][0]['webm']['preview'])
                    temp = temp.next
    return head
links = extract_links(12)
def extrae(id):
    temp = links
    t = 0
    while id>t:
        temp = temp.next
        links1 = [{"text":temp.text, "href":temp.href}]
        t=t+1
    return links1
