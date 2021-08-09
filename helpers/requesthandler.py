from flask import Flask
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

app = Flask(__name__)

mysql = MySQL(
    app,
    prefix="my_database",
    host="localhost",
    user="jjkivai",
    password="jjkivai",
    db="rental",
    autocommit=True,
)


def getallrequest(username):

    try:
        cur = mysql.get_db().cursor(DictCursor)
        cur.execute(
            "select ur.UserName, rr.requestID, rr.requestedDate, rr.EquipmentID, rr.Quantity, rr.status, eq.Name, eq.SKU from rentalrequests rr, users ur,equipment eq where ur.UserName = %s and ur.userID=rr.requestedBy and eq.equipmentID=rr.equipmentID",
            username,
        )

        rentalrequests = cur.fetchall()
        print("rentalrequests ", rentalrequests)
        cur.close()
        return rentalrequests
    except mysql.get_db().cursor().DatabaseError as e:
        print(e)
        return e


def getallrequests(username: str):
    try:
        cur = mysql.get_db().cursor(DictCursor)
        # select  rentalrequests rr, users ur,equipment eq where ur.UserName = %s and ur.userID=rr.requestedBy and eq.equipmentID=rr.equipmentID",username)
        query = (
            "SELECT user.UserName, request.requestID, request.requestedDate, request.EquipmentID, request.Quantity, request.status, equipment.Name, equipment.SKU "
            "FROM users user JOIN rentalrequests AS request ON request.requestedBy=user.userID JOIN equipment ON equipment.equipmentID = request.equipmentID WHERE user.UserName = %s"
        )
        cur.execute(query, (username,))

        rentalrequests = cur.fetchall()
        cur.close()
        return rentalrequests

    except mysql.get_db().cursor().DatabaseError as e:
        print(e)
        return e


def insertrequestdata(details, username):
    try:
        equipmentID = details["EquipmentList"]
        cur = mysql.get_db().cursor(DictCursor)
        cur.execute("select userid from users where username=%s", (username,))
        useridlist = cur.fetchone()
        userid = useridlist["userid"]
        print("userid")
        print(userid)
        cur.execute(
            "INSERT INTO rentalrequests(requestedDate,requestedBy,EquipmentID,Quantity,Status) values (NOW(),%s,%s,%s,%s)",
            (userid, equipmentID, 1, "Inprogress"),
        )
        mysql.get_db().commit()
        cur.close()
        return "Request successfully submitted"
    except mysql.get_db().cursor().DatabaseError as e:
        print(e)
        return e
