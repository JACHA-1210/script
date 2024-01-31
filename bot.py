import socket

# Dirección IP y Puerto para Escuchar
host = "192.168.249.128"
port = 5555

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)

    print(f"Server listening on {host}:{port}")

    client_socket, addr = s.accept()
    print(f"Connection from {addr}")

    while True:
        command = input("Enter command (type 'exit' to end): ")
        client_socket.sendall(command.encode())
        if command.lower() == "exit":
            break
        output = client_socket.recv(1024).decode()
        print(output)

    client_socket.close()

if __name__ == "__main__":
    start_server()
