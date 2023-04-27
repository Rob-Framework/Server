from handlers.vision_detector import initVisionDetector
from handlers.ocr import initOcr
from imgServer import initImgServer

initVisionDetector()
#initOcr()

def mainLoop():
    while True:
        pass

initImgServer()
mainLoop()