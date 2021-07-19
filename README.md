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

# Generating Routes/Views

To generate Routes and Views, flask provides an interface that is easy to work with
We generate simple routes by using the app.routes() method

In `routes.py` we can see we have defined a basic route to display hello world
If we run the application, we will now see `Hello, world` displayed

# Adding templates and Views

In the folder app, add a folder called templates

In the templates folder, add a file called index.html

In the templates we will load the sample HTML File

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <title>Retailer App</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
  </head>
  <body>
    <h1>Hello, {{name}}</h1>
  </body>
</html>
```

In our python code, having

```@app.route("/")
def index():
    return render_template("index.html", name="Cloverdale Robotics")
```

We should be able to `{{name}}` getting replaced with the appropriate value for name

# Now lets get started setting up our admin interface

We will update our index.html to look like below

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <title>Vancouver Retailer</title>
    <meta name="viewport" content="width=device-width" />
    <link
      rel="stylesheet"
      href="{{ url_for('static', filename='stylesheets/styles.css') }}"
    />
  </head>
  <body>
    <section class="congratulations">
      <h3>ABC Equipment Rentals</h3>
      <p>Equipment Rental Services</p>
    </section>

    <section class="instructions">
      <form action="{{ url_for('menu') }}" method="POST">
        <input
          type="text"
          name="username"
          placeholder="Username"
          maxlength="10"
          required
        />
        <br />
        <input
          type="password"
          name="password"
          placeholder="Password"
          maxlength="10"
          required
        />
        <input type="hidden" name="form_submitted" value="1" />
        <input type="submit" value="Log In" class="signin" />
      </form>
      <div>
        <p style="color: red">{{msg}}</p>
      </div>
    </section>
  </body>
</html>

```

Don't be worried about what the html does, our focus for this class is not html, but rather on the python concepts and ideas

A Static folder will be provided for you, and will contain all the styles needed for our webpage.
