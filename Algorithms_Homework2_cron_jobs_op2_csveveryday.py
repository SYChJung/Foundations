
# coding: utf-8

# ### Option 2: News headlines
# 

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


# In[2]:


response = requests.get("https://www.washingtonpost.com/")
doc = BeautifulSoup(response.text, 'html.parser')


# In[3]:


doc


# In[4]:


stories = doc.find_all("div", { 'moat-id': 'homepage/story' })
stories


# In[5]:


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


# In[ ]:


stories_df = pd.DataFrame(all_headlines)
stories_df.to_csv("wp-data.csv")


# In[ ]:


datestring = time.strftime("%Y-%m-%d-%H-%M")
filename = "wp-data-" + datestring + ".csv"
stories_df.to_csv(filename, index=False)


# In[ ]:




