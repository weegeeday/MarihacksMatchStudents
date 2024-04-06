import FormsAPI
import pymongo
import json
from pymongo import MongoClient
#setup
client = MongoClient('10.2.25.82', 27017)
db = client['main']
mentees = db['mentees']
mentors = db['mentors']

data = FormsAPI.FormsResp.GetResp()
