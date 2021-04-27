import streamlit as st
import os,io
# from io import StringIO
from PIL import Image
from google.cloud import vision_v1
from google.cloud.vision_v1 import types
from keywordExtractor import processAns

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'token.json'


client = vision_v1.ImageAnnotatorClient()


#saving selected image in the program directory for google API processing
def save_uploaded_file(uploadedfile):
  with open(os.path.join("./",uploadedfile.name),"wb") as f:
     f.write(uploadedfile.getbuffer())
  return st.success("Selected image {}".format(uploadedfile.name))


st.title("Student Answer Evaluator")

st.sidebar.write("# Menu")
img_file = st.sidebar.file_uploader(label='', type=['png', 'jpg'],help="upload image to be evaluated")
if img_file:
    img = Image.open(img_file)
    st.header("Selected Image")
    st.image(img)
    st.write(img_file.name)
    save_uploaded_file(img_file)
    FILE_PATH=img_file.name   
    with io.open(FILE_PATH, 'rb') as image_file:
        content = image_file.read()
 
    image = types.Image(content=content)
    response = client.document_text_detection(image=image)

    docText = response.full_text_annotation.text
    st.write(docText)
    processAns(docText)
    #exec(open("keywordExtractor.py").read())
else:
    st.header('Select An Image') 


