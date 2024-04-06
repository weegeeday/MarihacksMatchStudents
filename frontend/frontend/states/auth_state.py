import reflex as rx


class AuthState(rx.State):
    """The app state."""
    logged_in : bool = rx.LocalStorage(False)
    is_admin : bool = rx.LocalStorage(False)

    username : str = rx.LocalStorage("")

    def check_login(self):
        print("login attempt")
        print(self.logged_in)
        print(self.is_admin)
        
        if not self.logged_in:
            return rx.redirect("/")

    def check_admin_login(self):
        print("admin login attempt")
        print(self.logged_in)
        print(self.is_admin)
        if not self.logged_in or not self.is_admin:
            return rx.redirect("/admin-login")
    
    
    def logout(self):
        print("logout")
        self.logged_in, self.is_admin = False, False
        return rx.redirect("/")