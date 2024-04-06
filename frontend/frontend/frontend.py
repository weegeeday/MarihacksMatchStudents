"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config
from frontend.pages import *


import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"





app = rx.App()
app.add_page(index)
app.add_page(admin_failed, route="/admin-failed")
app.add_page(admin_login, route="/admin-login")
app.add_page(admin_dashboard, route="/admin")
app.add_page(mentor_dashboard, route="/mentor")
app.add_page(mentee_dashboard, route="/mentee")