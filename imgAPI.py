import os, io
from google.cloud import vision_v1
from google.cloud.vision_v1 import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ferrous-pact-309206-db4cd544f0f2.json'

client = vision_v1.ImageAnnotatorClient()

# get path of image
# hardcoded -> images/sample.img

FILE_PATH = "images/test1.jpeg"


with io.open(FILE_PATH, 'rb') as image_file:
    content = image_file.read()
 
image = types.Image(content=content)
response = client.document_text_detection(image=image)

docText = response.full_text_annotation.text
print(docText)

# for confidence

# pages = response.full_text_annotation.pages
# for page in pages:
#     for block in page.blocks:
#         print('block confidence:', block.confidence)

#         for paragraph in block.paragraphs:
#             print('paragraph confidence:', paragraph.confidence)

#             for word in paragraph.words:
#                 word_text = ''.join([symbol.text for symbol in word.symbols])

#                 print('Word text: {0} (confidence: {1}'.format(word_text, word.confidence))

#                 for symbol in word.symbols:
#                     print('\tSymbol: {0} (confidence: {1}'.format(symbol.text, symbol.confidence))