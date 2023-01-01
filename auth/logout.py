class Logout:
    def logout(self):
        """Wyloguj się z aplikacji."""
        self.logged_in = False
        self.username = None
        self.main_win.hide()
        self.show_login_window()