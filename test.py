from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from database import *

f = open("testdata","r")


while True:
    t = f.readline().split()
    # count:   neg:  pos:  neu:
    if not t:
        break
    tags = t[0]
    count = int(t[1][6:])
    neg = int(t[2][4:])
    pos = int(t[3][4:])
    neu = int(t[4][4:])
    temp = HashtagPairs(tags,count,neg,pos,neu)
    #print tags, count, neg, pos, neu
    db.session.add(temp)
    db.session.commit()
    
    

f.close()


a = HashtagPairs.query.all()
print a
