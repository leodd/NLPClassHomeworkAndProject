from utils import *
from collections import Counter


def compute_unigram(s, smoothing=None, is_count=False):
    if smoothing == 'add-one':
        return compute_unigram_add_one(s, is_count)
    elif smoothing == 'good-turing':
        return compute_unigram_good_turing(s, is_count)
    else:
        return compute_unigram_no_smoothing(s, is_count)


def compute_unigram_no_smoothing(s, is_count):
    words = word_count(s)
    unigrams = word_count(s)
    word_size = sum(words.values())
    token_size = len(words)

    res = dict()

    for word in words:
        if is_count:
            res[word] = unigrams.get(word, 0)
        else:
            res[word] = unigrams.get(word, 0) / word_size

    return res


def compute_unigram_add_one(s, is_count):
    words = word_count(s)
    unigrams = word_count(s)
    word_size = sum(words.values())
    token_size = len(words)

    res = dict()

    for word in words:
        if is_count:
            res[word] = (unigrams.get(word, 0) + 1) * word_size / (token_size + word_size)
        else:
            res[word] = (unigrams.get(word, 0) + 1) / (token_size + word_size)

    return res


def compute_unigram_good_turing(s, is_count):
    words = word_count(s)
    unigrams = word_count(s)
    word_size = sum(words.values())
    token_size = len(words)

    res = dict()

    n = Counter()

    for word in words:
        n[unigrams.get(word, 0)] += 1

    c_ = Counter()
    for c in n:
        c_[c] = (c + 1) * n[c + 1] / n[c]

    for word in words:
        if is_count:
            res[word] = c_[unigrams.get(word, 0)]
        else:
            res[word] = c_[unigrams.get(word, 0)] / word_size

    return res
