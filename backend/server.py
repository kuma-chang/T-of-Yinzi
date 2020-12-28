"""This is the backend for T-of-Yinzi"""
import pymongo
from pymongo import MongoClient
import config


cluster = MongoClient(config.ATLAS_URI)
db = cluster["t-of-yinzi"]
collection = db["test"]

post1 = {"_id": 0, "name": "yinzi"}

collection.insert(post1)
