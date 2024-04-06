import reflex as rx
from frontend.states import AuthState


def header():
    return rx.vstack(rx.flex(

        rx.button("Log Out", on_click=AuthState.logout),
        width="100%",
        height="10vh",
        align="end",
        
        
    ), rx.divider(), align="center")

@rx.page(on_load=AuthState.check_login, route="/mentee/[username]")
def mentee_dashboard():

    return rx.container(
        rx.center(
            rx.grid(
            header(),
            rx.center(
            rx.card(
            rx.heading("Mentee Dashboard"),
            rx.text(AuthState.username),),),
            height="100vh"),
            rows="2",
            columns="1"

        )
    )