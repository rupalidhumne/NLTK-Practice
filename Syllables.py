import nltk
from nltk.corpus import cmudict
def guess_syllables(text):
    lowercase = [w.lower() for w in text]
    entries = nltk.corpus.cmudict.entries()
    arpabet_vowels = ['AO', 'AA', 'IY', 'UW', 'EH', 'IH', 'UH', 'AH', 'AX', 'AE', 'EY', 'AY', 'OW', 'AW', 'OY', 'ER']
    english_vowels = ['a', 'e', 'i', 'o', 'u']
    words = []
    prons = []
    idx = 0
    count = 0

    for word, pron in entries:
        words.append(word)
        prons.append(pron)

    for word in lowercase:
        if word in words:
            idx = words.index(word) 
            for vowel in arpabet_vowels:
                for pron in prons[idx]:
                    if vowel in pron:
                        count = count + 1
        else:
            for vowel in english_vowels:
                count = count + word.count(vowel)

    return count

emma = nltk.corpus.inaugural.words('1789-Washington.txt')
c=guess_syllables(emma)
print(str(c))
