import json
from nltk import tokenize
from operator import itemgetter
from math import log
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from w2v import computeStrength
import gensim.downloader as api
from nltk.corpus import stopwords
from grammar import checkGrammar


def QuestionMatch(examQuestion):
    '''Returns the model answer from the question bank'''
    with open("QandAConverted.json") as jsonFile:
        filedata = json.load(jsonFile)

    for ele in filedata['data']:
        if ele['Question'] == examQuestion:
            modelAnswer = ele[' Answer']
    jsonFile.close()
    return modelAnswer


def getQword(question):
    with open("QandAConverted.json") as jsonFile:
        filedata = json.load(jsonFile)

    for ele in filedata['data']:
        if ele['Question'] == question:
            qword = ele['qword']
    jsonFile.close()
    return qword


def get_top_n(dict_elem, n):
    '''gets the top n keywords from a dictionary element'''
    result = dict(sorted(dict_elem.items(),
                  key=itemgetter(1), reverse=True)[:n])
    return result


def check_sent(word, sentences):
    '''Returns the sent words length'''
    final = [all([w in x for w in word]) for x in sentences]
    sent_len = [sentences[i] for i in range(0, len(final)) if final[i]]
    return int(len(sent_len))


def wordimportance(modelAnswer):
    '''Calculates Term Frequency x Inverse Document Frequency'''
    stopWords = set(stopwords.words('english'))
    totalWords = modelAnswer.split()
    totalWordCount = len(totalWords)
    totalSentences = tokenize.sent_tokenize(modelAnswer)
    totalSentencesCount = len(totalSentences)
    tfScore = {}
    idfScore = {}
    for eachWord in totalWords:
        eachWord = eachWord.replace('.', '')
        if eachWord not in stopWords:
            if eachWord in tfScore:
                tfScore[eachWord] += 1
                idfScore[eachWord] = check_sent(eachWord, totalSentences)
            else:
                tfScore[eachWord] = 1
                idfScore[eachWord] = 1
    tfScore.update((x, y/int(totalWordCount)) for x, y in tfScore.items())
    idfScore.update((x, log(int(totalSentencesCount)/y))
                    for x, y in idfScore.items())
    tF_idF = {key: tfScore[key] *
              idfScore.get(key, 0) for key in tfScore.keys()}
    return(get_top_n(tF_idF, 5))


def checkRelavancy(student_ans, keywords):
    '''returns relavancy score by comparing student answer and model'''
    score = 0
    t = 0
    word_vectors = api.load("word2vec-google-news-300")
    l = student_ans.split(" ")
    for word in l:
        if((word in word_vectors.key_to_index) and (word not in stopwords.words('english'))):
            data = word_vectors.most_similar(positive=[word])
            for tup in data:
                if (tup[0].lower() in keywords):
                    t += 1
                    score += tup[1]
    if(t != 0):
        score /= t
    return score


def processAns(question, student_ans, keywords, g_fac, s_fac):
    '''processes answer and returns compute context score'''
    # test for a given question passed
    qwords = getQword(question)
    res = checkGrammar(student_ans)
    errors = len(res[1])
    if (errors < 2):
        penalty = 0
    elif (errors < 5):
        penalty = 0.25
    elif (errors < 8):
        penalty = 0.5
    elif (errors < 10):
        penalty = 0.75
    else:
        penalty = 1

    student_ans = res[0].lower()

    for i in range(0, len(keywords)):
        keywords[i] = keywords[i].lower()
    print(keywords)

    presence = [0]*len(keywords)
    i = 0
    j = 0
    for keyword in keywords:
        if(student_ans.find(keyword) >= 0):
            presence[i] = 1
            j += 1
        i += 1

    p_weight = j/i
    print("p weight is ", p_weight)

    s_weight = 0
    # find strength vector
    strength = computeStrength(keywords, qwords)

    sum = 0
    i = 0

    for s in strength:
        sum += s
        s_weight += s*presence[i]
        i += 1

    s_weight /= sum

    print("strength weight = ", s_weight)

    p_fac = 1 - s_fac

    contextScore = p_fac*p_weight + s_fac*s_weight

    contextScore -= contextScore*penalty*g_fac

    if (contextScore < 0.5):
        relavancy_score = checkRelavancy(student_ans, keywords)
        if (relavancy_score > 0.5):
            contextScore = (contextScore + relavancy_score) / 2
    print(contextScore)

    return contextScore
