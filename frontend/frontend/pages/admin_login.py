import reflex as rx
from frontend.state import State

PASSWORD = "M4r14n0p0l1S"

class AuthState(rx.State):

    password: str = ""

    def login(self):
        if self.password == PASSWORD:
            State.logged_in, State.is_admin = True, True
            self.password = ""
            return rx.redirect("/")
        else:
            return rx.window_alert("Invalid Password")
        

def login():
    login_component = rx.container(
        rx.center(
            rx.card(
                rx.vstack(
                    rx.text("Please enter admin password."),
                    rx.input(placeholder="Password", type="password", on_change=AuthState.set_password),
                    rx.button("Submit", on_click=AuthState.login), 
                )
        )
    )
)
    return login_component



def admin_login():
    AuthState.password = ""
    page = rx.container(
        login()
    )
    

    return page