#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import random
import requests

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://api.gfycat.com/v1/gfycats/search?search_text=funny%20cat"
    req = requests.get(url)

    num_gifs = len(req.json()['gfycats'])
    random_gif = random.randint(0,num_gifs - 1)
    return render_template("index.html", front_gif=req.json()['gfycats'][random_gif]['max5mbGif'])

@app.route('/search')
def search():
    if request.args.get('search_string'):
        print(request.args.get('search_string'))
        return render_template("search.html", search_string=request.args.get('search_string'))
    else:
        return render_template("search.html")


@app.route('/trending')
def trending():
    return render_template("trending.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='2424')
