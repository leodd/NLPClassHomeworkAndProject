def most_likely_tagging(sentence, tag_set, tag_tag_conditional, tag_word_conditional):
    words = sentence.split()
    T = len(words)

    viterbi = list()
    backpointer = list()

    # initialization
    viterbi.append(dict())
    for tag in tag_set:
        viterbi[0][tag] = tag_tag_conditional['<s>'][tag] * tag_word_conditional[tag][words[0]]

    # forward
    for t in range(1, T):
        viterbi.append(dict())
        backpointer.append(dict())
        for tag in tag_set:
            temp = dict()
            for prev_tag in tag_set:
                temp[prev_tag] = viterbi[t - 1][prev_tag] * tag_tag_conditional[prev_tag][tag]

            backpointer[-1][tag] = max(temp.keys(), key=lambda x: temp[x])
            viterbi[t][tag] = temp[backpointer[-1][tag]] * tag_word_conditional[tag][words[t]]

    # backtrack
    res = [max(viterbi[-1].keys(), key=lambda x: viterbi[-1][x])]
    for backpointer_dict in reversed(backpointer):
        res.append(backpointer_dict[res[-1]])

    return list(reversed(res))


def probability(sentence, tag_set, tag_tag_conditional, tag_word_conditional):
    words = sentence.split()
    T = len(words)

    viterbi = list()

    # initialization
    viterbi.append(dict())
    for tag in tag_set:
        viterbi[0][tag] = tag_tag_conditional['<s>'][tag] * tag_word_conditional[tag][words[0]]

    # forward
    for t in range(1, T):
        viterbi.append(dict())
        for tag in tag_set:
            temp = 0
            for prev_tag in tag_set:
                temp += viterbi[t - 1][prev_tag] * tag_tag_conditional[prev_tag][tag]

            viterbi[t][tag] = temp * tag_word_conditional[tag][words[t]]

    res = 0
    for tag in tag_set:
        res += viterbi[-1][tag]

    return res
