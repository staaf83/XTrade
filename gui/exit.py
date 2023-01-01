import tkinter as tk

from gui.widgets import GUIWidgets


class GUIExit(tk.Toplevel):

    def __init__(self, window):
        super(GUIExit, self).__init__(window)
        GUIWidgets(self).getHeader()
        GUIWidgets(self).getExitButtons()
        self.overrideredirect(True)
        self.geometry("+%d+%d" % (window.winfo_x(), window.winfo_y()))
        self.withdraw()

