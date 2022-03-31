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
    cursor.execute(f"DELETE FROM users WHERE id_Al = {x}")
    return cursor
#????????
def put_user(cursor,name):
    crusor.execute(f"INSERT INTO users (full_name) values {name}")
    return crusor

def get_flights(cursor):
    cursor.execute(f"SELECT * FROM flights ")
    return cursor

def get_f_id(cursor,x):
    cursor.execute(f"SELECT * FROM flights where flight_id = {x}")
    return cursor

def post_flights(crusor, time, seats, origin_country,dest_country):
    crusor.execute("INSERT INTO Flights(timestamp,remaining_seats,origin_country_id,dest_country_id) VALUES (?, ?, ?, ?)", (time, seats, origin_country,dest_country))
    return crusor

def delete_flight(cursor, x):
    cursor.execute(f"delete FROM Flights WHERE flight_id = {x}")
    return cursor

def get_tickets(cursor):
    cursor.execute(f"SELECT * FROM Tickets ")
    return cursor

def get_tickets_id(cursor,x):
    cursor.execute(f"SELECT * FROM flights where ticket_id = {x}")
    return cursor

def post_post_tickets_sql(cursor,userID,flightID):
    crusor.execute("INSERT INTO Tickets(user_id,flight_id) VALUES (?, ?)", (userID,flightID))
    return crusor

def delete_ticket(cursor, x):
    cursor.execute(f"DELETE FROM Tickets WHERE ticket_id = {x}")
    return cursor
def close_sql(conn):
    conn.commit()
    conn.close()

