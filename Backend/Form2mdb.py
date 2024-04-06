import FormsAPI
import pymongo
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
failed = db['failed']
class Form2mdb:
    

    @staticmethod
    def InsertData(fid):
        try:
            data = FormsAPI.FormsResp.GetResp(fid)
            #print(data)
            #how can we get a python dict into MDB?
            resp = data["responses"]
            mentees.delete_many({})
            mentors.delete_many({})
            for x in resp:
                ans = x["answers"]["52018967"]["textAnswers"]["answers"][0]["value"]
                if ans == "Mentee":
                    mentees.insert_one(x)
                if ans == "Mentor":
                    mentors.insert_one(x)
            return True
        except any:
            return False