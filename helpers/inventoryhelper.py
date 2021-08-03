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


def getequipments():

    try:
        cur = mysql.get_db().cursor(DictCursor)
        cur.execute("SELECT * FROM EQUIPMENT WHERE quantity >0")
        equipmentlist = cur.fetchall()
        print("equipmentlist ", equipmentlist)
        cur.close()
        return equipmentlist
    except mysql.get_db().cursor().DatabaseError as e:
        print(e)
        return e


def insertequipment(details):

    try:
        EquipmentType = details["EquipmentType"]
        Name = details["Name"]
        SKU = details["SKU"]
        Description = details["Description"]
        AvailableFrom = details["AvailableFrom"]
        Quantity = details["Quantity"]
        EstimatedCost = details["EstimatedCost"]
        cur = mysql.get_db().cursor()
        cur.execute(
            "INSERT INTO equipment(EquipmentType, Name, SKU, Description, AvailableFrom, Quantity, Cost) VALUES (%s, %s,%s,%s,%s,%s,%s)",
            (
                EquipmentType,
                Name,
                SKU,
                Description,
                AvailableFrom,
                Quantity,
                EstimatedCost,
            ),
        )
        mysql.get_db().commit()
        cur.close()
        return "Equipment inserted successfully.."
    except mysql.get_db().cursor().DatabaseError as e:
        print(e)
        return e
