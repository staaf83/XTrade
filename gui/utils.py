import sys
import webbrowser
from auth.data import AuthData
import os

from auth.login import Login
class GUIUtils:

    def __init__(self, window):
        
        self.window = window

    def move(self, header):
        header.bind("<Button-1>", lambda e: drag(e, header))
        def drag(event, header):
            header.bind("<B1-Motion>", lambda e: drag(e, event))
            def drag(e, event):
                new_x = self.window.winfo_x() + e.x - event.x
                new_y = self.window.winfo_y() + e.y - event.y
                self.window.geometry("+{}+{}".format(new_x, new_y))
    
    def checkData(self):
        if not AuthData().getData("data.bin"):
            AuthData().createFile()
        if "login" and "password" and "server" and "license" in AuthData().getData("data.bin"):
            return "normal"
        else:
            return "disabled"

    def confirmEntry(self, key, widget, button):
        def confirm():
            value =str(widget.get()).replace(" ", "")
            AuthData().setData("data.bin", {key: value})
            button["state"] = self.checkData()
            print(AuthData().getData("data.bin"))
        match key:
            case "login" | "password":
                widget.bind('<Any-KeyPress>', lambda e: confirm())
                widget.bind('<Any-KeyPress>', lambda e: confirm())
            case "server":
                confirm()
            case "license":
                widget.set(True)
                confirm()

    def show(self, passwordButton, passwordEntry):
        passwordButton.bind("<Button-1>", lambda e: show())
        passwordButton.bind("<ButtonRelease-1>", lambda e: hide())
        def show():
            passwordEntry['show']=""
        def hide():
            passwordEntry['show']="*"

    def openUrl(self, link):
        link.bind("<Button-1>", lambda e: webbrowser.open_new("https://www.xtb.com/pl/oferta/informacje-o-rachunku/informacje-prawne"))

    def showExitWindow(self, exitWindow):
        self.window.withdraw()
        exitWindow.deiconify()
        exitWindow.lift()
        return self.window

    def cancelExit(self):
        self.window.withdraw()
        GUIUtils.__init__(self, self.window.master)
        if AuthData().getData("data.bin")["logged"]:
            self.window.master.deiconify()
            self.window.master.lift()
        else:
            python = sys.executable
            os.execl(python, python, * sys.argv)
        
        
    def exit(self):
        sys.exit()

    def connect(self):
        Login()


