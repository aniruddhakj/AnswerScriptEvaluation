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
    return(get_top_n(tF_idF, 7))

def processAns(student_ans):
    #test for a given question passed
    keywords = list(wordimportance(QuestionMatch("What are the different Layers of TCP/IP Model?")).keys())
    print(keywords)

    presence = [0,0,0,0,0] #same size as keyword


    #ans0 Router is a device responsible for routing and forwarding data between source and destination over the computer network. -> 1.0 [same answer]
    #ans1 -> Router is a device that allows the user to connect to a computer network . It has two key functions namely, forwarding and routing -> 0.8788311303339725
    #ans2 -> A Router is a device that allows users to connect to the internet. It is also used to make a wifi network. -> 0.540156296874736
    #ans3 -> Router is a device that is used to create networks and is responsible for packet forwarding and routing. -> 1.0
    #ans4 -> A Router is used for creating a wifi network that allows us to connect to internet -> 0.38047605496992754
    # hardcoded answer for now
    # student_ans = "A Router is a device that allows users to connect to the internet. It is also used to make a wifi network. "

    i = 0
    j = 0
    for keyword in keywords:
        if(student_ans.find(keyword) >=0):
            presence[i] = 1
            j+=1
        i+=1


    p_weight = j/i

    s_weight = 0


    # strength vec  word to vec
    strength = [0.045215975, 0.13770995, 0.2002548, 0.13610095, 0.41461614]

    sum = 0
    i = 0

    for s in strength:
        sum+= s
        s_weight += s*presence[i] 
        i+=1

    s_weight /= sum

    p_fac = 0.5
    s_fac = 0.5

    contextScore = p_fac*p_weight + s_fac*s_weight

    print("---------------------------------")

    print(contextScore)

#processAns("A network is a group of devices connected to each other through a physical medium ")









