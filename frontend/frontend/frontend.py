"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config
from frontend.pages import *


import reflex as rx

style = {
    
    "font_family" : "Roboto",


    rx.heading : {
        "font_family" : "Roboto"
    }
}





app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap"],
    style=style,
    theme=rx.theme(
        appearance="dark",  # Set the appearance to 'dark' for dark mode
        has_background=True,
        radius="large",
        accent_color="teal",
    ),
)
app.add_page(index)
app.add_page(admin_failed, route="/admin-failed")
app.add_page(admin_login, route="/admin-login")
app.add_page(admin_dashboard, route="/admin")
app.add_page(user_login, route="/user-login")
app.add_page(mentor_dashboard, route="/mentor/[username]")
app.add_page(mentee_dashboard, route="/mentee/[username]")