import streamlit as st
import os,io
# from io import StringIO
from PIL import Image
# from google.cloud import vision_v1
from google.cloud.vision_v1 import types
from keywordExtractor import processAns, QuestionMatch,wordimportance
from google.cloud import vision_v1p3beta1 as vision
    

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'token.json'


client = vision.ImageAnnotatorClient()


def modifyKeywords(keywords,model_answer):
    #need to do
    flag = True
    new_list = []
    item = st.multiselect("Select keywords that you want to remove", keywords, key = '69')
    word = st.text_input('Enter a keyword to insert')
    if(word not in model_answer):
            st.write("Invalid keyword, keyword must be present in the model answer")
    val = st.button("Make changes")
   
        
    

    #  A Router is a device that allows users to connect to the internet. It is also used to make a wifi network.
            

def getData():
    option = st.selectbox('',('Select a Question','What is a Router?', 'What do you mean by Network?','What is the OSI model?'))
    if (not (option == 'Select a Question')):
        new_list = []
        model_answer = QuestionMatch(option)
        st.subheader("Model answer")
        st.write(model_answer)

        keywords = list(wordimportance(QuestionMatch(option)).keys())
        st.subheader("Extracted keywords :-")
        st.write(keywords)
        item = st.multiselect("Select keywords that you want to remove", keywords, key = '69')
        words = st.text_input('Enter a keywords to insert','')
        w = words.split(",") 
        for word in w:
            if(word.lower() not in model_answer.lower() ):
                st.write("Invalid keyword, keyword must be present in the model answer")
            elif (word != ''):
                st.write("Added keyword ➤ ",word)
                new_list.append(word.lower())
        if st.button("Make changes"):
            for keyword in keywords:
                if (keyword not in item):
                    new_list.append(keyword)
            keywords = new_list
            st.write("Updated list :-")
            st.write(keywords)
        


        g_fac = st.slider("Choose grammar factor",0,100,value = 50)
        s_fac = st.slider("Choose strength vs presence factor (0→presence 1→strength)",0,100,value = (50))

        st.sidebar.write("# Menu")
        img_file = st.sidebar.file_uploader(label='', type=['png', 'jpg'],help="upload image to be evaluated")
        if img_file:
            img = Image.open(img_file)
            st.subheader("Student Answer")
            st.image(img)
            save_uploaded_file(img_file)
            FILE_PATH="images/" + img_file.name   
            with io.open(FILE_PATH, 'rb') as image_file:
                content = image_file.read()
            image = vision.Image(content=content)
            image_context = vision.ImageContext( language_hints=['en-t-i0-handwrit'])
            response = client.document_text_detection(image=image, image_context=image_context)
            docText = response.full_text_annotation.text
            st.write(docText)
                # st.markdown("![Alt Text](https://media.giphy.com/media/l4FGIO2vCfJkakBtC/giphy.gif)")
            g_fac /= 100
            s_fac /= 100
            score = processAns(option,docText,keywords,g_fac,s_fac)
            st.write("Student score ->",score)            
        else:
            st.subheader("Upload Student Answer") 


                    



#saving selected image in the program directory for google API processing
def save_uploaded_file(uploadedfile):
  with open(os.path.join("./images/",uploadedfile.name),"wb") as f:
     f.write(uploadedfile.getbuffer())
  return st.success("Selected image {}".format(uploadedfile.name))


st.title("Student Answer Evaluator")
getData()







