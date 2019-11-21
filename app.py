""" TODO
* Mark start(green) and top (red). Holds blue
* save
    * login
    * register
* load
"""

from flask import Flask, render_template
from find_rects import update_flask
app = Flask(__name__)

@app.route('/')
def hello():
    coords = update_flask()
    return render_template("index.html", coords=coords, width=3000, height=4000, scale=0.25, scalefix=0)

if __name__ == '__main__':
    app.run(debug=True)