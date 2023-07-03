#!/usr/bin/env python

import sys
import requests
import json

class Nodo:
    def _init_(self, text, href):
        self.text = text
        self.href = href
        self.next = None     

def extract_links(lmt=8):
    apikey = "YWIxZjAwZDktOTEwMS00NmNiLWFmN2ItNDdlOWRiM2IzZDEz"
    flag = False
    search_term = "excited"
    r = requests.get("https://reqres.in/api/users?%s&limit=%s" % (search_term, lmt))
    if r.status_code == 200:
        top_8gifs = json.loads(r.content)
        head = None
        temp = None
        for x in range(len(top_8gifs['data'])):
            if flag == False:
                head = Nodo(top_8gifs['data'][x]['id'], top_8gifs['data'][x]['avatar'])
                flag = True
                temp = head
            else:
                temp.next = Nodo(top_8gifs['data'][x]['id'], top_8gifs['data'][x]['avatar'])
                temp = temp.next
    return head

links = extract_links(12)

def extrae(id):
    temp = links
    t = 0
    while id > t:
        temp = temp.next
        links1 = [{"text": temp.text, "href": temp.href}]
        t += 1
    return links1