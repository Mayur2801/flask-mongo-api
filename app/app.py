from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# Connect to MongoDB using environment variable
mongo_host = os.environ.get("MONGO_HOST", "mongo")
client = MongoClient(f"mongodb://{mongo_host}:27017/")
db = client['mydatabase']
collection = db['test']

@app.route('/')
def home():
    return jsonify({"message": "Flask API is running with MongoDB"})

@app.route('/data')
def get_data():
    items = list(collection.find({}, {"_id": 0}))
    return jsonify(items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
