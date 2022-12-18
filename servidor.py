from socket import *

def Registro(valor):
    if(valor=='1'):
        return bytes(("Bienvenido Usuario"),encoding='utf-8')
    elif(valor=='2'):
        return bytes(("Bienvenido Administrador"),encoding='utf-8')
    elif(valor=='3'):
        return bytes(("Bienvenido Desarrollador"),encoding='utf-8')
    else:
        return bytes(("Error, no se encontro su rol"),encoding='utf-8')

puertoServidor = 12000

socket = socket(AF_INET, SOCK_DGRAM)

socket.bind(("127.0.0.1", puertoServidor))
print("Recibiendo mensaje...")

while True:
    try:
        mensaje, ipcliente = socket.recvfrom(2048)
        valor = mensaje.decode("utf-8")
        respuesta = Registro(valor)

        socket.sendto(respuesta, ipcliente)
    except:
        print("Se presento un error...")
        exit()
