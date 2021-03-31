import streamlit as st
import os
from io import StringIO
from PIL import Image
def save_uploaded_file(uploadedfile):
  with open(os.path.join("./",uploadedfile.name),"wb") as f:
     f.write(uploadedfile.getbuffer())
  return st.success("Saved file :{} in tempDir".format(uploadedfile.name))
st.title("  Student Answer Evaluator")
st.sidebar.write("# Menu")
img_file = st.sidebar.file_uploader(label='', type=['png', 'jpg'],help="upload image to be evaluated")
if img_file:
    img = Image.open(img_file)
    st.header("Selected Image")
    st.image(img)
    st.write(img_file.name)
    save_uploaded_file(img_file)
else:
    st.header('Select An Image') 
    
# stringio = StringIO(img_file.getvalue().decode("utf-8"))
# st.write(stringio)
# # To read file as string:
# string_data = stringio.read()
# st.write(string_data)

# bytes_data = img_file.getvalue()
# st.write(bytes_data)
