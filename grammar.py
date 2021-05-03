import language_tool_python
tool = language_tool_python.LanguageTool('en-US')

# Preparing the dataset
# all_sentences = nltk.sent_tokenize(processed_article)

# all_words = [nltk.word_tokenize(sent) for sent in all_sentences]

# from nltk.corpus import stopwords
# for i in range(len(all_words)):
#     all_words[i] = [w for w in all_words[i] if w not in stopwords.words('english')]



# print(len(all_words))






# word2vec = Word2Vec(all_words, min_count=1, vector_size = 700 , epochs = 100)
# vocabulary = word2vec.wv.key_to_index
# print(len(vocabulary.keys()))

# word2vec.save('models_large.kv')
 
    
# # #     print(b)
# # # model = gensim.models.Word2Vec([b],min_count=1,vector_size=32)


# # # w1 = "router"
# # # word2vec.wv.most_similar (positive=w1)

# # print(word2vec.wv.most_similar( 'host'))





def checkGrammar(text):
    matches = tool.check(text)
    for i in matches:
        print(i)
    my_mistakes = []
    my_corrections = []
    start_positions = []
    end_positions = []
    
    for rules in matches:
        if len(rules.replacements)>0:
            start_positions.append(rules.offset)
            end_positions.append(rules.errorLength+rules.offset)
            my_mistakes.append(text[rules.offset:rules.errorLength+rules.offset])
            my_corrections.append(rules.replacements[0])
    my_new_text = list(text)
    
    
    for m in range(len(start_positions)):
        for i in range(len(text)):
            my_new_text[start_positions[m]] = my_corrections[m]
            if (i>start_positions[m] and i<end_positions[m]):
                my_new_text[i]=""
        
    my_new_text = "".join(my_new_text)

    print(my_new_text)
    print(list(zip(my_mistakes,my_corrections)))

    return [my_new_text,my_mistakes]

# checkGrammar("A router is a device that helps us ocnnnect to a wntwork. there are two types of functions for the routers this are routing and forwarding ")

# checkGrammar("""Click the colored phrases for details on potential errors. or use this text too see an few of of the problems that LanguageTool can detecd. What do you thinks of grammar checkers? Please not that they are not perfect. It’s 5 P.M. in the afternoon. The weather was nice on Thursday, 27 June 2017""")
