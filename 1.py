#!/usr/bin/env python
# coding: utf-8

# In[1]:


import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


# In[2]:





# In[2]:


###API ########################
ckey = "SZ4lYd7M5Unbl8i6HxuCAcHkk"
csecret = "GNw2axdBaXr69HC0nAUO6OIu8eDFSIjR8NRkAk6wfWEp9YEVdd"
atoken = "1631284146-RVFxn5bXKbv5hzaLSLnYH0FTJC58qn7Bu9nRFEY"
asecret = "3fEyfLMJWWjja8beca5aZO1wHrXCVIbVwCaB4Irisr5SG"
#####################################


# In[6]:


class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED")
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://admin:admin@localhost:5984/')  #('http://localhost:5984/')
try:
    db = server.create('juegosolimpicos')
except:
    db = server['juegosolimpicos']
    
'''===============LOCATIONS=============='''    

twitterStream.filter(locations=[140.377712,36.319243,140.591259,36.462955])  



# In[ ]:




