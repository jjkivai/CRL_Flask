In this tutorial, we learn how to set up a flask environment in order to comply with the requirements and the needs of the file stated in the CPSP Level 2 docx.

So to set up we will start by installing choco, in order to make it easier to download and install packages

Open Start and type in Powershell, right click and run as administrator
Copy and paste Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
Wait for download to finish. If there are no errors, type choco -? and if there are no errors you're good to go
Now we can begin setting up our application. We will start by downloading python and mysql(server which runs database)

Open Powershell(admin mode) and type choco install python and follow instructions to install python (Only if you don't have python)
Type choco install mysql to install mysql
Create a new folder called Retailer, and open in VSCode or pycharm

Create a new virtual environment python -m venv venv Activate your virtual environment venv\scrips\activate

And we're all set to start our coding

To Start Our app, we need to install Flask

In terminal, type `pip install flask`

Create a new folder called app and create a file called `__init__.py`

Inside `__init__.py` we will import flask and get started

Inside `__init__.py` we will do the following

```
    from flask import Flask

    app = Flask(__name__)
```

This initialises a flask app that we can work with

In the same folder as app, create a file called `app.py` and in the file, add `from app import app`

Then in terminal run `flask run`

This should start your flask applicaition
