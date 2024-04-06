import reflex as rx
from frontend.states import AuthState
from frontend import Sync



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


def do_match():

    Sync.Sync("1sMoOAui_9mI1t9Sny4T18RAlgQHNqnN3w5DEPAwR3p8")


@rx.page(on_load=AuthState.check_admin_login)
def admin_dashboard():

    return rx.container(
        rx.center(
            rx.grid(
                header(),
                rx.vstack(
                    rx.heading("Admin Dashboard"), 
                    rx.hstack(
                        rx.button("Make Matches")
                    ),
                    height="50vh",
                    align="center",
                ),
                rows="2",
                columns="1"
            )
        )
    )