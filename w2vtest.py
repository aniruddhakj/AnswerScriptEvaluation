import re
import nltk
from gensim.models import Word2Vec

nltk.download('punkt')
nltk.download('stopwords')

text = ""
f = open('Computer Networking.txt')
for line in f:
    text += line

processed_article = text.lower()
processed_article = re.sub('[^a-zA-Z]', ' ', processed_article )
processed_article = re.sub(r'\s+', ' ', processed_article)

# Preparing the dataset
all_sentences = nltk.sent_tokenize(processed_article)

all_words = [nltk.word_tokenize(sent) for sent in all_sentences]

from nltk.corpus import stopwords
for i in range(len(all_words)):
    all_words[i] = [w for w in all_words[i] if w not in stopwords.words('english')]



word2vec = Word2Vec(all_words, min_count=2, vector_size = 300)
vocabulary = word2vec.wv.key_to_index
print(len(vocabulary.keys()))

    
#     print(b)
# model = gensim.models.Word2Vec([b],min_count=1,vector_size=32)


# w1 = "router"
# word2vec.wv.most_similar (positive=w1)

print(word2vec.wv.most_similar( 'hosts'))