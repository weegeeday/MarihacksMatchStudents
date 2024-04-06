import reflex as rx


class State(rx.State):
    """The app state."""
    logged_in : bool = False
    is_admin : bool = False