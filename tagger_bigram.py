from utils import *
from collections import Counter


def compute_tag_bigram(corpus, is_count):
    tags = tag_unigram_count(corpus)
    tag_bigrams = tag_bigram_count(corpus)
    size = len(tags)

    res = dict()

    for i, condition_word in enumerate(tags):
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


def compute_word_tag_conditional(corpus, is_count):
    words = word_count(corpus)
    bigrams = bigram_count(corpus)
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


def tag_unigram_count(corpus):
    _, poses = to_words_and_pos(corpus)
    return Counter(poses)


def tag_bigram_count(corpus):
    sentences = to_sentences(corpus)
    bigram = list()

    for sentence in sentences:
        _, poses = to_words_and_pos(sentence)
        for i in range(len(poses) - 1):
            bigram.append(
                (poses[i], poses[i + 1])
            )

    return Counter(bigram)


def word_tag_count(corpus):
    sentences = to_sentences(corpus)
    bigram = list()

    for sentence in sentences:
        words, poses = to_words_and_pos(sentence)
        for i in range(len(words)):
            bigram.append(
                (words[i], words[i + 1])
            )

    return Counter(bigram)
