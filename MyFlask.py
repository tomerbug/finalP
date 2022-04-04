import  SQL_connect
from flask import  Flask
from flask import flash,render_template,request,redirect,url_for
import json
import  sqlite3
import logging
app = Flask(__name__)
app.secret_key ="__privatekey__"
#Home PAGE
@app.route('/',methods =['POST','GET'])
def home_page():
    return render_template("Home.html")

@app.route('/register',methods =['POST','GET'])
def reg_page():
    return render_template("register.html")
#get all users
@app.route('/users',methods = ['GET'])
def getUser():
    conn,crusor= SQL_connect.Dbinit()
    par = ""
    SQL_connect.get_User(crusor)
    for row in crusor:
        z = str(row)
        par = z + par
    SQL_connect.close_sql(conn)
    return par
#get user by id
@app.route('/users/<int:x>',methods = ['GET'])
def checkUser(x):
    par=""
    conn,cursor =SQL_connect.Dbinit()
    cursor = SQL_connect.get_user_id(x,cursor)
    for row in cursor:
        z= str(row)
        par= z + par
    SQL_connect.close_sql(conn)
    return  par
#post the client info
@app.route('/register/user',methods = ['POST'])
def post_new():
    conn, crusor = SQL_connect.Dbinit()
    password = request.form['password']
    full_name = request.form['username']
    ID_FORM = request.form['ID']
    s = SQL_connect.post_user(crusor,full_name,password,ID_FORM)

    SQL_connect.close_sql(conn)
    return 'user created'
@app.route('/form/userup',methods =['POST','GET'])
def updated_user_page():
    return render_template("usersUp.html")
#put user
@app.route('/usercheck/put', methods = ['PUT', 'POST'])
def put_users():
    conn, cursor = SQL_connect.Dbinit()
    userID = request.form['user_id']
    password = request.form['password']
    id_client = request.form['realId']
    SQL_connect.put_users(cursor,userID, password, id_client)
    SQL_connect.close_sql(conn)
    return "user updated"

@app.route('/user/delete/<int:x>', methods = ['DELETE'])
# def delete_user(x):
def delete_user(x):
     conn, cursor = SQL_connect.Dbinit()
     par = ""
     cursor = SQL_connect.delete_user(x, cursor)
     SQL_connect.close_sql(conn)
     return"user deleted"

#########################flights###################
#get flights
@app.route('/form/flight',methods = ['GET'])
def form():
    #function for the form -flight post
    return render_template('flights.html')

    return render_template('flights.html')
@app.route('/flights', methods = ['GET'])
def get_f():
    conn, cursor = SQL_connect.Dbinit()
    par = ""
    cursor = SQL_connect.get_flights(cursor)
    for row in cursor:
        z = str(row)
        par = z + par
    SQL_connect.close_sql(conn)
    return par
#get flights/id
@app.route('/flights/get/<int:x>', methods = ['GET'])
def get_f_id_flask(x):
    conn, cursor = SQL_connect.Dbinit()
    par = ""
    cursor = SQL_connect.get_f_id(cursor,x)
    for row in cursor:
        z = str(row)
        par = z + par
    SQL_connect.close_sql(conn)
    return par
@app.route('/form/flights',methods =['POST','GET'])
def flight_form():
    return render_template("Flights.html")
#post flights
@app.route('/flight/add', methods = ['POST'])#
def get_post_flight_flask():
    par = " "
    conn , cursor = SQL_connect.Dbinit()
    time = request.form['TIMESTAMP']
    seats = request.form['REMAINMGSEATS']
    origin_country = request.form['ORIGIONCOUNTRYID']
    dest_country = request.form['DESTCOUNTRYID']
    s = SQL_connect.post_flights(cursor, time, seats, origin_country,dest_country)
    for row in cursor:
        z = str(row)
        par = z + par
    SQL_connect.close_sql(conn)
    return par
@app.route('/flightUpdate',methods =['PUT', 'GET'])
def update_flights():
    return render_template("flightUpdate.html")
###put flights
@app.route('/check/put', methods = ['PUT', 'POST'])#לא עובד
def put_flight():
    conn, cursor = SQL_connect.Dbinit()
    flightID = request.form['flightID']
    time = request.form['TIMESTAMP']
    seats = request.form['REMAINMGSEATS']
    origin_country = request.form['ORIGIONCOUNTRYID']
    dest_country = request.form['ORIGIONCOUNTRYID']
    SQL_connect.put_flights(cursor,flightID, time, seats, origin_country, dest_country)
    SQL_connect.close_sql(conn)
    return "flight updated"
#delete flights
@app.route('/flights/delete/<int:x>', methods = ['DELETE'])
def delete_flight_f(x):
    conn, cursor = SQL_connect.Dbinit()
    cursor =SQL_connect.delete_flight(cursor, x)
    SQL_connect.close_sql(conn)
    return "deleted"

###############tickets#############
#get tickets
@app.route('/tickets', methods = ['GET'])
def get_t():
    conn, cursor = SQL_connect.Dbinit()
    par = ""
    cursor = SQL_connect.get_tickets(cursor)
    for row in cursor:
        z = str(row)
        par = z + par
    SQL_connect.close_sql(conn)
    return par
#get ticket id
@app.route('/tickets/get/<int:x>', methods = ['GET'])
def get_t_id(x):
    conn, cursor = SQL_connect.Dbinit()
    par = ""
    cursor = SQL_connect.get_tickets_id(cursor,x)
    for row in cursor:
        z = str(row)
        par = z + par
    SQL_connect.close_sql(conn)
    return par
#page of tickets
@app.route('/form/tickets',methods = ['GET'])
def form_ticket():
    return render_template('tickets.html')
# post ticket
@app.route('/ticket/post', methods = ['POST'])
def post_t():
    conn, cursor = SQL_connect.Dbinit()
    par = ""
    userID = request.form['User Id']
    flightID = request.form['flight Id']
    cursor = SQL_connect.post_tickets_sql(cursor,userID,flightID)

    SQL_connect.close_sql(conn)
    return par
#DELETE TICKET
@app.route('/tickets/delete/<int:x>', methods = ['DELETE'])
def ticket_delete_f(x):
    conn, cursor = SQL_connect.Dbinit()
    cursor =SQL_connect.delete_ticket(cursor, x)
    SQL_connect.close_sql(conn)
    return "deleted"



######CLIENT SIDE############
@app.route("/manu", methods=['GET'])
def manu():
    return render_template('manu.html')
#login the client
@app.route("/login", methods=['GET'])
def login():
        username = request.args['username']
        password = request.args['password']
        realId = request.args['ID']
        conn, cursor = SQL_connect.Dbinit()
        cursor.execute(f"select * from users where real_id={realId}")
        rows = cursor.fetchall()
        for row in rows:
            if(row[1] == username and row[2] == password and row[3] == realId):
                flash("Login Successful!")
                return render_template('/manu.html')
            else:
                return "info was incorrect"
#register the client
@app.route("/register/post", methods=['POST'])
def register():
    full_name = request.form['username']
    password = request.form['password']
    ID_FORM = request.form['ID']
   # NULL = " "
    conn, cursor = SQL_connect.Dbinit()
    if(full_name == None or password == None or ID_FORM == None):
        return "one of the parameter seems to be empty , please try again"
        SQL_connect.close_sql(conn)
    else:
        SQL_connect.post_user(cursor,full_name,password,ID_FORM)
        SQL_connect.close_sql(conn)
        flash("user created")
        return render_template("Home.html")
#buy ticket for client
@app.route("/form/buyT", methods=['GET'])
def form_buy_t():
    return render_template('/buyTic.html')
@app.route("/buy_ticket_P", methods=['POST'])
def buy_t():
    conn, cursor = SQL_connect.Dbinit()
    userID = request.form['FLIGHT ID']
    flightID = request.form['USER ID']
    SQL_connect.post_tickets_sql(cursor,userID,flightID)
    SQL_connect.close_sql(conn)
    flash("user got a ticket ")
    return render_template('/manu.html')
@app.route("/form/deleteT", methods=['GET'])
def form_delete_t():
    return render_template('/deleteT.html')
@app.route('/deleteTic/',methods=['GET'])
def ticket_delete_from_client():
    TICKET_ID = request.args['TICKET ID']
    return ticket_delete_f(TICKET_ID)
#get the clients tickets
@app.route("/form/post_user_page", methods=['GET'])
def form_delete_tic():
    return render_template('/POST_USER_CLIENT.html')

@app.route("/post_user_page", methods=['GET'])
def get_ticket_from_client():
    conn, cursor = SQL_connect.Dbinit()
    user_id = request.args['user id']
    par = " "
    cursor.execute(f"SELECT * FROM Tickets where user_id = {user_id}")
    for row in cursor:
        z = str(row)
        par = z + par
    SQL_connect.close_sql(conn)
    return par



app.run()