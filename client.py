# Import socket module
import socket			

s = socket.socket()		

host = '192.168.1.16'
port = 4444	

s.connect((host, port))

# Main
string = input("Input text : ")
s.send(bytes(string,'utf-8'))

# get KEY from server
num_g = (s.recv(1024).decode())
print("\ng used : ", num_g)
num_h = (s.recv(1024).decode())
print("g^a used : ", num_h)
print("\n")

# get ENCRYPT
en_msg = (s.recv(1024).decode())
print("ENCRYPTED : ", en_msg)
print("\n")

# get DECRYPT
result = (s.recv(1024).decode())
print("DECRYPTED : ", result)

# close the connection

s.close()	
	
