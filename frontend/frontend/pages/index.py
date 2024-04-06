

import reflex as rx
from frontend.states import AuthState
from frontend.components import footer


def index() -> rx.Component:

    page = rx.center(
        rx.vstack(
            rx.heading("Marianopolis Mentor Portal", size="9"),
            rx.text("Welcome to the Marionopolis Mentor Portal! If you want to apply, click ", rx.link("here.", href="https://forms.gle/KG6eqeqddWMHBZ279"), size="4"),
            rx.hstack(
                rx.button("Applicant Login", size="4", on_click=rx.redirect("/user-login")),
                rx.button("Admin Login", size="4", on_click=rx.redirect("/admin-login")),
            ),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )

    return rx.container(
        page,
        
    )