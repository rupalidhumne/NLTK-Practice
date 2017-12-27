

import nltk
from nltk.corpus import brown


def multiple(corpus, number):
    fdist = nltk.FreqDist([w.lower() for w in corpus])
    words = [' ']
    for word in fdist:
        if fdist[word] >= number:
            words.append(word)
    return words
w=multiple(brown,3)


