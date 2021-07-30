from flask import Flask

from app.config import Config

app = Flask(__name__)

app.config.from_object(Config)

app.static_folder = "static"


from app import routes
