from flask import  Flask
from flask import render_template,request,redirect,url_for
import  sqlite3
con = sqlite3.connect(r'C:\Users\Tomer\OneDrive\Desktop\Devops/final1.db')
app = Flask(__name__)

#function to store new users
def register_user_to_db(username, password,ID):
    con = sqlite3.connect(r'C:\Users\Tomer\OneDrive\Desktop\Devops/final1.db')
    cur = con.cursor()
    cur.execute('INSERT INTO users(full_name,password,real_id) values (?,?,?)', (username, password,ID))
    con.commit()
    con.close()
#FUNCTION THE CHECK IF USERS PUT THE CORRECT INFO
def check_user(username, password,ID):
    con = sqlite3.connect(r'C:\Users\Tomer\OneDrive\Desktop\Devops/final1.db')
    cur = con.cursor()
    cur.execute('Select username,password,real_id FROM users WHERE username=? and password=? and real_id=?', (username, password,ID))

    result = cur.fetchone()
    if result:
        return True
    else:
        return False


#Home PAGE
@app.route('/',methods =['POST','GET'])
def home_page():
    return render_template("Home.html")
#register PAGE
#consider as register for now
def login():
    if request.method == 'GET':
        password = request.form['password']
        full_name = request.form['name']
        ID_FORM = request.form['ID']
        register_user_to_db(username, password,ID)
        conn.commit()
    else:
        return

@app.route('/register',methods =['POST','GET'])
def reg_page():
    return render_template("register.html")

app.run()