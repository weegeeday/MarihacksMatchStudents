import reflex as rx
from frontend.states import AuthState


def header():
    return rx.vstack(rx.flex(

        rx.button("Log Out", on_click=AuthState.logout),
        width="100%",
        height="10vh",
        align="end",
        
        
    ), rx.divider(), align="center")

@rx.page(on_load=AuthState.check_login, route="/mentor/[username]")
def mentor_dashboard():

    return rx.container(
        rx.center(
            rx.grid(
            header(),
            rx.heading("Mentor Dashboard"),
            rx.text(AuthState.username),
            height="100vh"),
            rows="2",
            columns="1"

        )
    )