from envReader import read, getBool
from handlers.vision_detector import initVisionDetector
from handlers.ocr import initOcr
from imgServer import initImgServer
from audioServer import startAudioServer
from db.redisClient import initRedis
from slam_handler.slammain import init as initSlam

def run():
    read()

    if getBool("USE_REDIS"):
        initRedis()
    
    initSlam()
    initVisionDetector()
    #initOcr()

    startAudioServer()
    initImgServer()