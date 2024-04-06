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
print(mentors.find_one({"responseId": "ACYDBNh9kG0Jb8al4hhHDSb-lDlH9hwX_HEq2yxvUB1XIztpRdYU8FOgjDwzRCyrcbUOZoM"}))
class Form2mdb:
    

    @staticmethod
    def InsertData(fid):
        data = FormsAPI.FormsResp.GetResp(fid)
        #print(data)
        #how can we get a python dict into MDB?
        resp = data["responses"]
        for x in resp:
            #if mentors
            mentors.insert_one(x)