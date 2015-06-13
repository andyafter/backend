# Backend

A backend server for cloud computing project. 

Simple database for data storage of twitter hashtags and NLTK processed words. You will have to have sqlite first before running.

- pip install -r requirements.txt

python app.py

However the template files in this project is not contained inside the flask project so if you want to see the front end result in the template folder you simply install **node.js** and **npm** then:

- npm install http-server -g

# About the API(for teammates only)

To add new tag pair or word-tag pair data you just use this url(IP address depends on the real situation):
- http://127.0.0.1:5000/add/#test,#data|10|8|2|0 (real IP depends on the situation you know it)

To query a specific hashtag or word you simply do things like this:
- http://127.0.0.1:5000/search/%23hashtag_or_word

Note that the above API is only for single hashtag or single word, but a sentence would also be possible and easy with simple modifications inside the flask server and you know how to do it.

Also the **%23** is the escape for **"#"** in url.

# Run server, access in front end.
1. Run flask server
2. Switch to the template directory and: http-server -p 8000
3. Go to chrome and go to 127.0.0.1:8000, in the **Table** there is an input and a search button, happy using them.

And thanks for all the work that my teamates have done, it is actually already cool and amazing to make a hadoop application in such a short time. And I think this functionality is awesome.

# How to configure database
First make sure that you are running in a unix like system(better be macos). Second you need to make sure that sqlite works pretty well. 
Open up IPython in this folder, type:
- from database import *
- db.create_all()
- import test

Noticing that this procedure can only be done once, if you came into some bugs and want to debug, there is somethings in the database that needs to be done first. If you don't mind every time you came across a bug you need to roll back by:
- db.session.rollback()
How ever I am a lazy person so everytime I can't solve the problem with a rollback I simply use the dirty way:
- Change the **__tablename__** in **database.py**

And you are welcome!

