from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import sys

from .backend import Backend
from .login import Login
from .acount import Acount

class Frontend:
    """
        The Frontent class displays an acount. It get's it's information from the Backend class.
    """
    def __init__(self) -> None:
        self.backend = Backend()
        self.loginn = Login()
    
    def login(self):
        """
            The login funkition calls the login function of the Login variable.
            To start the system.
        """
        ac = self.loginn.login()
        self.main(ac)

    def menubar(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        settingsMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Settings",menu=settingsMenu)
        settingsMenu.add_command(label="Change")

        personalisirungsMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Personalisirung",menu=personalisirungsMenu)

        picturSizeMenu = Menu(personalisirungsMenu, tearoff=0, font=10, fg='white', bg='black')

        picturSizeMenu.add_command(label="5", command=lambda: self.scalePictur(5 * 0.4))
        picturSizeMenu.add_command(label="3", command=lambda: self.scalePictur(3 * 0.4))
        picturSizeMenu.add_command(label="2", command=lambda: self.scalePictur(2 * 0.4))
        picturSizeMenu.add_command(label="1/2", command=lambda: self.scalePictur(0.5 * 0.4))
        picturSizeMenu.add_command(label="1/3", command=lambda: self.scalePictur(0.33 * 0.4))
        picturSizeMenu.add_command(label="1/5", command=lambda: self.scalePictur(0.2 * 0.4))


        personalisirungsMenu.add_cascade(label="Picture size", menu=picturSizeMenu)

        personalisirungsMenu.add_command(label="Change Pictur", command=lambda: self.changePictur())
        personalisirungsMenu.add_command(label="Profil pictur", command=lambda: self.changeProfilPictur())


    def main(self, ac: list):
        try:
            self.acount = Acount(ac[0][0], ac[0][1], ac[0][2], ac[0][3])
        except IndexError:
            print("ERROR: Not a valid acount!")
            sys.exit()

        self.root = Tk()
        self.root.geometry("800x900")
        self.root.title(self.acount.username)
        
        
        self.menubar()

        # self.picturLoad()

        # self._acount.iconphoto(False, self.img)
        # self.profilPictur()
        

        icon = Image.open(self.acount.mainImagePath)
        pixels_x, pixels_y = tuple([int(0.4 * x) for x in icon.size])

        self.img = ImageTk.PhotoImage(icon.resize((pixels_x, pixels_y)))

        self.label = Label(self.root, image=self.img)

        self.label.grid(column=0, row=0)


        self.root.mainloop()

if __name__ == "__main__":
    frontent = Frontend()
    frontent.login()