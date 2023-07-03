#!/usr/bin/env python

import sys
import requests
import json
from urllib.parse import urljoin

class Nodo:
    def _init_(self, text, href):
        self.text = text
        self.href = href
        self.next = None     

flag = False

def extract_links(lmt=8):
    api_key = "YOUR_GIPHY_API_KEY"
    search_term = "excited"
    url = f"https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={search_term}&limit={lmt}"

    r = requests.get(url)

    if r.status_code == 200:
        top_gifs = json.loads(r.content)
        head = None
        temp = None
        for x in range(len(top_gifs['data'])):
            if flag == False:
                head = Nodo(top_gifs['data'][x]['id'], top_gifs['data'][x]['images']['preview']['webp'])
                flag = True
                temp = head
            else:
                temp.next = Nodo(top_gifs['data'][x]['id'], top_gifs['data'][x]['images']['preview']['webp'])
                temp = temp.next
    return head

links = extract_links(50)

def extrae(id):
    temp = links
    t = 0
    while id > t:
        temp = temp.next
        links1 = [{"text": temp.text, "href": temp.href}]
        t += 1
    return links1