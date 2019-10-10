from flask import Blueprint
from extensions import sqlite

api_experiment = Blueprint("experiment", __name__)

conn = sqlite.get_db()


@api_experiment.route("/")
def home():
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    rows = cur.fetchall()

    for row in rows:
        print(row)
        
    return "success"