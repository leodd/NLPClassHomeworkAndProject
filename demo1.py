from utils import *
from unigram import compute_unigram
from bigram import compute_bigram


corpus = load_text('NLP6320_POSTaggedTrainingSet.txt')

smoothing = 'good-turing'

unigram_model = compute_unigram(corpus, smoothing=smoothing)
bigram_model = compute_bigram(corpus, smoothing=smoothing)

# save_unigram_model('{}.txt'.format(smoothing), unigram_model)
# save_bigram_model('{}.txt'.format(smoothing), bigram_model)

sentence_probability('The standard Turbo engine is hard to work', unigram_model, bigram_model)
