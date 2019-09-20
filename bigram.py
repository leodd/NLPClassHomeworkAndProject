from utils import *
from collections import Counter


def compute_bigram(s, smoothing=None, is_count=False):
    if smoothing == 'add-one':
        return compute_bigram_add_one(s, is_count)
    elif smoothing == 'good-turing':
        return compute_bigram_good_turing(s, is_count)
    else:
        return compute_bigram_no_smoothing(s, is_count)


def compute_bigram_no_smoothing(s, is_count):
    words = word_count(s)
    bigrams = bigram_count(s)
    size = len(words)

    res = dict()

    for i, condition_word in enumerate(words):
        condition_res = dict()
        condition_size = words[condition_word]

        for word in words:
            if is_count:
                condition_res[word] = bigrams.get((condition_word, word), 0)
            else:
                condition_res[word] = bigrams.get((condition_word, word), 0) / condition_size
        res[condition_word] = condition_res

        if i % 100 == 0:
            print(i, '/', size)

    return res


def compute_bigram_add_one(s, is_count):
    words = word_count(s)
    bigrams = bigram_count(s)
    size = len(words)

    res = dict()

    for i, condition_word in enumerate(words):
        condition_res = dict()
        condition_size = words[condition_word]

        for word in words:
            if is_count:
                condition_res[word] = (bigrams.get((condition_word, word), 0) + 1) * condition_size \
                                      / (condition_size + size)
            else:
                condition_res[word] = (bigrams.get((condition_word, word), 0) + 1) / (condition_size + size)
        res[condition_word] = condition_res

        if i % 100 == 0:
            print(i, '/', size)

    return res


def compute_bigram_good_turing(s, is_count):
    words = word_count(s)
    bigrams = bigram_count(s)
    size = len(words)

    res = dict()

    for i, condition_word in enumerate(words):
        condition_res = dict()
        condition_size = words[condition_word]

        n = Counter()

        for word in words:
            n[bigrams.get((condition_word, word), 0)] += 1

        c_ = Counter()
        for c in n:
            c_[c] = (c + 1) * n[c + 1] / n[c]

        for word in words:
            if is_count:
                condition_res[word] = c_[bigrams.get((condition_word, word), 0)]
            else:
                condition_res[word] = c_[bigrams.get((condition_word, word), 0)] / condition_size
        res[condition_word] = condition_res

        if i % 100 == 0:
            print(i, '/', size)

    return res

