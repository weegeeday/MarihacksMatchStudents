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

# mentorProgram = ""
# mentorGender = 0

# menteeProgram = ""
# mentorGender = 0

# Call MatchProgram function
def MatchProgram(mentor):
    candidates = []
    for answer in mentor["answers"]:
        if answer == "36b8a936":
            mentorProgram = mentor["answers"][answer]["textAnswers"]["answers"][0]["value"]
            for mentee in mentees.find():
                for a in mentee["answers"]:
                    if a == "36b8a936":
                        if mentee["answers"][a]["textAnswers"]["answers"][0]["value"] == mentorProgram:
                            for key in mentee["answers"]:
                                if key == "12c982a5":
                                    candidates.append(mentee)
                                    
    # print()
    return MatchGender(mentor, candidates)

def MatchGender(mentor, candidates):
    c = []
    for answer in mentor["answers"]:
        if answer == "627fa5ae":
            mentorGender = mentor["answers"][answer]["textAnswers"]["answers"][0]["value"]
            for mentee in candidates:
                for a in mentee["answers"]:
                    if a == "627fa5ae":
                        if mentee["answers"][a]["textAnswers"]["answers"][0]["value"] == mentorGender:
                            for key in mentee["answers"]:
                                if key == "12c982a5":
                                    c.append(mentee["answers"][key]["textAnswers"]["answers"][0]["value"])
    if c == []:
        for key in candidates:
            if key == "12c982a5":
                c.append(mentee["answers"][key]["textAnswers"]["answers"][0]["value"])
        
    return c[0]

# def Match(mentor):

    

            
for m in mentors.find():
    print(MatchProgram(m))