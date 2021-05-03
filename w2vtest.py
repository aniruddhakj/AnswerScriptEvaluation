import re
import nltk
from gensim.models import Word2Vec, KeyedVectors 

nltk.download('punkt')
nltk.download('stopwords')

text = ""
f = open('cn1.txt')
for line in f:
    text += line

f1 = open('cn2.txt')
for line in f1:
    text += line

f2 = open('cn3.txt')
for line in f2:
    text += line

f3 = open('cn4.txt')
for line in f3:
    text += line

f4 = open('cn5.txt')
for line in f4:
    text += line

f5 = open('cn6.txt')
for line in f5:
    text += line


processed_article = text.lower()
processed_article = re.sub('[^a-zA-Z]', ' ', processed_article )
processed_article = re.sub(r'\s+', ' ', processed_article)

print(len(text.split(' ')))

# Preparing the dataset
# all_sentences = nltk.sent_tokenize(processed_article)

# all_words = [nltk.word_tokenize(sent) for sent in all_sentences]

# from nltk.corpus import stopwords
# for i in range(len(all_words)):
#     all_words[i] = [w for w in all_words[i] if w not in stopwords.words('english')]



# print(len(all_words))






# word2vec = Word2Vec(all_words, min_count=1, vector_size = 700 , epochs = 100)
# vocabulary = word2vec.wv.key_to_index
# print(len(vocabulary.keys()))

# word2vec.save('models_large.kv')
 
    
# # #     print(b)
# # # model = gensim.models.Word2Vec([b],min_count=1,vector_size=32)


# # # w1 = "router"
# # # word2vec.wv.most_similar (positive=w1)

# # print(word2vec.wv.most_similar( 'host'))