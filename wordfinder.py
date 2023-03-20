"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, path):
        self.path = path

    def random(self):
        file = open(self.path, 'r')

        word = file.read().split()
       
        random_word = random.choice(word)
        print(random_word)

        file.close()