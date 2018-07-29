from pymongo import MongoClient
from flask import Flask,render_template,request

client = MongoClient('localhost', 27017)
app=Flask(__name__)

db=client['rec_database']                                                       #creted a connection
collection = db.rec_database                                                    #basically to show the type of collection
posts=db.posts

@app.route("/enter_data")
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

@app.route("/",methods=['GET'])
def show_stats()-> 'html' :
    ls=[]
    for post in posts.find():
        ls.append(post)
    return render_template('show_stats.html',ls=ls)

@app.route("/del",methods=['GET','POST'])
def del_data() -> 'html' :
    dl=request.form
    #posts.remove({dl})
    #return render_template('show_stats.html',ls=dl)
    return render_template('chk.html',ps=dl)

@app.route("/delete",methods=['GET','POST'])
def deleted() -> 'html' :
    pl=request.form
    posts.remove({"valname":pl['todel1']}) #{$or: [{"valname":pl['todel1']} , {"valsize":pl['todel2']} , {"valprice":pl['todel3']}]} )
    return render_template('chk.html',delete=pl)

@app.route("/checking")
def checking() -> 'html' :
    p=request.form['h']
    return render_template('check.html',d=p)

'''@app.route("/change",methods=['GET','POST'])
def change() -> 'html' :
    pl=request.form
    render_template('entr_data.html',n1=,n2=,n3=)
'''

@app.route("/enter_updated_data")
def enter_updated_data() -> 'html' :
    ls=[]
    for post in posts.find():
        ls.append(post)
    return render_template("update.html",ls=ls)

@app.route("/update",methods=['GET','POST'])
def update() -> 'html' :
    pr1=request.form['browser']
    pr2=request.form['toup2']
    posts.update_one(
        {"valname" : pr1},
        {
        "$set":{
            "valprice":pr2
        }
        }
    )
    ls=[]
    for post in posts.find():
        ls.append(post)
    return render_template('show_stats.html',ls=ls)

@app.route("/see",methods=['GET','POST'])
def see() -> 'html' :
    return render_template('search.html')

@app.route("/search",methods=['GET','POST'])
def search() ->'html' :
    ab=request.form["say"]
    return render_template('check.html',d=ab)

app.run(debug=True)
