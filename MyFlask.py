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
    return render_template("Home.html")
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
@app.route('/delete', methods = ['GET','DELETE'])
# def delete_user(x):
def delete_user():
     conn, cursor = SQL_connect.Dbinit()
     par = ""
     cursor = SQL_connect.delete_user(x, cursor)
     for row in crusor:
         z = str(row)
         par = z + par
     SQL_connect.close_sql(conn)
     return par

@app.route('/put/<int x>/<str name>', methods = ['PUT'])
def put_user(x,name):
     conn, cursor = SQL_connect.Dbinit()
     par = ""
     cursor = SQL_connect.put_user(x, cursor,name)
     for row in crusor:
         z = str(row)
         par = z + par
     SQL_connect.close_sql(conn)
     return par
app.run()
