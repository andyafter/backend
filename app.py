from flask import Flask
from flask import render_template, request
from flask_bootstrap import *
from flask.ext.sqlalchemy import SQLAlchemy
from database import *


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app

app = create_app()

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/test")
def test():
    #t = HashtagPairs("#test,#data",19,4,15,6)
    #print t
    #db.session.add(t)
    #db.session.commit()
    tags = HashtagPairs.query.all()
    print tags
    return "success"

@app.route("/add/<s>")
def add(s):
    temp = s.split('|')
    t = HashtagPairs(temp[0],int(temp[1]),int(temp[2]),int(temp[3]),int(temp[4]))
    if not int(temp[1])==int(temp[2])+int(temp[3])+int(temp[4]):
        return "count is not equal to the sum of positive negative neutral"
    
    db.session.add(t)
    db.session.commit()
    return "success"

@app.route("/searchbytag/<s>")
def searchByTag():
    # query all tags related, sort them, and return a string
    return "success"

@app.route("/searchbyword/<s>")
def searchByWord():
    # query everything according to the words given, sort them and return a string containing relative information
    return "success"
if __name__ == "__main__":
    app.debug = True
    app.run("0.0.0.0")
