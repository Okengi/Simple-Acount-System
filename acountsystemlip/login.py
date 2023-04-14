from tkinter import *
from functools import partial

from .backend import Backend
from .register import Register

class Login:
    """
        The Login class can login into an acount from the acounts_db.db database.
    """
    def __init__(self) -> None:
        self.backend = Backend()
        self.register = Register()
    
    def startregister(self):
        
        self.ac = self.register.register()
        self.closeWindow()

    
    def validateLogin(self, username, password):
        """
            Checks if the input is correct and closes the login window if so.
        """
        ac = self.backend.get_ac_by_name(username.get())
        if ac != []:
            self.errorLabel.config(text="")
            if ac[0][1] == password.get():
                self.ac = ac
                self.errorLabel.config(text="")
                self.closeWindow()
            else:
                self.errorLabel.config(text="Password wronge")
        else:
            self.ac = []
            self.errorLabel.config(text="Username dosn't exist")

    def login(self):
        """
            The login function setsup an login window.
        """
        self.tkWindow = Tk()  
        self.tkWindow.geometry('500x200')  
        self.tkWindow.title('Login')
        self.tkWindow.resizable(False, False)
        self.tkWindow.grid()

        #username label and text entry box
        usernameLabel = Label(self.tkWindow, text="Username:", font=("Helvetica",24,"bold")).grid(row=0, column=0)
        username = StringVar()
        usernameEntry = Entry(self.tkWindow, textvariable=username, font=("Helvetica",20,"bold")).grid(row=0, column=1)  

        
        passwordLabel = Label(self.tkWindow,text="Password:", font=("Helvetica",24,"bold")).grid(row=1, column=0)  
        password = StringVar()
        passwordEntry = Entry(self.tkWindow, textvariable=password, show='*', font=("Helvetica",20,"bold")).grid(row=1, column=1)  

        self.validateLogin = partial(self.validateLogin, username, password)
        self.startregister = partial(self.startregister)

        #login button
        loginButton = Button(self.tkWindow, text="Login", command=self.validateLogin, font=("Helvetica",20,"bold"), anchor=W).grid(row=3, column=1)
        registerButton = Button(self.tkWindow, text="Register", command=self.startregister, font=("Helvetica",20,"bold"), anchor=W).grid(row=3, column=0) 
        self.errorLabel = Label(self.tkWindow, text="", font=("Helvetica",20,"bold"))
        self.errorLabel.grid(row=2, column=0, columnspan=2)

        self.tkWindow.mainloop()
        try:
            return self.ac
        except AttributeError:
            return [] # Only happens, because user closed window without previously pressing login button. 

    def closeWindow(self):
        self.tkWindow.destroy()