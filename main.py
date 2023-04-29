from envReader import read
from handlers.vision_detector import initVisionDetector
from handlers.ocr import initOcr
from imgServer import initImgServer
from audioServer import startAudioServer
from consoleListener import startConsoleListener

read()
initVisionDetector()
#initOcr()

startAudioServer()
startConsoleListener()
initImgServer()