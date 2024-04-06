import FormsAPI
import pymongo
import json
from pymongo import MongoClient
#setup
try:
    c = open("./Backend/ip.txt","r")
    ip = c.readline()
    c.close()
except FileNotFoundError:
    c = open("./Backend/ip.txt","x")
    l = input("whats the MangoDB ip? It will be saved in ip.txt")
    c.write(l)
    ip = l
    c.close()

client = MongoClient(ip, 27017)
db = client['main']
mentees = db['mentees']
mentors = db['mentors']
class Form2mdb:
    

    @staticmethod
    def FormGetNparse(fid):
        data = FormsAPI.FormsResp.GetResp(fid)
        print(data)
        #how can we get a python dict into MDB?
        resp = data["responses"]
        for x in resp:
            if
            mentors.insert_one(resp)