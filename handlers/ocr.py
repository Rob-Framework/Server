import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import easyocr
# https://www.jaided.ai/easyocr/modelhub/

reader = None

def initOcr():
    global reader
    reader = easyocr.Reader(['en'])

def getOcr(img):
    global reader
    result = reader.readtext(img)
    print(result)
    return result
