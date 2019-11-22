""" TODO
* Mark start(green) and top (red). Holds blue
* save
    * login
    * register
* load
* Dont call update_flask() for every callup. Either at startup (name==main) or through some kind of admin panel
"""

from flask import Flask, render_template, url_for, redirect, flash, request, session, jsonify
from flask_pymongo import PyMongo
from find_rects import update_flask
from passlib.hash import sha256_crypt
from functions import login_required, Rectangles
from SECRETS import *

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET
app.config["MONGO_URI"] = MDB_URI
db = PyMongo(app).db

@app.route('/')
def index():
    return render_template("new.html", coords=coords, width=3000, height=4000, scale=0.22)


@app.route('/route/<string:name>')
def route(name):
   route = db.routes.find_one({"name": name})
   return render_template("route.html", route=route, width=3000, height=4000, scale=0.22)


@app.route('/myroutes/')
# @login_required
def myroutes():
   pass


@app.route('/all/')
def all():
    routes = db.routes.find({})
    return render_template("all.html", routes=routes)


@app.route('/search/')
def search():
   pass


@app.route('/new/')
# @login_required
def new():
    return render_template("new.html", coords=coords, width=3000, height=4000, scale=0.22, buttons=["save"])


@app.route('/save/', methods=["POST"])
def save():
    if request.method == "POST":
        req = request.get_json()

        if db.routes.count_documents({"name": req["name"]}) == 0:
            name = req["name"]
            difficulty = req["difficulty"]
            canvasData = req["canvasData"]

            insert_res = db.routes.insert_one({"name": name, "difficulty": difficulty, "canvasData": canvasData})

            return redirect(url_for("index")) #CHANGE TO ROUTE DISPLAY

        else:
            flash("Diesen Namen gibt es bereits")
    else:
        return redirect(url_for("index"))


@app.route('/edit/')
# @login_required
def edit():
   pass


@app.route('/delete/')
def delete():
   pass


@app.route('/profile/')
# @login_required
def profile():
   pass


@app.route('/admin/')
# @login_required
def admin():
   pass


@app.route('/login/', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form['username']
        password = request.form['password']

        userObj = db.users.find_one({"$or": [{"username": user}, {"email": user}]})

        if userObj is not None:
            # password check. Use sha256_crypt
            if sha256_crypt.verify(password, userObj["password"]):
                session['logged_in'] = True
                session['username'] = userObj["username"]
                session['admin'] = userObj['status']['admin']
                print(session['admin'])
                return redirect(url_for("index"))

            else:
                flash("Ungültiger Username oder Passwort")

        else:
            flash("Ungültiger Username oder Passwort")

    return render_template("login.html")


@app.route('/register/', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        if db.users.count_documents({"username": request.form["username"]}) == 0 and db.users.count_documents({"email": request.form["email"]}) == 0:
            user = {
                "username": request.form["username"],
                "email": request.form["email"],
                "password": sha256_crypt.hash(request.form["password"]),
                "settings": {},
                "status": {"admin": "False"},
            }

            insert_res = db.users.insert_one(user)
            return redirect(url_for('index'))

        else:
            flash("Username oder Email gibt es bereits")

    return render_template("register.html")


@app.route('/logout/')
@login_required
def logout():
   session.clear()
   flash("Erfolgreich ausgeloggt")
   return redirect(url_for("index"))


if __name__ == '__main__':
    coords = Rectangles().coordinates
    app.run(debug=True)