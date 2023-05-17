"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi8iqt269vf5qbjchi0-a.oregon-postgres.render.com",
        database="todo_m7m7",
        user="root",
        password="G9jxPSjQpZVDPJNMTm895ae1Qywv6m2v")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
