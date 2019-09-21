from utils import *
from collections import Counter


class BillsTagger:
    def __init__(self):
        self.rules = None
        self.tags = None
        self.most_possible_tag = None

    def learn(self, corpus):
        words, poses_correct = to_words_and_pos(corpus)

        self.tags = set()
        for tag in poses_correct:
            self.tags.add(tag)

        self.compute_most_possible_tag(words, poses_correct)

        sentences = list()
        for line in to_sentences(corpus):
            words, poses_correct = to_words_and_pos(line)

            poses_current = list()
            for word in words:
                poses_current.append(self.most_possible_tag[word])

            sentences.append((words, poses_correct, poses_current))

        self.rules = list()
        while True:
            rule, score = self.get_best_rule(sentences)

            if score <= 0:
                break

            z, from_tag, to_tag = rule
            for words, poses_correct, poses_current in sentences:
                for i in range(1, len(words)):
                    if poses_current[i - 1] == z and poses_current[i] == from_tag:
                        poses_current[i] = to_tag

            self.rules.append(rule)
            print(rule, score)

    def apply(self, s):
        words = s.lower().split()
        poses = list()

        for word in words:
            poses.append(self.most_possible_tag[word])

        for z, from_tag, to_tag in self.rules:
            for i in range(1, len(words)):
                if poses[i - 1] == z and poses[i] == from_tag:
                    poses[i] = to_tag

        res = ''
        words = s.split()
        for word, pos in zip(words, poses):
            res += '{}_{} '.format(word, pos)

        return res

    def compute_most_possible_tag(self, words, poses):
        self.most_possible_tag = dict()
        counter_dict = dict()

        for word, pos in zip(words, poses):
            counter = counter_dict.get(word, Counter())
            counter[pos] += 1
            counter_dict[word] = counter

        for word, counter in counter_dict.items():
            self.most_possible_tag[word] = max(counter.keys(), key=lambda w: counter[w])

    def get_best_rule(self, sentences):
        best_rule = None
        best_score = 0

        for from_tag in self.tags:
            for to_tag in self.tags:
                if from_tag == to_tag:
                    continue

                num_good_transforms = Counter()

                for words, poses_correct, poses_current in sentences:
                    for i in range(1, len(words)):
                        if poses_correct[i] == to_tag and poses_current[i] == from_tag:
                            num_good_transforms[poses_current[i - 1]] += 1
                        elif poses_correct[i] == from_tag and poses_current[i] == from_tag:
                            num_good_transforms[poses_current[i - 1]] -= 1

                if len(num_good_transforms) == 0:
                    continue

                best_z = max(num_good_transforms.keys(), key=lambda z: num_good_transforms[z])
                best_z_score = num_good_transforms[best_z]

                if best_z_score > best_score:
                    best_rule = (best_z, from_tag, to_tag)
                    best_score = best_z_score

        return best_rule, best_score
