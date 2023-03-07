import sqlite3
from acount import Acount

class Backend:
    def __init__(self) -> None:
        self.conn = self.create_connection("acounts_db.db")

    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Exception as e:
            print(str(e)+" Couldn't connect")
        return conn
    
    def commit(self):
        self.conn.commit()
    
    def close(self):
        self.conn.close()

    def insert_ac(self, ac):
        with self.conn:
            try:
                c = self.conn.cursor()
                c.execute("Select count(*) from acounts where username = :name", {'name': ac.username})
                id = c.fetchone()[0]
                if id > 0:
                    print("Name Already exists")
                    return
                c.execute("INSERT INTO acounts VALUES (:username, :passwort, :mainImagePath, :profileImagePath)", {'username': ac.username, 'passwort':ac.password, 'mainImagePath':ac.mainImagePath, 'profileImagePath':ac.profileImagePath})
            except Exception as e:
                print(str(e)+" Couldn't insert Acount")
    
    def get_ac_by_name(self, name):
        c = self.conn.cursor()
        c.execute("SELECT * FROM acounts WHERE username=:username", {'username':name})
        return c.fetchall()


    def update_password(self, ac, newPassword):
        with self.conn:
            try:
                c = self.conn.cursor()
                c.execute("""UPDATE acounts SET password=:newPassword
                        WHERE username=:username""", 
                        {'newPassword':newPassword, 'username':ac.username})
            except Exception as e:
                print(e)
            
    def remove_ac(self, ac):
        with self.conn:
            try:
                c = self.conn.cursor()
                c.execute("DELETE from acounts WHERE username = :username AND password=:password", {'username':ac.username, 'password':ac.password})
            except Exception as e:
                print(e)


# cs = Acount("Okengi", "hello", r"C:\Users\chuon\Pictures\Screenshots\PileUp 26.12.2022 12_39_52.png", r"C:\Users\chuon\Pictures\Screenshots\PileUp 26.12.2022 12_39_52.png")
# backend = Backend()
# backend.insert_ac(cs)