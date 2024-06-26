import sqlite3

from .acount import Acount

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)

    return conn

def create_table(conn):
    """
    :param conn: Connection object
    """
    create_acount = """ CREATE TABLE IF NOT EXISTS acounts (
                                        username text PRIMARY KEY,
                                        password text NOT NULL,
                                        mainImagePath text,
                                        profileImagePath text 
                                    ); """
    try:
        c = conn.cursor()
        c.execute(create_acount)
    except Exception as e:
        print(e)

def insert_ac(conn: sqlite3.Connection, acount: Acount):
    insert_acount = """ INSERT INTO acounts VALUES (
                            :username,
                            :passwort,
                            :mainImagePath,
                            :profileImagePath
                            ) """
    with conn:
        try:
            c = conn.cursor()
            # c.execute("Select count(*) from acounts")
            # id = c.fetchall()[0][0]
            c.execute(insert_acount, {
                'username': acount.username,
                'passwort': acount.password,
                'mainImagePath': acount.mainImagePath,
                'profileImagePath': acount.profileImagePath
                })
        except Exception as e:
            print(e)

# def main():
#     database = "acounts_db.db"

#     create_acount = """ CREATE TABLE IF NOT EXISTS acounts (
#                                         username text PRIMARY KEY,
#                                         password text NOT NULL,
#                                         mainImagePath text,
#                                         profileImagePath text 
#                                     ); """

#     conn = create_connection(database)

#     if conn is not None:
#         create_table(conn, create_acount)
#     else:
#         print("Error! cannot create the database connection.")
    
# def get_ac_by_name(c, ac):
#     c.execute("SELECT * FROM acounts WHERE username=:last", {'last':ac.username})
#     return c.fetchall()

# def update_zoom(conn, ac, zoom):
#     with conn:
#         try:
#             c = conn.cursor()
#             c.execute("""UPDATE acounts SET zoom=:zoom
#                     WHERE username=:first""", 
#                     {'pay':zoom, 'first':ac.username})
#         except Exception as e:
#             print(e)
        
# def remove_ac(conn, ac):
#     with conn:
#         try:
#             c = conn.cursor()
#             c.execute("DELETE from acounts WHERE first = :first AND last=:last", {'first':ac.first, 'last':ac.last})
#         except Exception as e:
#             print(e)