"""Move out any repeated snippets to avoid DRY."""

import random
import os


class CreateTemp:
    """Temporarily create a file with a rnadom name in your chosen directory."""

    def __init__(self, dir='tmp'):
        """Save down the temp file and location."""
        self.file = None
        self.dir = dir

    def mkfile(self, extension):
        """Make a temporary file which will soon be deleted."""
        if not os.path.isdir(self.dir):
            os.mkdir(self.dir)
        file = f'./{self.dir}/{random.randint(0,1000000)}.{extension}'
        self.file = file
        return file

    def rmfile(self):
        """Remove the file you've made."""
        if self.file:
            os.remove(self.file)


def dir_walk(path):
    """Do a walk of a dir and return a random obj from it."""
    return [os.path.join(root, name) for root, _, files in os.walk(path) for name in files]


def random_colour():
    """Return a random colour from a list"""
    return (random.choice(range(266)), random.choice(range(266)), random.choice(range(266)))
