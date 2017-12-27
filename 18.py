import nltk
from nltk.corpus import stopwords
	
def freq_non_stopwords(text):
	stopwords = nltk.corpus.stopwords.words('english')
	clean_list = [w for w in text if w.lower() not in stopwords] 
	freqdist = nltk.probability.FreqDist(clean_list)
	return freqdist.keys()[:50] 


emma = nltk.corpus.gutenberg.words('austen-emma.txt')
L=freq_non_stopwords(emma)
print(str(L))
