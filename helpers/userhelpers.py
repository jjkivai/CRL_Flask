from pymysql.cursors import DictCursor
from flaskext.mysql import MySQL
from flask import Flask, session
from flask_session import Session

app = Flask(__name__)

app.config.from_object(__name__)
Session(app)

DATABASE_NAME = "rental"

mysql = MySQL(
    app,
    prefix="my_database",
    host="localhost",
    user="jjkivai",
    password="jjkivai",
    db="rental",
    autocommit=True,
)


def validateuser(details):
    try:
        username = details["username"]
        password = details["password"]
        cur = mysql.get_db().cursor(DictCursor)
        print("inside validateuser")
        cur.execute(
            "SELECT RoleID FROM users where username=%s and password=%s",
            (username, password),
        )
        userlist = cur.fetchall()
        print("userlist ", userlist)
        cur.close()
        session["username"] = username
        return userlist
    except mysql.get_db().cursor().DatabaseError as e:
        print(e)
        return e


def getUserByID(username):
    # getUserByID can be combined with validateuser if needed
    try:
        cur = mysql.get_db().cursor(DictCursor)
        cur.execute("SELECT * FROM users where username=%s", username)
        userlist = cur.fetchall()
        print("userlist ", userlist)
        cur.close()
        return userlist
    except mysql.get_db().cursor().DatabaseError as e:
        print(e)
        return e

def getUsers():

    try:
        cur = mysql.get_db().cursor(DictCursor)
        cur.execute("SELECT * FROM users")
        userlist = cur.fetchall()
        print("userlist " ,userlist)
        cur.close()
        return userlist
    except mysql.get_db().cursor().DatabaseError as e:
        print(e)
        return e