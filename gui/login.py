import tkinter as tk
from gui.widgets import GUIWidgets
from gui.exit import GUIExit


class GUILogin(tk.Toplevel):

    def __init__(self, window):
        super(GUILogin, self).__init__(window)
        GUIWidgets(self).getHeader()
        GUIWidgets(self).getUsernameLabel()
        GUIWidgets(self).getUsernameEntry()
        GUIWidgets(self).getPasswordLabel()
        GUIWidgets(self).getPasswordEntry()
        GUIWidgets(self).getPasswordButton()
        GUIWidgets(self).getServerType()
        GUIWidgets(self).getLagalNotice()
        GUIWidgets(self).getLink()
        GUIWidgets(self).saveDataButton()
        GUIWidgets(self).getConnectButton()
        GUIWidgets(self).getQuiteButton(GUIExit(window))
        
        self.overrideredirect(True)
        self.geometry("+%d+%d" % (window.winfo_x(), window.winfo_y()))
