from collections import Counter


def load_text(f):
    with open(f, 'r') as file:
        return file.read()


def save_unigram_model(f, model):
    with open(f, 'w') as file:
        for word, p in model.items():
            file.write('{} {}\n'.format(word, p))


def save_bigram_model(f, model):
    with open(f, 'w') as file:
        word_list = model.keys()
        for condition_word, value_dict in model.items():
            for word in word_list:
                file.write('{} {} {}\n'.format(condition_word, word, value_dict[word]))


def to_sentences(s):
    res = s.splitlines()

    for i in range(len(res)):
        res[i] = res[i].strip()

    return res


def to_words_and_pos(s, lower_case=True):
    units = s.split()
    words = list()
    poses = list()

    for unit in units:
        word, pos = unit.split('_')

        if lower_case:
            word = word.lower()

        words.append(word)
        poses.append(pos)

    return words, poses


def word_count(s):
    words, _ = to_words_and_pos(s)
    return Counter(words)


def bigram_count(s):
    sentences = to_sentences(s)
    bigram = list()

    for sentence in sentences:
        words, _ = to_words_and_pos(sentence)
        for i in range(len(words) - 1):
            bigram.append(
                (words[i], words[i + 1])
            )

    return Counter(bigram)


def sentence_probability(s, unigram, bigram):
    s = s.lower()
    words = s.split()

    if len(words) == 0:
        return 0

    p = unigram.p(words[0])

    print('p( {} ) = {}'.format(words[0], p))
    f = 'p( {} ) '.format(words[0])

    for i in range(1, len(words)):
        w = words[i]
        w_ = words[i - 1]

        pw_w = bigram.p(w_, w)

        print('p( {} | {} ) = {}'.format(w, w_, pw_w))
        f += '* p( {} | {} ) '.format(w, w_)

        p *= pw_w

    print('sentence probability:', f, '=', p)

    return p
