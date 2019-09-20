from utils import *
from collections import Counter


def compute_tag_bigram(corpus, is_count=False):
    tags = tag_unigram_count(corpus)
    tag_bigrams = tag_bigram_count(corpus)

    res = dict()

    for (conditional_tag, tag), join_count in tag_bigrams.items():
        conditional_dict = res.get(conditional_tag, dict())

        if is_count:
            conditional_dict[tag] = join_count
        else:
            conditional_dict[tag] = join_count / tags[conditional_tag]

        res[conditional_tag] = conditional_dict

    return res


def compute_word_tag_conditional(corpus, is_count=False):
    tags = tag_unigram_count(corpus)
    word_tag = word_tag_count(corpus)

    res = dict()

    for (tag, word), join_count in word_tag.items():
        conditional_dict = res.get(tag, dict())

        if is_count:
            conditional_dict[word] = join_count
        else:
            conditional_dict[word] = join_count / tags[tag]

        res[tag] = conditional_dict

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
    word_tag = list()

    for sentence in sentences:
        words, poses = to_words_and_pos(sentence)
        for i in range(len(words)):
            word_tag.append(
                (poses[i], words[i])
            )

    return Counter(word_tag)
