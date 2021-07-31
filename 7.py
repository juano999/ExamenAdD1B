#!/usr/bin/env python
# coding: utf-8

# In[8]:


import couchdb
import json
from argparse import ArgumentParser
import requests
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb
import pandas as pd


URL = 'http://admin:admin@localhost:5984'
couch = couchdb.Server(URL)
try:
    response = requests.get(URL)
    if response.status_code == 200:
        print('CouchDB connection: Success')
    if response.status_code == 401:
        print('CouchDB connection: failed', response.json())
except requests.ConnectionError as e:
    raise e

CLIENT = MongoClient('mongodb://localhost:27017/')

try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)
    
db = couch['juegosolimpicos'] # existing
Mongodb = CLIENT["JuegosOlimpicosMongo"]
Collection = Mongodb["elcomercio"]


'''
for id in db:
    df=pd.DataFrame(db[id])
    salidaJson = df.to_json('doc.json')
    with open('doc.json') as file:
        dato_json = json.load(file)
            
    Collection.insert_one(dato_json)
    print("se guardó")
'''   
for ids in db.view('_all_docs'):
    try:
        id=ids['id']
        data=db[id]
        
        CLIENT.JuegosOlimpicosMongo.elcomercio.insert_one(data)
    except Exception as e:
        raise e


# In[4]:


db["1421242829435723777"]


# In[ ]:




