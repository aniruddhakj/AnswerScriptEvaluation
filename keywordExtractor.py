# importing libraries
import json
from nltk import tokenize
from operator import itemgetter
from math import log
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def QuestionMatch(examQuestion):
    '''Returns the model answer from the question bank'''
    with open ("QandAConverted.json") as jsonFile:
        filedata = json.load(jsonFile)

    for ele in filedata['data']:
        if ele['Question'] == examQuestion:
            modelAnswer = ele[' Answer']
    jsonFile.close()
    return modelAnswer

def get_top_n(dict_elem, n):
    '''gets the top n keywords from a dictionary element'''
    result = dict(sorted(dict_elem.items(), key = itemgetter(1), reverse = True)[:n]) 
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
    totalSentences = tokenize.sent_tokenize(modelAnswer);
    totalSentencesCount = len(totalSentences)
    tfScore = {}
    idfScore = {}
    for eachWord in totalWords:
        eachWord = eachWord.replace('.','')
        if eachWord not in stopWords:
            if eachWord in tfScore:
                tfScore[eachWord] += 1
                idfScore[eachWord] = check_sent(eachWord, totalSentences)
            else:
                tfScore[eachWord] = 1
                idfScore[eachWord] = 1
    tfScore.update((x, y/int(totalWordCount)) for x, y in tfScore.items())
    idfScore.update((x, log(int(totalSentencesCount)/y)) for x, y in idfScore.items())
    tF_idF = {key: tfScore[key] * idfScore.get(key, 0) for key in tfScore.keys()}
    return(get_top_n(tF_idF, 5))

#test for a given question passed
print(wordimportance(QuestionMatch("What do you mean by Network?")))
