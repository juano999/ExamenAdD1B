#!/usr/bin/env python
# coding: utf-8

# In[9]:


import requests
import json
from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
import pandas as pd
import bson
from bson.raw_bson import RawBSONDocument
from bs4 import BeautifulSoup

db_client = MongoClient()
my_db = db_client.cursos
my_posts = my_db.posts
    
def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)


def find_1st(string, substring):
    return string.find(substring, string.find(substring))


# In[25]:


CLIENT = MongoClient('mongodb://localhost:27017/')

try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)


response = requests.get("https://www.elcomercio.com/tag/juegos-olimpicos/")
soup = BeautifulSoup(response.content, "lxml")

Course=[]
Provider=[]
Duration=[]
Start_Date=[]
Offered_By=[]
No_Of_Reviews=[]
Rating=[]
title=[]

post_all = soup.find_all("p")

extracted = []

for element in post_all:
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')+1])
    limpio1=str()
    #print (limpio)
    title.append(limpio.strip())

df=pd.DataFrame(title)
salidaJson = df.to_json('Descripcion.json')



db = CLIENT["JuegosOlimpicosMongo"]
Collection = db["elcomercio"]

with open('Descripcion.json') as file:
    dato_json = json.load(file)

if isinstance(dato_json, list):
    
    
    Collection.insert_many(dato_json)
    print("se inserto muchos elementos correctamente")

else:
    Collection.insert_one(dato_json)
    print("se inserto un elemento correctamente")

