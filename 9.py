import nltk
sense = nltk.corpus.gutenberg.words('austen-sense.txt')
moby = nltk.corpus.gutenberg.words('melville-moby_dick.txt')

print(str(float(len(sense)) / len(moby)))

sense_sents = nltk.corpus.gutenberg.sents('austen-sense.txt')
print(str(float(len(sense)) / len(sense_sents)))

moby_sents = nltk.corpus.gutenberg.sents('melville-moby_dick.txt')
print(str(float(len(moby)) / len(moby_sents)))

print(len(set(moby)))
print(len(set(sense)))

print(float(len(moby)) / len(set(moby)))
print(float(len(sense)) / len(set(sense)))

moby_text = nltk.text.Text(moby)
sense_text = nltk.text.Text(sense)
moby_text.concordance('late')
sense_text.concordance('late')
