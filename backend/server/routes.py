"""This is the backend for T-of-Yinzi"""
from pymongo import MongoClient
from bson.json_util import dumps
import config


cluster = MongoClient(config.ATLAS_URI)
db = cluster["t-of-yinzi"]
collection = db["test"]

post1 = {"_id": 0, "name": "yinzi"}

def get_all_users():
    all_users = dumps(list(collection.find()))
    print(all_users)
    return all_users

def add_user(user_name):
    add_user_post = {"_id": 7, "name": user_name}
    collection.insert_one(add_user_post)
    return

