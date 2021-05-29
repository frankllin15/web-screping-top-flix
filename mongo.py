from flask import Flask, json
from flask import jsonify
from flask import request
from bson.json_util import dumps

from flask.templating import render_template
from flask_pymongo import PyMongo
from pymongo import results
import pymongo
from screppy import searchEmbed

import dns

app = Flask(__name__)

# app.config['MONGO_DBNAME'] = 'best_films'
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/best_films'
# mongodb://localhost:27017/best_films'

mongo = pymongo.MongoClient("mongodb+srv://frank:2Aekl1JyIK6xy2wf@bestfilmscuster.oofs0.mongodb.net/best-films?retryWrites=true&w=majority")
# PyMongo(app)
embedCollection = mongo.db.embed

@app.route('/embeds', methods=['GET'])
def get_all_embeds():
    embeds = embedCollection.find()


    return dumps(list(embeds), indent=2)

@app.route('/embeds', methods=['POST'])
def add_embed():
    name = request.json['name']
    url = request.json['url']

    embed_id = embedCollection.insert_one({'name': name, 'url': url})
    new_embed = embedCollection.find_one({'_id': embed_id.inserted_id})
  

    return dumps(new_embed, indent = 2)

@app.route('/embeds/find')
def find_embed():
    name = request.json['name']
    imdb_id = request.json['imdb_id']

    title = embedCollection.find_one({"imdb_id": imdb_id})

    if (title):
        return dumps(title, indent=2)
        print("has Title")

    # try:
    results = searchEmbed(name)

    for doc in results:
        embedCollection.update_one(filter={"imdb_id": doc['imdb_id']}, update={"$set": doc}, upsert=True)
        print(doc["imdb_id"])
    



    return dumps(results, indent=2), 200 if(results) else 400


if __name__ == '__main__':
    app.run(debug=True)

