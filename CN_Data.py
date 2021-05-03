from gensim.models import Word2Vec, KeyedVectors 

model = KeyedVectors.load('models.kv')

m = KeyedVectors.load('models_large.kv')

# dataset 2.6 lakh lines. 16 lakh words

print(model.wv.most_similar(positive=['router',],))

print(m.wv.most_similar(positive=['router',],))

