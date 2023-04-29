import threading
import cv2
import socket
import pickle
from handlers.vision_detector import getVisionDetector
from envReader import getValue
from mainLoop import Loop
from crop_images__callback import OnNewCroppedImages

running = True
client = None

def on_new_client(clientsocket,addr):
    global client, running
    client = clientsocket

    print("Connected to: " + str(addr))
    while running:
        x = clientsocket.recvfrom(1000000)
        data = x[0]

        if (len(data) == 0):
            continue
        try:
            data = pickle.loads(data)

            img = cv2.imdecode(data, cv2.IMREAD_COLOR)
            img = getVisionDetector().runDetector(img, OnNewCroppedImages)
            
            cv2.imshow('Img Server', img)
        except Exception as e:
            print(e)
            continue
        
        if cv2.waitKey(5) & 0xFF == 27:
            break

    cv2.destroyAllWindows()
    clientsocket.close()

def closeClient():
    global running, client
    running = False

def send(msg):
    global client
    client.send(msg)

def initImgServer():
    s = socket.socket()
    ip = getValue("IP")
    port = int(getValue("PORT"))
    s.bind((ip, port))
    s.listen(1)
    print("listening")

    while True:
        Loop()
        c, addr = s.accept()   
        threading.Thread(target=on_new_client, args=(c,addr)).start()
        
    s.close()