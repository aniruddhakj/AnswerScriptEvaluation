import gensim.downloader as api
word_vectors = api.load("word2vec-google-news-300")  


# king - man + woman
# dataset (about 100 billion words). The model contains 300-dimensional vectors for 3 million words and phrases.

print(word_vectors.most_similar(positive=['woman', 'king'], negative=['man']))



