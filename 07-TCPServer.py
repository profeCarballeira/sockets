import socket

HOST = '127.0.0.1' #dirección de loopback standart para localhos
PORT = 2000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4 - TCP
try:
    s.bind((HOST, PORT))
    s.listen(1) #creo una lista de un cliente en espera
    conn, addr = s.accept() #función bloqueante
    print (f"Conexión exitosa del cliente. IP {addr[0]} Puerto {addr[1]}")
    conn.close()
except socket.error as exc:
    print ("Excepción de socket: %s" % exc)
finally:
    #cerramos la escucha general de nuestro servidor
    s.close()