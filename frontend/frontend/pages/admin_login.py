import reflex as rx
from frontend.states.auth_state import AuthState


PASSWORD = "M4r14n0p0l1S"

class LoginAttemptState(rx.State):

    password: str = ""

    def login(self):
        if self.password == PASSWORD:
            AuthState.logged_in, AuthState.is_admin = True, True
            self.password = ""
            return rx.redirect("/admin")
        else:
            return rx.window_alert("Invalid Password")
        

def login():
    login_component = rx.container(
        rx.center(
            rx.card(
                rx.vstack(
                    rx.text("Please enter admin password."),
                    rx.input(placeholder="Password", type="password", on_change=LoginAttemptState.set_password),
                    rx.button("Submit", on_click=LoginAttemptState.login), 
                )
        )
    )
)
    return login_component



def admin_login():
    LoginAttemptState.password = ""
    page = rx.container(
        login()
    )
    

    return page