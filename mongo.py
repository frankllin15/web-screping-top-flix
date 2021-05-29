from flask import Flask, json
from flask import jsonify
from flask import request
from bson.json_util import dumps

from flask.templating import render_template
from flask_pymongo import PyMongo

from screppy import searchEmbed

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'best_films'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/best_films'

mongo = PyMongo(app)
embedCollection = mongo.db.embed

@app.route('/embeds', methods=['GET'])
def get_all_embeds():
    embeds = mongo.db.embed.find()


    return dumps(list(embeds), indent=2)

@app.route('/embeds', methods=['POST'])
def add_embed():
    name = request.json['name']
    url = request.json['url']

    embed_id = mongo.db.embed.insert_one({'name': name, 'url': url})
    new_embed = mongo.db.embed.find_one({'_id': embed_id.inserted_id})
  

    return dumps(new_embed, indent = 2)

@app.route('/embeds/find')
def find_embed():
    name = request.json['name']
    imdb_id = request.json['imdb_id']

    title = embedCollection.find_one({"imdb_id": imdb_id})

    if (title):
        return dumps(title, indent=2)
        print("has Title")

    new_title = searchEmbed(name, "")
    # print(name, id)

    

    embedCollection.insert_one(new_title)

    return dumps(new_title, indent=2)


if __name__ == '__main__':
    app.run(debug=True)

