from utils import *
from BrillsTagger import BillsTagger


corpus = load_text('NLP6320_POSTaggedTrainingSet.txt')

tagger = BillsTagger()
tagger.learn(corpus)

res = tagger.apply('The standard Turbo engine is hard to work')
print(res)
