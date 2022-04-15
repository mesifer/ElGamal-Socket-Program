# first of all import the socket library
import socket			
import elgamal
import random

s = socket.socket()		
print ("Server running")

host = '192.168.1.16'
port = 4444			

s.bind((host, port))		
print ("Server binded to %s" %(port))

s.listen(2)	
print ("Waiting for connection .......... ")		

while True:
    
    conn, addr = s.accept()	

    print ('Got connection from', addr )

    # get text from client
    string = (conn.recv(1024).decode())
    print(string)
    
    # send several KEY to client
    num_q = random.randint(pow(10, 20), pow(10, 50))
    
    num_g = random.randint(2, num_q)
    conn.send(bytes(str(num_g),'utf-8'))

    key = elgamal.gen_key(num_q) # Generate KEY

    num_h = elgamal.power(num_g, key, num_q)
    conn.send(bytes(str(num_h),'utf-8'))

    en_msg, num_p = elgamal.encrypt(string, num_q, num_h, num_g)
    conn.send(bytes(str(en_msg), 'utf-8'))

    dr_msg = elgamal.decrypt(en_msg, num_p, key, num_q)
    result = ''.join(dr_msg)
    conn.send(bytes(str(result), 'utf-8'))


    conn.close()

    break
