import reflex as rx
import pymongo
from pymongo import MongoClient

from frontend.states.auth_state import AuthState

import os
import sys

absolute_path = os.path.abspath(os.path.join(sys.path[1], ".."))
relative_path = "Backend/ip.txt"
full_path = os.path.join(absolute_path, relative_path)
full_path = full_path.replace("\\", "/")

#setup
try:
    c = open(full_path,"r")
    ip = c.readline()
    c.close()
except FileNotFoundError:
    c = open(full_path,"x")
    l = input("whats the MangoDB ip? It will be saved in ip.txt")
    c.write(l)
    ip = l
    c.close()

client = MongoClient(ip, 27017)
db = client['main']
mentees = db['mentees']
mentors = db['mentors']

class UserLoginAttemptState(rx.State):

    user : str = ""

    def try_login(self):

        for mentee in mentees.find():
            for key in mentee["answers"]:
                if key == "12c982a5":
                    result = mentee["answers"][key]["textAnswers"]["answers"][0]["value"]
                    print(result)
                    print(f"user: {self.user}")
                    if result == self.user:
                        print(f"match: {result}")
                        AuthState.logged_in, AuthState.is_admin, AuthState.username = True, False, result
                        self.user = ""
                        rx.window_alert("MENTEE")
                        return rx.redirect(f"/mentee/{result}")
        
        for mentor in mentors.find():
            for key in mentor["answers"]:
                if key == "12c982a5":
                    result = mentor["answers"][key]["textAnswers"]["answers"][0]["value"]
                    print(result)
                    print(f"user: {self.user}")
                    if result == self.user:
                        print(f"match mentor: {result}")
                        AuthState.logged_in, AuthState.is_admin, AuthState.username = True, False, result
                        self.user = ""
                        rx.window_alert("MENTEE")
                        return rx.redirect(f"/mentor/{result}")
        



def login():
    login_component = rx.container(
        rx.center(
            rx.card(
                rx.vstack(
                    rx.text("Please enter your user."),
                    rx.input(placeholder="Username", on_change=UserLoginAttemptState.set_user),
                    rx.button("Submit", on_click=UserLoginAttemptState.try_login), 
                )
        )
    )
)
    return login_component


def user_login():
    UserLoginAttemptState.user = ""
    page = rx.container(
        rx.center(
            login(),
            height="100vh"
        ),
    )
    

    return page