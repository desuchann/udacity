"""Primary meme-making engines."""

import random
from PIL import Image, ImageDraw, ImageFont
from helpers import CreateTemp, random_colour, dir_walk

class QuoteModel:
    """Simple class to hold the quote data."""

    def __init__(self, quote: str, name: str):
        """Hold author name and quote body."""
        self.name = name
        self.quote = quote

    def __repr__(self):
        """Computer-friendly representation of class."""
        return f'{self.name!r} says: "{self.quote!r}"'.replace("'", "")

    def __str__(self):
        """Print out the quote by the author."""
        return f'"{self.quote}" - {self.name}'.replace("'", "")


class MemeEngine:
    """Main meme image parsing."""

    def __init__(self, output_dir):
        """Save down the dir the picture is being output to."""
        self.ouptut = output_dir

    def make_meme(self, img_path, text, author, width=500):
        """Create a Postcard With a Text Greeting."""
        img = Image.open(img_path)

        if img.size[0] != width:
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)
        else:
            height = img.size[1]
        fnt_loc = random.choice(dir_walk(('./_data/fonts')))
        fnt = ImageFont.truetype(fnt_loc, 30)
        d = ImageDraw.Draw(img)
        colour = random_colour()
        x, y = [(0.25)*random.choice(range(x)) for x in (width, height)]
        d.multiline_text((x, y), f'"{text}"\n - {author}',
                         font=fnt, fill=colour)
        pic = CreateTemp(dir=self.ouptut)
        pic_name = pic.mkfile('jpg')
        img.save(pic_name)
        return pic_name
