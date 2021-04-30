import gensim.downloader as api
word_vectors = api.load("word2vec-google-news-300")  # load pre-trained word-vectors from gensim-data
# Check the "most similar words", using the default "cosine similarity" measure.
result = word_vectors.most_similar(positive=['woman', 'king'], negative=['man'])

print(result)

# most_similar_key, similarity = result[0]  # look at the first match
# print(f"{most_similar_key}: {similarity:.4f}")

# print(word_vectors.most_similar(positive=['internet']))