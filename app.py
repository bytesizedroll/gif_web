#!/usr/bin/python3

from flask import Flask, render_template
import json
import random
import requests

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://api.gfycat.com/v1/gfycats/search?search_text=gif"
    req = requests.get(url)

    num_gifs = len(req.json()['gfycats'])
    random_gif = random.randint(0,num_gifs - 1)
    return render_template("index.html", front_gif=req.json()['gfycats'][random_gif]['max1mbGif'])

@app.route('/search')
def search():
    return "THE SEARCH PAGE"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='2424')
