import socket
import threading
from envReader import getValue

def startAudioServer():
    threading.Thread(target=start_tcp_server_thread).start()
    
def start_tcp_server_thread():
    ip = getValue("AUDIO_IP")
    port = int(getValue("AUDIO_PORT"))

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(1)

    print(f"Server is listening on {ip}:{port}")

    while True:
        connection, client_address = server_socket.accept()

        print(f"Connection from {client_address}")

        try:
            while True:
                audio_data = connection.recv(1024)

                if not audio_data:
                    break

                print(f"Received audio data: {audio_data}")

        finally:
            connection.close()