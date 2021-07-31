#!/usr/bin/env python
# coding: utf-8

# In[7]:


from facebook_scraper import get_posts
import couchdb
import json
import time
import pandas as pd
from pymongo import MongoClient


# In[8]:


CLIENT = MongoClient('mongodb://localhost:27017/')

try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)

db = CLIENT["JuegosOlimpicosMongo"]
Collection = db["elcomercio"]
    
i=1
for post in get_posts('JuegosOlimpicos', pages=20, extra_info=True, credentials=('carl-bo@hotmail.com', 'family1011')):
    print(i)
    i=i+1
    time.sleep(5)
    
    id=post['post_id']
    doc={}
     
    doc['id']=id
    
    mydate=post['time']
    
    try:
        doc['texto']=post['text']
        doc['date']=mydate.timestamp()
        doc['likes']=post['likes']
        doc['comments']=post['comments']
        doc['shares']=post['shares']
        try:
            doc['reactions']=post['reactions']
        except:
            doc['reactions']={}

        doc['post_url']=post['post_url']
        df=pd.DataFrame(doc)
        salidaJson = df.to_json('doc.json')
        with open('doc.json') as file:
            dato_json = json.load(file)
            
        Collection.insert_one(dato_json)

    
        print("guardado exitosamente")

    except Exception as e:    
        print("no se pudo grabar:" + str(e))


# In[4]:





# In[ ]:




