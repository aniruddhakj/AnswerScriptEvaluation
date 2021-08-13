import bs4 as bs
import urllib.request
import re
import nltk
from gensim.models import Word2Vec, KeyedVectors


nltk.download('punkt')
nltk.download('stopwords')


def check_miss(strength, keywords, qwords):
    # scrapping data from wikipidea in case keyword is not present in the model
    flag = True

    for i in strength:
        if (i == 0):
            flag = False
            break
    if(flag):
        return strength

    try:
        article_text = ""
        for keyword in keywords:
            scrapped_data = urllib.request.urlopen(
                'https://en.wikipedia.org/wiki/' + keyword)
            article = scrapped_data .read()
            parsed_article = bs.BeautifulSoup(article, 'lxml')
            paragraphs = parsed_article.find_all('p')
            for p in paragraphs:
                article_text += p.text
        scrapped_data = urllib.request.urlopen(
            'https://en.wikipedia.org/wiki/' + qwords)
        article = scrapped_data .read()
        parsed_article = bs.BeautifulSoup(article, 'lxml')
        paragraphs = parsed_article.find_all('p')
        for p in paragraphs:
            article_text += p.text
        # preprocessing data for text data
        processed_article = article_text.lower()
        processed_article = re.sub('[^a-zA-Z]', ' ', processed_article)
        processed_article = re.sub(r'\s+', ' ', processed_article)
        # Preparing the dataset
        all_sentences = nltk.sent_tokenize(processed_article)
        all_words = [nltk.word_tokenize(sent) for sent in all_sentences]
        from nltk.corpus import stopwords
        for i in range(len(all_words)):
            all_words[i] = [w for w in all_words[i]
                            if w not in stopwords.words('english')]
        word2vec = Word2Vec(all_words, min_count=1, vector_size=30)
        for i in range(0, len(strength)):
            if (strength[i] == 0):
                strength[i] = abs(word2vec.wv.similarity(keywords[i], qwords))
        return strength
    except:
        print("ERROR")
        return strength


def computeStrength(keywords, qwords):
    '''computes the strength value for the answer given the keywords and the qwords'''

    model = KeyedVectors.load('models.kv')
    large_model = Word2Vec.load('models_large.kv')

    strength = [0]*len(keywords)
    i = 0

    for keyword in keywords:
        if keyword in model.wv.key_to_index:
            print(keyword + "->" + str(model.wv.similarity(keyword, qwords)))
            strength[i] = abs(model.wv.similarity(keyword, qwords))
        else:
            print(keyword, " not present")
            if keyword in model.wv.key_to_index:
                strength[i] = abs(large_model.wv.similarity(keyword, qwords))
            else:
                strength[i] = 0
        i += 1

    strength = check_miss(strength, keywords, qwords)

    print(strength)
    return strength
