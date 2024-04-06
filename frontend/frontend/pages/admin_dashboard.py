import reflex as rx
from frontend.states import AuthState

import pymongo
from pymongo import MongoClient
#setup


client = MongoClient("10.2.25.82", 27017)
db = client['main']
mentees = db['mentees']
mentors = db['mentors']


def header():
    return rx.center(
        rx.flex(

            rx.button("Log Out", on_click=AuthState.logout),
            rx.spacer(),
            rx.link("Dashboard", href="/admin-dashboard"),
            width="100%",
            # height="10vh",
            align="center",
            direction="row",
            padding="5"
        ), 
        width="100%",
        height="10vh",
        direction="column",
        
    )




@rx.page(on_load=AuthState.check_admin_login)
def admin_dashboard():

    return rx.container(
        rx.center(
            rx.grid(
                header(),
                rx.vstack(
                    rx.heading("Admin Dashboard"), 
                    rx.hstack(
                        rx.button("Make Matches", on_click=rx.window_alert("Unfortunately, we ran out of time."))
                    ),
                    height="50vh",
                    align="center",
                ),
                rows="2",
                columns="1"
            )
        )
    )