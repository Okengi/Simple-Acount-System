import os

from .SQL_Setup import create_connection
from .SQL_Setup import create_table
from .frontend import Frontend


class acount_system:
    def __init__(self, name: str) -> None:
        """
        :param str name: The name of the system. It is going to try to connect to an system with the name if it doesn't exist it's going to be created.
        """

        CURRENT_FOLDER = os.getcwd()
        path = os.path.join(CURRENT_FOLDER, name)

        if not os.path.isdir(path):
            self.create_folder_system(path)
    
    def start(self):
        frontend = Frontend()
        frontend.login()

    def create_folder_system(self, path):
        os.mkdir(path)
        cur_path  = os.path.join(path, "acounts_db.db")
        conn = create_connection(cur_path)
        create_table(conn)
        # should probably alredy create a user here