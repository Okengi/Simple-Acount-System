from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import os


class Acount:
    def __init__(self, name, passwort, image):
        self._username = name
        self._passwort = passwort
        self._image = image
        self._profilimage = image
        self.zoom = 0.4

    def menuBar(self):
        menubar = Menu(self._acount, bg="black")
        self._acount.config(menu=menubar, bg="black")

        fileMenu = Menu(menubar, tearoff=0, font=10, fg='white', bg='black')
        menubar.add_cascade(label="Acount", menu=fileMenu, font=10)
        fileMenu.add_command(label="Open")
        fileMenu.add_command(label="Save")
        fileMenu.add_separator()

        setingMenu = Menu(fileMenu, tearoff=0)
        fileMenu.add_cascade(label="Setings", menu=setingMenu)
        setingMenu.add_command(label="Lightword", command=self.lightmode)
        setingMenu.add_command(label="Darkmode", command=self.darkmode)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=quit)

        personalMenu = Menu(menubar, tearoff=0, font=10, fg='white', bg='black')
        picturSizeMenu = Menu(personalMenu, tearoff=0, font=10, fg='white', bg='black')

        picturSizeMenu.add_command(label="5", command=lambda: self.scalePictur(5 * self.zoom))
        picturSizeMenu.add_command(label="3", command=lambda: self.scalePictur(3 * self.zoom))
        picturSizeMenu.add_command(label="2", command=lambda: self.scalePictur(2 * self.zoom))
        picturSizeMenu.add_command(label="1/2", command=lambda: self.scalePictur(0.5 * self.zoom))
        picturSizeMenu.add_command(label="1/3", command=lambda: self.scalePictur(0.33 * self.zoom))
        picturSizeMenu.add_command(label="1/5", command=lambda: self.scalePictur(0.2 * self.zoom))


        personalMenu.add_cascade(label="Picture size", menu=picturSizeMenu)
        personalMenu.add_command(label="Change Pictur", command=lambda: self.changePictur())
        personalMenu.add_command(label="Profil pictur", command=lambda: self.changeProfilPictur())

        menubar.add_cascade(label="Personalising", menu=personalMenu, font=9)

    def scalePictur(self, size):
        self.zoom = size
        self.label.destroy()
        self.picturLoad()

    def changePictur(self):
        path = askopenfilename(initialdir=os.getcwd(), title="Select Image File",
                                          filetypes=(("JPG File", "*jpg"), ("PNG File", "*.png"), ("All Files", "*.*")))
        self._image = path
        try: 
            self.label.destroy()
        except AttributeError:
            self.label = None
        self.picturLoad()

    def changeProfilPictur(self):
        path = askopenfilename(initialdir=os.getcwd(), title="Select Image File",
                                          filetypes=(("JPG File", "*jpg"), ("PNG File", "*.png"), ("All Files", "*.*")))
        self._profilimage = path
        self.profilPictur()

    def profilPictur(self):
        iconProfil = Image.open(self._profilimage)
        self.imgProfilPic = ImageTk.PhotoImage(iconProfil)

        self._acount.iconphoto(False, self.imgProfilPic)

    def picturLoad(self):
        icon = Image.open(self._image)
        pixels_x, pixels_y = tuple([int(self.zoom * x) for x in icon.size])

        self.img = ImageTk.PhotoImage(icon.resize((pixels_x, pixels_y)))

        self.label = Label(self._acount, image=self.img)

        self.label.grid(column=0, row=0)

    def openAcount(self):
        root.destroy()

        self._acount = Tk()
        self._acount.geometry("800x900")
        self._acount.title(self._username)

        self.menuBar()

        self.picturLoad()

        self._acount.config(background='black')
        # self._acount.iconphoto(False, self.img)
        self.profilPictur()
        self._acount.mainloop()

    def login(self, passwortEnterd):
        if passwortEnterd == self._passwort:
            self.openAcount()

    def lightmode(self):
        self._acount.config(background='white')

    def darkmode(self):
        self._acount.config(background='black')


acount1 = Acount("okinyi", "hi", "C:\\Users\\achuo\\Pictures\\Screenshots\\Screenshot (1).png")
acount2 = Acount("testuser", "hi", r"C:\Users\achuo\Pictures\2018-05-30\FB_IMG_1527704878866.jpg")
a3 = Acount("nice", "hi", r"C:\Users\chuon\Pictures\Screenshots\PileUp 26.12.2022 12_39_52.png")

acountlist = [acount1, acount2, a3]


def loginAcount():
    username = username_entry.get()
    password = password_entry.get()

    for i in acountlist:
        if i._username == username:
            i.login(password)
    complainsLabel.configure(text="Name or password wrong")


# root window
root = Tk()
root.geometry("1200x500")
root.title('Login')
root.resizable(0, 0)

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

# username
username_label = Label(root, text="Username:", font=('Chiller', 50), fg='yellow', bg='black')
username_label.grid(column=0, row=0, sticky=W, padx=20, pady=20)

username_entry = Entry(root, font=('Chiller', 50), fg='yellow', bg='black', insertbackground='yellow', insertwidth=5, insertborderwidth=1)
username_entry.grid(column=1, row=0, sticky=E, padx=5, pady=5)

# password
password_label = Label(root, text="Password:", font=('Chiller', 50), fg='yellow', bg='black')
password_label.grid(column=0, row=1, sticky=W, padx=20, pady=20)

password_entry = Entry(root, show="*", font=('Chiller', 50), fg='yellow', bg='black', insertbackground='yellow', insertwidth=5, insertborderwidth=1)
password_entry.grid(column=1, row=1, sticky=E, padx=20, pady=20)

# login
login_butten = Button(root, text="Login", command=loginAcount, font=('Chiller', 50), fg='yellow', bg='black')
login_butten.grid(column=1, row=3, sticky=E, padx=20, pady=20)

# complain-label
complainsLabel = Label(root, text="", font=('Chiller', 25), fg='yellow', bg='black')
complainsLabel.grid(column=0, row=3, sticky=E)


root.config(background='black')
root.mainloop()