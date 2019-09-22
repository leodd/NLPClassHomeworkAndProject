from utils import *
from tagger_bigram import *


corpus = load_text('NLP6320_POSTaggedTrainingSet.txt')

tag_tag = compute_tag_bigram(corpus)
word_tag = compute_word_tag_conditional(corpus)

print(tag_tag)
print(word_tag)


best_tag = None
best_p = 0
for tag in ['NN', 'JJ']:
    p = tag_tag['DT'].get(tag, 0) * tag_tag[tag].get('NN', 0) * word_tag[tag].get('standard', 0)
    print(tag_tag['DT'].get(tag, 0), tag_tag[tag].get('NN', 0), word_tag[tag].get('standard', 0), p)
    if p > best_p:
        best_tag = tag
        best_p = p

print(best_tag, best_p)


best_tag = None
best_p = 0
for tag in ['NN', 'VB']:
    p = tag_tag['TO'].get(tag, 0) * word_tag[tag].get('work', 0)
    print(tag_tag['TO'].get(tag, 0), word_tag[tag].get('work', 0), p)
    if p > best_p:
        best_tag = tag
        best_p = p

print(best_tag, best_p)
