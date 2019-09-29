from utils import *
import unigram
import bigram


corpus = load_text('NLP6320_POSTaggedTrainingSet.txt')

uni = unigram.GoodTuring(corpus)
bi = bigram.GoodTuring(corpus)

sentence_probability('The standard Turbo engine is hard to work', uni, bi)
