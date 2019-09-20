from utils import *
from collections import Counter


class NoSmoothing:
    def __init__(self, corpus=None):
        self.words = None
        self.word_size = 0

        if corpus:
            self.learn(corpus)

    def learn(self, corpus):
        self.words = word_count(corpus)
        self.word_size = sum(self.words.values())

    def p(self, word):
        return self.words.get(word, 0) / self.word_size

    def count(self, word):
        return self.words.get(word, 0)


class AddOne:
    def __init__(self, corpus=None):
        self.words = None
        self.word_size = 0

        if corpus:
            self.learn(corpus)

    def learn(self, corpus):
        self.words = word_count(corpus)
        self.word_size = sum(self.words.values())

    def p(self, word):
        return (self.words.get(word, 0) + 1) / (self.word_size + len(self.words))

    def count(self, word):
        return self.p(word) * self.word_size


class GoodTuring:
    def __init__(self, corpus=None):
        self.words = None
        self.word_size = 0
        self.c_ = None

        if corpus:
            self.learn(corpus)

    def learn(self, corpus):
        self.words = word_count(corpus)
        self.word_size = sum(self.words.values())
        token_size = len(self.words)

        n = Counter()
        for word, count in self.words.items():
            n[count] += 1
        n[0] = 15000 - token_size

        self.c_ = Counter()
        for c in n:
            self.c_[c] = (c + 1) * n[c + 1] / n[c]

    def p(self, word):
        return self.c_[self.words.get(word, 0)] * self.word_size

    def count(self, word):
        return self.c_[self.words.get(word, 0)]
