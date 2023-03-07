from tkinter import *
from functools import partial

from backend import Backend

class Register:
    def __init__(self) -> None:
        self.backend = Backend()

    def validateRegister(self, username, password):
        ac = self.backend.get_ac_by_name(username.get())
        if ac == []:
            self.errorLabel.config(text="")
        else:
            self.ac = []
            self.errorLabel.config(text="Username already exist")
    
    def closeWindow(self):
            self.tkWindow.destroy()

    def register(self):
        self.tkWindow = Tk()  
        self.tkWindow.geometry('500x200')  
        self.tkWindow.title('Register')
        self.tkWindow.resizable(False, False)
        self.tkWindow.grid()

        #username label and text entry box
        usernameLabel = Label(self.tkWindow, text="Username:", font=("Helvetica",24,"bold")).grid(row=0, column=0)
        username = StringVar()
        usernameEntry = Entry(self.tkWindow, textvariable=username, font=("Helvetica",20,"bold")).grid(row=0, column=1)  

        
        passwordLabel = Label(self.tkWindow,text="Password:", font=("Helvetica",24,"bold")).grid(row=1, column=0)  
        password = StringVar()
        passwordEntry = Entry(self.tkWindow, textvariable=password, show='*', font=("Helvetica",20,"bold")).grid(row=1, column=1)  

        self.validateRegister = partial(self.validateRegister, username, password)

        #login button
        # loginButton = Button(self.tkWindow, text="Login", command=self.validateLogin, font=("Helvetica",20,"bold"), anchor=W).grid(row=3, column=1)
        registerButton = Button(self.tkWindow, text="Register", command=self.validateRegister, font=("Helvetica",20,"bold"), anchor=W).grid(row=3, column=0, columnspan=2) 
        self.errorLabel = Label(self.tkWindow, text="", font=("Helvetica",20,"bold"))
        self.errorLabel.grid(row=2, column=0, columnspan=2)

        self.tkWindow.mainloop()
        return self.ac