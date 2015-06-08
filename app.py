from flask import Flask
from flask import render_template, request
from flask_bootstrap import *
from flask.ext.sqlalchemy import SQLAlchemy
from database import *
import operator
import json


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

@app.route("/search/<s>")
def search(s):
    # query all tags related, sort them, and return a string
    # give a query and return a list of tags
    temp = "%"+s+"%"
    a = HashtagPairs.query.filter(HashtagPairs.tagpair.like(temp)).all()
    m = {}  # dictionary for the result output
    mfs = {} # m for sort
    for i in a:
        tags = i.tagpair.split(',')
        if s in tags:
            ## only if there is a string that is exactly equal to s can
            ## you make sure that this tag is useful.
            temp = ""
            if tags[1] == s:
                temp = tags[0]
            else:
                temp = tags[1]
            if temp:
                if temp[0]!= "#":
                    print "not a tag"
                    continue
            if temp not in m:
                m[temp] = {}
                m[temp]["count"] = i.count
                m[temp]["positive"] = i.positive
                m[temp]["negative"] = i.negative
                m[temp]["neutral"] = i.neutral
                mfs[temp] = int(i.count)
            else:
                print "error, duplicate tag pair"

    sor = sorted(mfs.items(), key=operator.itemgetter(1))
    r = []
    for i in sor:
        r.append(i[0])
        print i

    result = json.dumps([m,r[::-1]])            
            
    return result

if __name__ == "__main__":
    app.debug = True
    app.run("0.0.0.0")
