import re
from flask import render_template, request, session
from app import app

from helpers.userhelpers import validateuser, getUserByID


@app.route("/")
def index():
    return render_template("index.html", name="Cloverdale Robotics")


@app.route("/menu", methods=["GET", "POST"])
def menu():
    if request.method == "POST":
        formData = request.form
        user = validateuser(formData)

        if len(user) == 0:
            return render_template(
                "index.html", msg="Please enter correct Username and Password"
            )

        for ID in user:
            roleID = ID["RoleID"]

        if roleID == 1:
            username = session["username"]
            userinfo = getUserByID(username)
            return render_template("admin/menu.html", msg=userinfo)
        elif roleID == 2:
            # Create another page for Super User
            username = session["username"]
            userinfo = getUserByID(username)
            return render_template("admin/menu.html", msg=userinfo)
        elif roleID == 3:
            username = session["username"]
            userinfo = getUserByID(username)
            return render_template("user/usermenu.html", msg=userinfo)
        else:
            return render_template(
                "/index.html", msg="Please enter a correct Username and Password"
            )
    else:
        return render_template("/index.html")


@app.route("/equipment", methods=["GET"])
def equipment():
    return render_template("/admin/equipment.html")
