from envReader import read, getBool
from handlers.vision_detector import initVisionDetector
from handlers.ocr import initOcr
from imgServer import initImgServer
from audioServer import startAudioServer
from db.redisClient import initRedis

def run():
    read()

    if getBool("USE_REDIS"):
        initRedis()
        
    initVisionDetector()
    #initOcr()

    startAudioServer()
    initImgServer()