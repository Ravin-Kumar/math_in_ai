import numpy as np
import random


def read_passage(path):
    with open(path, 'r') as passage:
        passage_text = passage.read()
    return passage_text

def parse_text(text):
    phrases = []
    for i in range(len(text)):
        phrases.append(text[i:i+3])

class TransitionMatrix():

    def __init__(self, text):

        num_words = len(set(' '.split(text)))
        matrix = np.zeros((num_words, num_words))
