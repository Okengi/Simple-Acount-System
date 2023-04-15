import os

from .SQL_Setup import create_connection
from .SQL_Setup import create_table

from .acount import Acount
from .frontend import Frontend
from .backend import Backend
from .login import Login
from .register import Register


class acount_system:

    def __init__(self, name: str) -> None:
        """
        :param str name: The name of the system. It is going to try to connect to an system with the name if it doesn't exist it's going to be created.
        """

        CURRENT_FOLDER = os.getcwd()
        path = os.path.join(CURRENT_FOLDER, name)

        if not os.path.isdir(path):
            self.create_folder_system(path)
        else:
            self.db_path = os.path.join(path, "acounts_db.db")
        
        self.backend = Backend(self.db_path)                    # In the Future i need to put login and register into frontend
        self._register = Register(self.backend)                 # because this is a mess
        self.login = Login(self.backend, self._register)       
        self.frontend = Frontend(self.backend, self.login)   
        
    
    def start(self):
        self.frontend.login()
    
    def register(self, acount_to_register: Acount):
        self.backend.insert_ac(acount_to_register)
        
    def create_folder_system(self, path):
        os.mkdir(path)
        self.db_path  = os.path.join(path, "acounts_db.db")
        conn = create_connection(self.db_path)
        create_table(conn)
        ac = Acount("Default", "1234", "C:\\Users\\chuon\\Documents\\Programming\\Python\\acountSystem\\my_octocat.png", "C:\\Users\\chuon\\Documents\\Programming\\Python\\acountSystem\\my_octocat.png")
        self.register(ac)
        conn.commit()
        conn.close()