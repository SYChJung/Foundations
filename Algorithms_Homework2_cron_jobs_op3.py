
# coding: utf-8

# ### Option 3: The Times it is a-changing

# In[9]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


# In[10]:


response = requests.get("http://www.nytimes.com")
doc = BeautifulSoup(response.text, 'html.parser')


# In[18]:


stories = doc.find_all("article", { 'class': 'story' })
# stories


# In[ ]:


# ("h2", { 'class': 'story-heading' }) # Top left article


# In[26]:


all_stories = []

for story in stories:
    headline = story.find('h2', {'class': 'story-heading'})
#     print(headline.find('a')['href'])
#     break
    if headline:
        headline_text = headline.text.strip()
        
        if headline.find('a'):
            headline_link = headline.find('a')['href']
        else:
            headline_link = None
        
        this_story = {
            'headline': headline_text,
            'link': headline_link,
        }
#         byline = story.find('p', {'class': 'byline'})
#         # Not all of them have a byline
#         if byline:
#             byline_text = byline.text.strip()
#             this_story['byline'] = byline_text
        all_stories.append(this_story)

all_stories


# In[28]:


top_left_story = all_stories[0]
top_left_story


# In[29]:


top_left_story['link']


# In[38]:


from twilio.rest import Client

account_sid = "AC328e01be8d8cfeb4d17e91ae8a616e58"
auth_token = "1348c1d164c17e6391c68a755ed54593"
client = Client(account_sid, auth_token)
client.messages.create(

#   to="+16518675309",
  to="+19178252615",
  from_="+12012926019",

  body = top_left_story["headline"],
  media_url = top_left_story['link']
)

