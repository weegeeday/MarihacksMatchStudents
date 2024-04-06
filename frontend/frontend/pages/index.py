

import reflex as rx

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Marianopolis Mentor Portal", size="9"),
            rx.text("Welcome to the Marionopolis Mentor Portal! If you want to apply to the program, "),
            rx.hstack(
                rx.button("Applicant Login", size="4"),
                rx.button("Admin Login", size="4", on_click=rx.redirect("/admin-login")),
            ),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )