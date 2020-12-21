#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from matplotlib import pyplot as Plt
import seaborn as sns
import numpy as np


# In[2]:


ipl=pd.read_csv(r'C:\Users\ANUJ KUMAR PANDEY\Desktop\matches.csv')


# In[3]:


ipl.head()


# In[4]:


ipl.shape


# In[5]:


ipl['player_of_match'].value_counts()


# In[6]:


ipl['player_of_match'].value_counts()[0:10]


# In[7]:


ipl['player_of_match'].value_counts()[0:5]


# In[8]:


list(ipl['player_of_match'].value_counts()[0:5].keys())


# In[9]:


set(ipl['player_of_match'].value_counts()[0:5].keys())


# In[10]:


Plt.figure(figsize=(8,5))
Plt.bar(list(ipl['player_of_match'].value_counts()[0:5].keys()),list(ipl['player_of_match'].value_counts()[0:5]))
Plt.show()


# In[11]:


#finding the frequency of result column
ipl['result'].value_counts()


# In[12]:


# here i am finding number of toss wins wrt to each team
ipl['toss_winner'].value_counts()


# In[13]:


#i am trying to extract the record where a team wins first while bated first
batting_first=ipl[ipl['win_by_runs']!=0]


# In[14]:


#looking at the head
batting_first.head()


# In[15]:


Plt.figure(figsize=(7,7))
Plt.hist(batting_first['win_by_runs'])
Plt.title("Distribution of Runs")
Plt.xlabel("runs")
Plt.show()


# In[16]:


#Here I am making a bar plot for top 3 teams with most wins after batting first
Plt.figure(figsize=(7,7))
Plt.bar(list(batting_first['winner'].value_counts()[0:3].keys()),(batting_first['winner'].value_counts()[0:3]),color=['#005fa2','#f9cd05','#ed1b24'])
Plt.show()


# In[17]:


#first bat & winner
batting_first['winner'].value_counts()


# In[18]:


#Here I am making a bar plot for top 3 teams with most wins after batting first
Plt.figure(figsize=(7,7))
Plt.pie(list(batting_first['winner'].value_counts()),labels=list(batting_first['winner'].value_counts().keys()),autopct="%0.1f%%")
Plt.show()


# In[19]:


#when a team has batted second and has won when they choose to bat first
batting_second=ipl[ipl['win_by_wickets']!=0]


# In[20]:


#Looking at the head
batting_second.head()


# In[21]:


#making a histrogram for frequency of wins  with respect to number of wickets
Plt.figure(figsize=(7,7))
Plt.hist(batting_second['win_by_wickets'],bins=30,color=['#808100'])
Plt.show()


# In[22]:


#finding the number of teams who batted second and wins
batting_second['winner'].value_counts()


# In[23]:


#making the plot of above
#Here I am making a bar plot for top 3 teams with most wins after batting second
Plt.figure(figsize=(7,7))
Plt.bar(list(batting_second['winner'].value_counts()[0:3].keys()),(batting_second['winner'].value_counts()[0:3]),color=['#b3a123','#004ba0','#E63329'])
Plt.show()


# In[24]:


#Here I am making a bar plot for top 3 teams with most wins after batting second
Plt.figure(figsize=(7,7))
Plt.pie(list(batting_second['winner'].value_counts()),labels=list(batting_second['winner'].value_counts().keys()),autopct="%0.1f%%")
Plt.show()


# In[25]:


#the number of matches played each seasons
ipl['season'].value_counts()


# In[26]:


#making a histrogram for frequency of wins  with respect to number of wickets
Plt.figure(figsize=(7,7))
Plt.hist(batting_second['win_by_wickets'],bins=3)
Plt.show()


# In[27]:


#finding the frequency of number of wins w.r.t each time after batting second
batting_second['winner'].value_counts()


# In[28]:


#number of matches played at diff cities
ipl['city'].value_counts()


# In[29]:


#finding the number of times when a team batted first and wins the match
np.sum(ipl['toss_winner']==ipl['winner'])


# In[30]:


#finding percentage of winning(above)
325/636


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




