# main.py

import socket
import subprocess
import importlib
import bot  # Importa directamente el módulo bot

def run():
    # Define la dirección IP y el puerto del servidor
    host = "172.16.22.190"
    port = 5555

    try:
        # Crea un socket TCP/IP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Conecta el socket al servidor
        s.connect((host, port))

        # Ejecuta el bot
        bot.run()

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
            command = input("Ingrese el comando a enviar al servidor: ")
            s.sendall(command.encode())

            # Recibe y muestra la salida del comando ejecutado en el servidor
            output = s.recv(1024)
            print(output.decode())

    except ConnectionRefusedError:
        print("Error: No se pudo establecer la conexión. Asegúrate de que el servidor esté en ejecución.")
    finally:
        # Cierra la conexión al salir del bucle
        s.close()

if __name__ == "__main__":
    run_bot()
