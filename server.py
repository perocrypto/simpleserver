import socket
import pickle

# Создаем сокет сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Получаем локальный IP-адрес и порт
host = '194.87.98.51'
port = 8250

# Связываем сокет с IP-адресом и портом
server_socket.bind((host, port))

# Начинаем прослушивание входящих подключений
server_socket.listen(5)

print(f"Сервер запущен. Слушаем {host}:{port}")

while True:
    # Ждем подключения клиента
    client_socket, address = server_socket.accept()
    print(f"Новое подключение от {address}")
    
    # Получаем сообщение от клиента
    message = client_socket.recv(160000)
    print(f"Получено сообщение: {message}")
    data_bytes = pickle.dumps(message)

    # Отправляем ответ клиенту
    response = f"Сервер получил сообщение: {message}"
    client_socket.sendall(response)
    

  
