import nltk
from nltk.corpus import cmudict
pron = cmudict.dict()

multi_pronunciation_word_ct = 0
word_ct = 0

for word in pron:
   word_ct += 1
   if len(pron[word]) > 1:
      multi_pronunciation_word_ct += 1

print(str((multi_pronunciation_word_ct)/word_ct))
print(str(word_ct))
