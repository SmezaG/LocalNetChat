import socket
import threading

clients = []

def broadcast(message, source):
    for client in clients:
        if client != source:
            try:
                client.send(message)
            except:
                clients.remove(client)

def client_handler(connection):
    while True:
        try:
            message = connection.recv(1024)
            broadcast(message, connection)
        except:
            clients.remove(connection)
            connection.close()
            break

def start_server(host='0.0.0.0', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Servidor escuchando en {host}:{port}")

    while True:
        connection, _ = server_socket.accept()
        print("Conectado a un nuevo cliente.")
        clients.append(connection)
        thread = threading.Thread(target=client_handler, args=(connection,))
        thread.start()

if __name__ == "__main__":
    start_server()
