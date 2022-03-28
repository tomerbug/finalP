import sqlite3
def Dbinit():
    url2 = r'C:\Users\Tomer\OneDrive\Desktop\Devops\final1.db'
    conn = sqlite3.connect(url2)
    print(type(conn))
    cursor = conn.cursor()
    return conn, cursor

def create_user(full_name,password,ID_FORM): #creates new user
    conn, cursor = SQL_connect.Dbinit()
    cursor = SQL_connect.getIdUser()
    cur.execute(f" INSERT INTO users(full_name,password,real_id) values ({full_name},{password},{ID_FORM})")
    SQL_connect.close_sql(conn, cursor)

def get_user_id(x, cursor): #get id user
    SqlStatment = f"SELECT * from users where id_Al = {x}"
    cursor.execute(SqlStatment)
    return cursor

def get_User(crusor): #get Users
    crusor.execute(f"SELECT * FROM users ")
    return  crusor

def post_user(crusor,full_name,password,ID_FORM): #post user
    # crusor.execute(f"INSERT INTO users (full_name,password,real_id) values ({full_name},{password},{ID_FORM}) ")
    crusor.execute("INSERT INTO users(full_name,password,real_id) VALUES (?, ?, ?)", (full_name, password, ID_FORM))
    return crusor
#deletes user
def delete_user(x, cursor):
    crusor.execute(f"DELETE FROM users WHERE id_Al = {x}")
    return crusor
#????????
def put_user(x, cursor,name):
    crusor.execute(f"INSERT INTO users (full_name) values {name} where id_Al = {x}")
    return crusor

def close_sql(conn):
    conn.commit()
    conn.close()

