from socket import *

ipCliente = "localhost"
puertoCliente = 12000

socket = socket(AF_INET, SOCK_DGRAM)

mensaje = input("Ingrese su codigo:")

try:
    mensajeBytes = bytes(mensaje, encoding='utf-8')
    socket.sendto(mensajeBytes, (ipCliente, puertoCliente))

    mensajeRespuesta, ipServidor = socket.recvfrom(2048)

    print("Respuesta del servidor:",mensajeRespuesta.decode("utf-8"))
    socket.close()
except:
    print("Se presento un error...")
    exit()