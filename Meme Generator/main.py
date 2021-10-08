"""Main CLI for meme generator."""

import argparse
from helpers import dir_walk
import random

from engines import QuoteModel, MemeEngine
from importer import Ingestor


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        img = random.choice(dir_walk("./_data/photos/"))
    else:
        img = path[0]

    if body is None:
        quote_files = dir_walk('./_data/DogQuotes')
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.quote, quote.name)
    return path


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get meme making')
    parser.add_argument('--path', type=str, default=None)
    parser.add_argument('--body', type=str, default=None)
    parser.add_argument('--author', type=str, default=None)

    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
