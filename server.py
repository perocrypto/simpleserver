import socket
import pickle

# Создаем сокет сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Получаем локальный IP-адрес и порт
host = '194.87.98.51'
port = 8250

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Сервер запущен на {host}:{port}. Ожидание подключения...")
        
        conn, addr = server_socket.accept()
        with conn:
            print(f"Подключено к {addr}")
            while True:
                # Получаем размер данных
                data_size = int.from_bytes(conn.recv(4), byteorder='big')
                
                # Получаем данные
                data_bytes = b''
                while len(data_bytes) < data_size:
                    packet = conn.recv(4096)
                    if not packet:
                        break
                    data_bytes += packet
                
                # Десериализуем массив
                received_array = pickle.loads(data_bytes)
                print("Полученный массив:")
                print(received_array)
    
                # Сериализуем массив для отправки обратно
                response_bytes = pickle.dumps(received_array)
                
                # Отправляем размер массива
                conn.sendall(len(response_bytes).to_bytes(4, byteorder='big'))
                # Отправляем массив
                conn.sendall(response_bytes)
    

  
