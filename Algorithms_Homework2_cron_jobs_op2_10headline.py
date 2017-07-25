
# coding: utf-8

# ### Option 2: News headlines


import requests
from bs4 import BeautifulSoup
import pandas as pd
import time



response = requests.get("https://www.washingtonpost.com/")
doc = BeautifulSoup(response.text, 'html.parser')

stories = doc.find_all("div", { 'moat-id': 'homepage/story' })
stories


all_headlines = []
for story in stories[:10]:
    headline = story.find('a')
    if headline:
        headline_text = headline.text.strip()
        this_story = { 'headline': headline_text }
        
        link   = story.find('a')['href']
        if link:
            link_text   = link
            this_story.update({
                'link' : link_text
            })

        byline = story.find('div', {'class': 'blurb'}) 


        if byline:
            byline_text = byline.text.strip()
            this_story.update({
                'byline' : byline_text
            })

        all_headlines.append(this_story)
all_headlines






