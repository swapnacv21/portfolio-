from flask import Flask,render_template,request
import sqlite3

app = Flask(__name__)


@app.route('/')
def fun():
    return render_template('index.html')

app.run()