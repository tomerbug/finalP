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
def put_users(cursor,userID,  password, id_client):
    cursor.execute(f'UPDATE users SET password = {password}, real_id = {id_client} WHERE id_Al = {userID}')
    return cursor

def get_flights(cursor):#get flights
    cursor.execute(f"SELECT * FROM flights ")
    return cursor

def get_f_id(cursor,x):#get flight by id
    cursor.execute(f"SELECT * FROM flights where flight_id = {x}")
    return cursor

def post_flights(cursor, time, seats, origin_country,dest_country):#creates new flight
    cursor.execute(f"INSERT INTO Flights(timestamp,remaining_seats,origin_country_id,dest_country_id) VALUES ({time}, {seats}, {origin_country}, {dest_country})")
    return cursor
def put_flights(cursor,flightID, time,seats,origin_country, dest_country):#updates a flight
    cursor.execute(f'UPDATE flights SET timestamp = {time},remaining_seats = {seats}, origin_country_id = {origin_country}, dest_country_id = {dest_country} WHERE flight_id = {flightID}')
def delete_flight(cursor, x):
    cursor.execute(f"delete FROM Flights WHERE flight_id = {x}")
    return cursor

def get_tickets(cursor):#get all tickets
    cursor.execute(f"SELECT * FROM Tickets ")
    return cursor

def get_tickets_id(cursor,x):#get tickets by id
    cursor.execute(f"SELECT * FROM Tickets where ticket_id = {x}")
    return cursor

def post_tickets_sql(cursor,userID,flightID):#creates new ticket
    cursor.execute(f"INSERT INTO Tickets(user_id,flight_id) VALUES ({userID}, {flightID})")
    return cursor

def delete_ticket(cursor, x):#deletes ticket
    cursor.execute(f"DELETE FROM Tickets WHERE ticket_id = {x}")
    return cursor


def CheckUser(cursor):
    cursor.execute(f'select password from users WHERE full_name = {name}')
    return cursor
#closes the connection to the sql
def close_sql(conn):
    conn.commit()
    conn.close()

