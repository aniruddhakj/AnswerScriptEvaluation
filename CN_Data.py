from gensim.models import Word2Vec, KeyedVectors 
import numpy as np
import matplotlib.pyplot as plt
 
from sklearn.manifold import TSNE

def tsne_plot(model):
    "Creates and TSNE model and plots it"
    labels = []
    tokens = []

    for word in model.wv.key_to_index:
        tokens.append(model.wv[word])
        labels.append(word)
    
    tsne_model = TSNE(perplexity=40, n_components=2, init='pca', n_iter=2500, random_state=23)
    new_values = tsne_model.fit_transform(tokens)

    x = []
    y = []
    for value in new_values:
        x.append(value[0])
        y.append(value[1])
        
    plt.figure(figsize=(16, 16)) 
    for i in range(len(x)):
        plt.scatter(x[i],y[i])
        plt.annotate(labels[i],
                     xy=(x[i], y[i]),
                     xytext=(5, 2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')
    plt.show()

 

model = KeyedVectors.load('models.kv')

m = KeyedVectors.load('models_large.kv')

# dataset 2.6 lakh lines. 16 lakh words

print(model.wv.most_similar(positive=['router',],))

print(m.wv.most_similar(positive=['router',],))

tsne_plot(model)




