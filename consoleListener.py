import json
import threading
from imgServer import send

def startConsoleListener():
    threading.Thread(target=consoleThread).start()

def consoleThread():
    while True:
        inp = input("Enter command: ")
        print(inp)

        data = json.dumps({ "command": inp })
        send(data.encode())