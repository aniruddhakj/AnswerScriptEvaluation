from gensim.models import Word2Vec, KeyedVectors 

model = KeyedVectors.load('models.kv')

print(model.wv.most_similar(positive=['network'], ))

