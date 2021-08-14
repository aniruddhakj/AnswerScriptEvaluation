''' Generating keyed vectors from textbooks on computer networks.'''

from gensim.models import Word2Vec, KeyedVectors
import numpy as np
import matplotlib.pyplot as plt

from sklearn.manifold import TSNE

model = KeyedVectors.load('models.kv')

m = KeyedVectors.load('models_large.kv')

# dataset has 260K lines. 1.6 million words
