import tkinter as tk
from gui.login import GUILogin
from gui.exit import GUIExit
from gui.widgets import GUIWidgets
from auth.data import AuthData

class GUIMain(tk.Tk):

    def __init__(self):
        super().__init__()
        self.overrideredirect(True)
        self.eval('tk::PlaceWindow . center')
        
        if AuthData().getData("data.bin")["logged"]:
            GUILogin(self).withdraw()
            self.deiconify()
            self.lift()
            GUIWidgets(self).getHeader()
            GUIWidgets(self).getQuiteButton(GUIExit(self))
        else:
            self.withdraw()
            GUILogin(self).lift()

        self.mainloop()