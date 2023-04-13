#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("Screentime-App-Details.csv")
print(data.head())


# In[2]:


#checking if there is any null values
data.isnull().sum()


# In[3]:


print(data.describe())


# In[4]:


#checking amount of usage of the apps
figure = px.bar(data_frame=data, 
                x = "Date", 
                y = "Usage", 
                color="App", 
                title="Usage")
figure.show()


# In[5]:


#Now let’s have a look at the number of notifications from the apps:
figure = px.bar(data_frame=data, 
                x = "Date", 
                y = "Notifications", 
                color="App", 
                title="Notifications")
figure.show()


# In[6]:


#Now let’s have a look at the number of times the apps opened:
figure = px.bar(data_frame=data, 
                x = "Date", 
                y = "Times opened", 
                color="App",
                title="Times Opened")
figure.show()


# In[7]:


#let’s have a look at the relationship between the number of notifications and the amount of usage:
figure = px.scatter(data_frame = data, 
                    x="Notifications",
                    y="Usage", 
                    size="Notifications", 
                    trendline="ols", 
                    title = "Relationship Between Number of Notifications and Usage")
figure.show()


# In[8]:


#So this is how we can analyze the screen time of a user using the Python programming language. Screen Time Analysis is the task of analyzing and creating a report on which applications and websites are used by the user for how much time.

