import json
import threading
import tcpServer

def startConsoleListener():
    threading.Thread(target=consoleThread).start()

def consoleThread():
    while True:
        cmd = input("Enter command: ")
        print(cmd)

        data = ""
        if cmd == "forward" or cmd == "backward" or cmd == "left" or cmd == "right" or cmd == "stop" or cmd == "break" or cmd == "slow_stop":
            data = { "command": cmd }
        elif data.startswith("move_hand"):
            split = data.split(" ")
            cmdObj = {
                "command" : "move_hand",
                "movement" : split[1],
                "servo": split[2],
            }
            data = cmdObj

        tcpServer.tcpServer.sendMessage(0, data)