from utils import *
from collections import Counter


def compute_tag_bigram(corpus, is_count):
    tags = tag_unigram_count(corpus)
    tag_bigrams = tag_bigram_count(corpus)
    size = len(tags)

    res = dict()

    for i, condition_tag in enumerate(tags):
        condition_res = dict()
        condition_size = tags[condition_tag]

        for tag in tags:
            if is_count:
                condition_res[tag] = tag_bigrams.get((condition_tag, tag), 0)
            else:
                condition_res[tag] = tag_bigrams.get((condition_tag, tag), 0) / condition_size
        res[condition_tag] = condition_res

        if i % 100 == 0:
            print(i, '/', size)

    return res


def compute_word_tag_conditional(corpus, is_count):
    tags = tag_unigram_count(corpus)
    word_tag = word_tag_count(corpus)
    size = len(tags)

    res = dict()

    for i, condition_tag in enumerate(tags):
        condition_res = dict()
        condition_size = tags[condition_tag]

        for word in words:
            if is_count:
                condition_res[tag] = word_tag.get((condition_tag, tag), 0)
            else:
                condition_res[tag] = tag_bigrams.get((condition_tag, tag), 0) / condition_size
        res[condition_tag] = condition_res

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
                (poses[i], words[i])
            )

    return Counter(bigram)
