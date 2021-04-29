import bs4 as bs
import urllib.request
import re
import nltk
from gensim.models import Word2Vec, KeyedVectors 


nltk.download('punkt')
nltk.download('stopwords')

# getting tokens
# keywords = ['router', 'device', 'responsible', 'routing', 'forwarding']
# keywords = ['set', 'device', 'connected', 'physical', 'medium']

#keywords = ['application', 'layer', 'transport', 'network', 'internet', 'data', 'link']

def computeStrength(keywords,qwords):

    model = KeyedVectors.load('models.kv')

    for keyword in keywords:
        if keyword in model.wv.key_to_index:
            print(keyword," present in model")
        else:
            print(keyword," not present")
    #building wiki model
    # article_text = ""

    # for keyword in keywords:
    #     scrapped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/' + keyword)
    #     article = scrapped_data .read()

    #     parsed_article = bs.BeautifulSoup(article,'lxml')

    #     paragraphs = parsed_article.find_all('p')

    #     for p in paragraphs:
    #         article_text += p.text


    # scrapped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/TCP/IP')
    # article = scrapped_data .read()

    # parsed_article = bs.BeautifulSoup(article,'lxml')

    # paragraphs = parsed_article.find_all('p')
    # for p in paragraphs:
    #     article_text += p.text


    # ### preprocessing data for text data
    # processed_article = article_text.lower()
    # processed_article = re.sub('[^a-zA-Z]', ' ', processed_article )
    # processed_article = re.sub(r'\s+', ' ', processed_article)

    # # Preparing the dataset
    # all_sentences = nltk.sent_tokenize(processed_article)

    # all_words = [nltk.word_tokenize(sent) for sent in all_sentences]

    # from nltk.corpus import stopwords
    # for i in range(len(all_words)):
    #     all_words[i] = [w for w in all_words[i] if w not in stopwords.words('english')]



    # word2vec = Word2Vec(all_words, min_count=1, vector_size = 30,)
    # vocabulary = word2vec.wv.key_to_index
    # #print(vocabulary.keys())
    # print("-----------------------------------\n")

    # ### testing
    # # v1 = word2vec.wv['artificial']


    # print(word2vec.wv.most_similar( 'model'))
    
   

    strength = [0]*len(keywords)
    i = 0

    for keyword in keywords:
        if keyword in model.wv.key_to_index:
            print(keyword + "->" + str(model.wv.similarity(keyword,qwords)))
            strength[i] = abs(model.wv.similarity(keyword,qwords))
        else:
            print(keyword," not present")
        
        i+=1

    print(strength)
    return strength



    # print('Router ->' + str(word2vec.wv.similarity("router","router")))
    # print('device ->' + str(word2vec.wv.similarity("device","router")))
    # print('responsible ->' + str(word2vec.wv.similarity("responsible", "router")))
    # print('routing ->' + str(word2vec.wv.similarity("routing", "router")))
    # print('forwarding ->' + str(word2vec.wv.similarity("forwarding", "router")))


    # word2vec.wv.doesnt_match(["america","europe","floor"])