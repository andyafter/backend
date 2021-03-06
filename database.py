from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class HashtagPairs(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    __tablename__ = 'HashTagsPairs'
    #id = db.Column(db.Integer, primary_key=True)
    tagpair = db.Column(db.String(120),primary_key=True)
    count= db.Column(db.Integer)
    positive= db.Column(db.Integer)
    negative= db.Column(db.Integer)
    neutral= db.Column(db.Integer)
    def __init__(self, tagpair, count,positive,negative,neutral):
        self.tagpair = tagpair
        self.count = count
        self.positive = positive
        self.negative = negative
        self.neutral = neutral

    def __repr__(self):
        return '<Tagpair %r>' % self.tagpair
    
    # positive negative nutral
    

#"http://172.23.195.172/add/#test,#data|10|8|2|0"
