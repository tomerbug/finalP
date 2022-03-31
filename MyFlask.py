import  SQL_connect
from flask import  Flask
from flask import render_template,request,redirect,url_for
import  sqlite3
con = sqlite3.connect(r'C:\Users\Tomer\OneDrive\Desktop\Devops/final1.db')
app = Flask(__name__)

#function to store new users
#def register_user_to_db(username, password,ID):
#    con = sqlite3.connect(r'C:\Users\Tomer\OneDrive\Desktop\Devops/final1.db')
#    cur = con.cursor()
#    cur.execute('INSERT INTO users(full_name,password,real_id) values (?,?,?)', (username, password,ID))
#    con.commit()
#    con.close()
#FUNCTION THE CHECK IF USERS PUT THE CORRECT INFO
#def check_user(username, password,ID):
#    con = sqlite3.connect(r'C:\Users\Tomer\OneDrive\Desktop\Devops/final1.db')
#    cur = con.cursor()
#    cur.execute('Select username,password,real_id FROM users WHERE username=? and password=? and real_id=?', (username, password,ID))
#
#    result = cur.fetchone()
#    if result:
#        return True
#    else:
#        return False


#Home/login PAGE
@app.route('/',methods =['POST','GET'])
def home_page():
    return render_template("Flights.html")
#consider as register for now
def login():
    password = request.form['password']
    full_name = request.form['name']
    ID_FORM = request.form['ID']
  #  register_user_to_db(username, password,ID_FORM)
    creat = SQL_connect.create_user(full_name,password,ID_FORM)
    conn.commit()

@app.route('/register',methods =['POST','GET'])
def reg_page():
    return render_template("register.html")
#get user/id
@app.route('/user/<int:x>',methods = ['GET'])
def checkUser(x):
    par=""
    conn,cursor =SQL_connect.Dbinit()
    cursor = SQL_connect.get_user_id(x,cursor)
    for row in cursor:
        z= str(row)
        par= z + par
    SQL_connect.close_sql(conn)
    return  par
#get
@app.route('/Get',methods = ['GET'])
def getUser():
    conn,crusor= SQL_connect.Dbinit()
    par = ""
    SQL_connect.get_User(crusor)
    for row in crusor:
        z = str(row)
        par = z + par
    SQL_connect.close_sql(conn)
    return par
#post
@app.route('/login',methods = ['POST'])
def post_new():
    conn, crusor = SQL_connect.Dbinit()
    password = request.form['password']
    full_name = request.form['username']
    ID_FORM = request.form['ID']
    s = SQL_connect.post_user(crusor,full_name,password,ID_FORM)

    SQL_connect.close_sql(conn)
    return 'OK'

# @app.route('/delete/<int:x>',methods = ['DELETE'])
@app.route('/delete/<int:x>', methods = ['DELETE'])
# def delete_user(x):
def delete_user(x):
     conn, cursor = SQL_connect.Dbinit()
     par = ""
     cursor = SQL_connect.delete_user(x, cursor)
     SQL_connect.close_sql(conn)
     return par
#put user
@app.route('/put/<string:name>', methods = ['PUT'])
def put_user(x,name):
     conn, cursor = SQL_connect.Dbinit()
     par = ""
     cursor = SQL_connect.put_user(x, cursor,name)
     for row in crusor:
         z = str(row)
         par = z + par
     SQL_connect.close_sql(conn)
     return par
#########################flights###################
#get flights
@app.route('/form/flight',methods = ['GET'])
def form():
    #function for the form -flight post
    return render_template('flights.html')

    return render_template('flights.html')
@app.route('/flights/get', methods = ['GET'])
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
@app.route('/other', methods = ['GET'])
def exe():

    return "ok"
#post flights
@app.route('/flights/add', methods = ['POST'])#לא סיימתי!!!!
def get_post_flight_flask():
    conn , cursor = SQL_connect.Dbinit()
    time = request.form['TIMESTAMP']
    seats = request.form['REMAINMGSEATS']
    origin_country = request.form['ORIGIONCOUNTRYID']
    dest_country = request.form['ORIGIONCOUNTRYID']
    s = SQL_connect.post_flights(crusor, time, seats, origin_country,dest_country)
    SQL_connect.close_sql(conn)
    return  "namda"
###put flights
@app.route('/flight/put/<int:x>', methods = ['PUT'])
def put_flight(x):
     conn, cursor = SQL_connect.Dbinit()
     par = ""
     cursor = SQL_connect.put_flight(cursor,x)
     for row in crusor:
         z = str(row)
         par = z + par
     SQL_connect.close_sql(conn)
     return par
#delete flights
@app.route('/flights/delete/<int:x>', methods = ['DELETE'])
def delete_flight_f(x):
    conn, cursor = SQL_connect.Dbinit()
    cursor =SQL_connect.delete_flight(cursor, x)
    SQL_connect.close_sql(conn)
    return "done"

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
@app.route('/tickets/get/<int:x>', methods = ['GET'])#לא בדקתי עדיין
def get_t_id():
    conn, cursor = SQL_connect.Dbinit()
    par = ""
    cursor = SQL_connect.get_tickets_id(cursor,x)
    for row in cursor:
        z = str(row)
        par = z + par
    SQL_connect.close_sql(conn)
    return par
@app.route('/tickets/post', methods = ['POST'])#לא בדקתי עדיין
def post_t():
    conn, cursor = SQL_connect.Dbinit()
    par = ""
    userID = request.form['User Id']
    flightID = request.form['flight Id']
    cursor = SQL_connect.post_tickets_sql(cursor,userID,flightID)
    for row in cursor:
        z = str(row)
        par = z + par
    SQL_connect.close_sql(conn)
    return par
#DELETE TICKET
@app.route('/tickets/delete/<int:x>', methods = ['DELETE'])
def ticket_delete_f(x):
    conn, cursor = SQL_connect.Dbinit()
    cursor =SQL_connect.delete_ticket(cursor, x)
    SQL_connect.close_sql(conn)
    return "deleted"
app.run()
