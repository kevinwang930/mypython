# from flask import Flask

# app = Flask(__name__)


# @app.route('/')
# def hello():
#     return 'Hello, World!'
import flaskr
app = flaskr.create_app()

app.run()