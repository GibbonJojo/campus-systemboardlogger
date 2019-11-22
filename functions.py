from flask import session, redirect, url_for, flash
from find_rects import update_flask
from functools import wraps


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("Not logged in")
            return redirect(url_for('index'))

    return wrap


class Rectangles:
    def __init__(self):
        self.coordinates = update_flask()

    def update_coordinates(self):
        self.coordinates = update_flask()