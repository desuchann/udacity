"""Main entry point for the online application."""

from helpers import CreateTemp, dir_walk
import random
import os
import requests
from flask import Flask, render_template, abort, request
from engines import MemeEngine
from importer import Ingestor
import webbrowser
from threading import Timer

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = dir_walk('./_data/DogQuotes')

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    imgs = dir_walk("./_data/photos/")

    return quotes, imgs


quotes, imgs=setup()


@ app.route('/')
def meme_rand():
    """Generate a random meme."""
    img=random.choice(imgs)

    quote=random.choice(quotes)
    path=meme.make_meme(img, quote.quote, quote.name)
    return render_template('meme.html', path = path)


@ app.route('/create', methods = ['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@ app.route('/create', methods = ['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url=request.form.get('image_url')
    body=request.form.get('body')
    author=request.form.get('author')
    req=requests.get(image_url)
    if not req:
        abort(404, description = 'Unable to download an image from the supplied URL.')
    tmp=CreateTemp()
    file_name=tmp.mkfile('jpg')
    open(file_name, 'wb').write(req.content)
    path=meme.make_meme(file_name, body, author)
    tmp.rmfile()
    return render_template('meme.html', path = path)


def open_browser():
    """Automatically open your browser."""
    webbrowser.open_new('http://127.0.0.1:5000/')


if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(port = 5000)
