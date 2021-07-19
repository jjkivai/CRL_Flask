import re
from flask import render_template
from app import app

@app.route("/")
def index():
    return render_template("index.html", name="Cloverdale Robotics")

@app.route("/menu", methods= ["GET", "POST"])
def menu():
    pass