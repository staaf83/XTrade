class GUIStyles:
    def __init__(self):
        self.button_fg_color = "#ffffff"

    def ex(self, button):
        button.configure(bg=self.button_bg_color, fg=self.button_fg_color, font=self.button_font)



        #set_button_style(self.button)