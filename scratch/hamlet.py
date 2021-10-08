import collections
from pathlib import Path
from pprint import pprint as pp


def count_unique_words(filename):

    def _stripPunctuation(word):
        if not word.isalpha():
            word = [word.strip(letter)
                    for letter in word if not letter.isalpha()][0]
        return word.lower()

    file = Path('.') / filename
    with open(file) as f:
        words = []
        for line in f.readlines():
            words += line.split()
        words = map(_stripPunctuation, words)
    pp(collections.Counter(words).most_common(10))


if __name__ == '__main__':
    count_unique_words("hamlet.txt")
