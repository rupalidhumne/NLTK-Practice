
from __future__ import division
import nltk
from nltk.corpus import wordnet as wn

def polysemy(group):
    polysemy = 0
    count = 0
    name = ''

    for synset in wn.all_synsets(group):
        for lemma in synset.lemmas:
            name = lemma.name
            polysemy = polysemy + len(wn.synsets(name, group))
            count = count + 1

    return polysemy / count


