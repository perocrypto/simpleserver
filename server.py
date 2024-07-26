import socket
import threading

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        client_socket.sendall(data)
    client_socket.close()

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f'Server started. Listening for incoming connections on {host}:{port}...')

    while True:
        client_socket, address = server_socket.accept()
        print(f'Connected by {address}')
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == '__main__':
    host = '194.87.98.51'  # Замените на свой IP-адрес
    port = 8250
    start_server(host, port)