"""Play around with pillow.Image!"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path


def generate_postcard(in_path, out_path, crop=None, width=None):
    """Create a Postcard With a Text Greeting

    Arguments:
        in_path {str} -- the file location for the input image.
        out_path {str} -- the desired location for the output image.
    Returns:
        str -- the file path to the output image.
    """
    img = Image.open(in_path)

    if crop is not None:
        img = img.crop(crop)

    if width is not None:
        # compare new and old width to get ratio
        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))  # multiply old height by ratio
        # nearest prevents fractions of pixels
        img = img.resize((width, height), Image.NEAREST)

    fnt = ImageFont.truetype('./udacity/web/ephesis.ttf', 30)
    d = ImageDraw.Draw(img) # create a drawing context
    d.multiline_text((200,100), 'tokyo\n    fashioncats!',font=fnt,fill='pink') # d.text otherwise, coords for upper left
    img.save(out_path)
    return out_path


if __name__ == '__main__':
    print(generate_postcard(Path('./udacity/web') / 'tokyfashioncats.jpg',
          Path('./udacity/web') / 'tokyofc.jpg', (150, 90, 600, 350), 400))
