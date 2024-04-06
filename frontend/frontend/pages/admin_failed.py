
import reflex as rx

def admin_failed():
    page = rx.container(
        rx.center(
            rx.vstack(
                rx.spacer(direction="column"),
                rx.text("Access denied. Please log in as administrator."),
                rx.spacer(direction="column"),
                rx.button("Return to home.", on_click=rx.redirect("/"))
            ),
            align="center", height="40vh"
        )
    )

    return page