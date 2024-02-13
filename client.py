import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            print(f"\nMensaje recibido: {message.decode('utf-8')}")
            print("Escribe tu mensaje: ", end='', flush=True)
        except:
            print("Se ha perdido la conexión con el servidor.")
            client_socket.close()
            break

def start_client(server_host='127.0.0.1', server_port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    threading.Thread(target=receive_messages, args=(client_socket,)).start()

    try:
        while True:
            message = input("Escribe tu mensaje: ")
            client_socket.sendall(message.encode('utf-8'))
    except:
        client_socket.close()

if __name__ == "__main__":
    start_client()
