from pymongo import MongoClient
from passlib.hash import sha256_crypt
from SECRETS import *

def create_db():
    # connect to the client
    client = MongoClient(MDB_URI)

    # create and connect to the coobkook database
    db = client.campuslogger

    # create the Users collection
    db_users = db.users

    # create the Recipe collection
    db_recipes = db.routes

    # create the standard users
    create_user(db_users)


def create_user(db):
    # Will be removed when deploying
    jojo = {"username": "Gibbon",
            "password": "sha256_crypt.hash('admin')",
            "email": "johannes.uttecht@gmail.com",
            "settings": {},
            "status": {"admin": "True"}}

    insert_res = db.insert_one(jojo)
    print(insert_res.acknowledged)


if __name__ == "__main__":
    create_db()