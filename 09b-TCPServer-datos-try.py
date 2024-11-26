import socket

HOST = '' #todas las interfaces locales a la escucha
PORT = 2000

try:
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind ((HOST,PORT))
        s.listen()
        conn, addr = s.accept() #linea bloqueante
        with conn:
            print (f"Conexión exitosa del cliente. IP {addr[0]} Puerto {addr[1]}")
            while True:
                data = conn.recv(1024) #linea bloqueante
                print (data)
                if data==b"0":                    
                    break
                conn.sendall(b"mensaje recibido")            
except socket.error as e:
    print ("Error en socker: %s" %e)
