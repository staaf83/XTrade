import tkinter as tk
from tkinter import Button, ttk
from PIL import Image, ImageTk
from gui.utils import GUIUtils

class GUIWidgets:
    def __init__(self, root):
        self.root = root
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure('TMenubutton', font='helvetica 11')
        self.legalNotice = tk.BooleanVar()
        self.serverType = tk.StringVar()
        self.utils = GUIUtils(self.root)

    def getHeader(self):
        header = tk.Label(self.root, text="XTrade", width=60, height=2, borderwidth=3, relief='ridge')
        header.grid(row=0, columnspan=5,sticky='nesw')
        self.utils.move(header)
        return header

    def getUsernameLabel(self):
        usernameLabel = tk.Label(self.root, text="Login: ")
        usernameLabel.grid(row=1, column=0, pady=(10, 10), padx=(10, 10), sticky="E")
        return

    def getUsernameEntry(self):
        usernameEntry = tk.Entry(self.root)
        usernameEntry.grid(row=1, column=1, columnspan=3, pady=(10, 10), padx=(10, 10), sticky='nesw')
        self.utils.confirmEntry("login", usernameEntry, self.getConnectButton())
        return usernameEntry

    def getPasswordLabel(self):
        passwordLabel = tk.Label(self.root, text="Password: ")
        passwordLabel.grid(row=2, column=0, pady=(10, 10), padx=(10, 10), sticky="E")
        return passwordLabel

    def getPasswordEntry(self):
        passwordEntry = tk.Entry(self.root, show="*")
        passwordEntry.grid(row=2, column=1, columnspan=3, pady=(10, 10), padx=(10, 10), sticky='nesw')
        self.utils.confirmEntry("password", passwordEntry, self.getConnectButton())
        return passwordEntry

    def getPasswordButton(self):
        self.image = ImageTk.PhotoImage(Image.open("gui/images/eye.png").resize((15,15), Image.ANTIALIAS))
        passwordButton = Button(self.root, bd=1, image=self.image)
        passwordButton.grid(row=2, column=4, sticky="W")
        self.utils.show(passwordButton, self.getPasswordEntry())
        return passwordButton
    
    def getServerType(self):
        serverTypeLabel = tk.Label(self.root,  text='Server type: ')
        serverTypeLabel.grid(row=3, column=0, pady=(10, 10), padx=(10, 10), sticky="E")
        acc = ('-', 'Demo', 'Real               ')
        server = ttk.OptionMenu(self.root, self.serverType, acc[0], acc[1], acc[2], command=lambda e: self.utils.confirmEntry("server", self.serverType, self.getConnectButton()))
        server.grid(row=3, column=1, columnspan=3,pady=(10, 10), padx=(10, 10), sticky="WE")
        server["menu"].configure(font='helvetica 11')
        return server
    
    def getLagalNotice(self):
        legalNoticeLabel = tk.Label(self.root, text="Legal notice: ")
        legal = tk.Checkbutton(self.root, variable=self.legalNotice, onvalue=1, offvalue=0, command=lambda: self.utils.confirmEntry("license", self.legalNotice, self.getConnectButton()))
        legalNoticeLabel.grid(row=4, column=0, pady=(10, 10), padx=(10, 10), sticky="SE")
        legal.grid(row=4, column=1, pady=(0, 0), padx=(0, 0))
        return legal
    
    def getLink(self):
        link = tk.Label(self.root, text="Legal notice", fg="blue", cursor="hand2", font= ('Helvetica 8 underline italic'))
        link.grid(row=4, column=2, pady=(0, 0), padx=(0, 0), sticky="W")
        self.utils.openUrl(link)
        return link

    def saveDataButton(self):
        saveDataLabel = tk.Label(self.root, text="Remember data: ")
        saveDataLabel.grid(row=5, column=0, pady=(10, 10), padx=(10, 10), sticky="SE")
        save = tk.Checkbutton(self.root, variable=self.legalNotice, onvalue=1, offvalue=0, command=lambda: self.utils.confirmEntry("license", self.legalNotice, self.getConnectButton()))
        save.grid(row=5, column=1, pady=(0, 0), padx=(0, 0))
        return save
    
    def getConnectButton(self):
        connectButton = tk.Button(self.root, text="CONNECT", state=self.utils.checkData(), command=lambda: self.utils.connect())
        connectButton.grid(row=6, columnspan=4, sticky='nesw', pady=(10, 10), padx=(10, 10))    
        return connectButton

    def getQuiteButton(self, exitWindow):
        quiteButton = tk.Button(self.root, text="Quit", command=lambda: self.utils.showExitWindow(exitWindow))
        quiteButton.grid(row=6, column=4, sticky='nesw', pady=(10, 10), padx=(10, 10))
        return quiteButton
    
    def getExitButtons(self):
        labelExit = tk.Label(self.root, text="Are you sure you want to exit?")
        labelExit.grid(row=1, columnspan=4, pady=(50, 40))
        exitButton = tk.Button(self.root, text="Exit", width=10, command=lambda: self.utils.exit())
        exitButton.grid(row=2, column=3, sticky='nesw', pady=(10, 10), padx=(10, 10))
        cancelButton = tk.Button(self.root, text="Cancel", width=10, command=lambda: self.utils.cancelExit())
        cancelButton.grid(row=2, column=4, sticky='nesw', pady=(10, 10), padx=(10, 10))
        return exitButton
        
        




    




"""     

        # Przycisk podejrzyj haslo #
        self.image = ImageTk.PhotoImage(Image.open("gui/images/eye.png").resize((15,15), Image.ANTIALIAS))
        self.b = Button(self.win, bd=1, image=self.image)
        self.b.bind("<Button-1>", lambda e: self.function.entry_show(self.password_entry))
        self.b.bind("<ButtonRelease-1>", lambda e: self.function.entry_hide(self.password_entry))
        self.b.grid(row=2, column=4, sticky="W")
       



      # Przycisk podejrzyj haslo #
        self.image = ImageTk.PhotoImage(Image.open("gui/images/eye.png").resize((15,15), Image.ANTIALIAS))
        self.b = Button(self.win, bd=1, image=self.image)
        self.b.bind("<Button-1>", lambda e: self.function.entry_show(self.password_entry))
        self.b.bind("<ButtonRelease-1>", lambda e: self.function.entry_hide(self.password_entry))
        self.b.grid(row=2, column=4, sticky="W")
      

        # Przycisk podejrzyj haslo #
        self.image = ImageTk.PhotoImage(Image.open("gui/images/eye.png").resize((15,15), Image.ANTIALIAS))
        self.b = Button(parent, bd=1, image=self.image)

        # Przyciski polacz i wyjdz #
        self.login_button = tk.Button(parent, text="CONNECT",state="disabled")
        #, command=self.login)
 
        
        
        self.login_button.grid(row=6, columnspan=4, sticky='nesw', pady=(10, 10), padx=(10, 10))
        

    def c_button(self):
        self.cancel_button = tk.Button(self.parent, text="Quit")
        self.cancel_button.grid(row=6, column=4, sticky='nesw', pady=(10, 10), padx=(10, 10))
        return self.cancel_button """