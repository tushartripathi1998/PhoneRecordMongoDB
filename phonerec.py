from pymongo import MongoClient
from flask import Flask,render_template,request

client = MongoClient('localhost', 27017)
app=Flask(__name__)

db=client['rec_database']                                                       #creted a connection
collection = db.rec_database                                                    #basically to show the type of collection
posts=db.posts

@app.route("/")
def enterval() -> 'html' :
    return render_template('enter_data.html')

@app.route("/add",methods=["POST"])
def add() -> 'html' :

    name1=request.form["name1"]
    size1=request.form["size1"]
    price1=request.form["price1"]

    post_data= {"valname":name1,"valsize":size1,"valprice":price1}
    lsp=posts.insert_one(post_data)

    return render_template('feed_data.html',lsp=lsp)

@app.route("/stats",methods=['GET','POST'])
def show_stats()-> 'html' :
    ls=[]
    for post in posts.find():
        ls.append(post)
    return render_template('show_stats.html',ls=ls)

app.run(debug=True)
