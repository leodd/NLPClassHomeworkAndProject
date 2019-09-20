from utils import *
from collections import Counter


class NoSmoothing:
    def __init__(self, corpus=None):
        self.bigrams = None
        self.words = None

        if corpus:
            self.learn(corpus)

    def learn(self, corpus):
        self.bigrams = bigram_count(corpus)
        self.words = word_count(corpus)

    def p(self, conditional_word, word):
        if conditional_word in self.words:
            return self.bigrams.get((conditional_word, word), 0) / self.words[conditional_word]
        else:
            return 0

    def count(self, conditional_word, word):
        return self.p(conditional_word, word) * self.words.get(conditional_word, 0)


class AddOne:
    def __init__(self, corpus=None):
        self.bigrams = None
        self.words = None

        if corpus:
            self.learn(corpus)

    def learn(self, corpus):
        self.bigrams = bigram_count(corpus)
        self.words = word_count(corpus)

    def p(self, conditional_word, word):
        if conditional_word in self.words:
            return (self.bigrams.get((conditional_word, word), 0) + 1) / (self.words[conditional_word] + len(self.words))
        else:
            return 0

    def count(self, conditional_word, word):
        return self.p(conditional_word, word) * self.words.get(conditional_word, 0)


class GoodTuring:
    def __init__(self, corpus=None):
        self.bigrams = None
        self.words = None
        self.c_ = None

        if corpus:
            self.learn(corpus)

    def learn(self, corpus):
        self.bigrams = bigram_count(corpus)
        self.words = word_count(corpus)
        token_size = len(self.words)

        n = dict()
        for (conditional_word, word), join_count in self.bigrams.items():
            conditional_n = n.get(conditional_word, Counter({0: token_size}))
            conditional_n[join_count] += 1
            conditional_n[0] -= 1
            n[conditional_word] = conditional_n

        self.c_ = dict()
        for conditional_word, conditional_n in n.items():
            conditional_c_ = Counter()
            for c in conditional_n:
                conditional_c_[c] = (c + 1) * conditional_n[c + 1] / conditional_n[c]
            self.c_[conditional_word] = conditional_c_

    def p(self, conditional_word, word):
        if conditional_word in self.words:
            return self.c_[conditional_word][self.bigrams.get((conditional_word, word), 0)] / \
                   self.words[conditional_word]
        else:
            return 0

    def count(self, conditional_word, word):
        return self.p(conditional_word, word) * self.words.get(conditional_word, 0)
