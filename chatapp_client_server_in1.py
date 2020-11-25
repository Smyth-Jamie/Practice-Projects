import socket
import sys
import time

ascii_list = []

def ascii_make(string):
    print(string)
    a = len(string)
    for x in range(0, a):
        ascii_list.append(ord(string[x]))

def ascii_decode(val):
    character_list = []
    a = len(val)
    for x in range(0, a):
        character_list.append(chr(int(val[x])))
    print_val = ''.join(map(str, character_list))
    return print_val

def dh_key_gen(p,g,val):
    Capitol = g**int(val)%p
    return Capitol

def dh_encrypt(p,priv,pub,message):
    encrypted_list = []
    s = pub**int(priv)%p
    print("User private key: ", priv)
    print("User public key: ", pub)
    print("User encryption key: ", s)
    x = len(message)
    for i in range(0, x):
        encrypted_val = int(message[i])*s
        encrypted_list.append(encrypted_val)
    return encrypted_list

def dh_decrypt(p,priv,pub,encrypted_values):
    decrypted_list = []
    s = pub**int(priv)%p
    print("Encryption key: ", s)
    x = len(encrypted_values)
    for i in range(0, x):
        d_val = (encrypted_values[i])/s
        decrypted_list.append(round(d_val))
    return decrypted_list

print("Are you the host (1) or the client (2)")
print("Please enter the relevent index number")
setup = input(int)

if setup == '1':
    print("Thank you for selecting host")
    x = socket.socket()
    h_name = socket.gethostname()
    print("Server will start on host: ", h_name)
    print("Please enter the comms port address")
    port = input(int)

    x.bind((h_name, int(port)))
    print("Server done binding to host and port successfully!")
    print("Server is waiting for incoming connections")

    x.listen()

    connection,address = x.accept()
    print(address, "has connected to the server and is now online")

elif setup == '2':
    print("Thank you for selecting clinet")
    x = socket.socket()
    h_name = input(str("Enter the host name of your required server"))
    print("Please enter the comms port address")
    port = input(int)

    x.connect((h_name, int(port)))
    print("Connected to the chat server")


print("Please enter the required prime")
p = input(int)
p = int(p)
print(p)
print("Please enter the required coprime")
g = input(int)
g = int(g)
print("PLease enter a COPLETELY RANDOM number")
priv = input(int)
priv = int(priv)
print("Calculating your public key.....")
pub = dh_key_gen(p,g,priv)


pub_key = str(pub).encode()
connection.send(pub_key)
co_pub = connection.recv(1024)
co_pub = co_pub.decode()
co_pub = int(co_pub)

while 1:    
    display_mess = input(str(">>"))
    display_mess = dh_encrypt(p,priv,co_pub,display_mess)
    display_mess = display_mess.encode()
    connection.send(display_mess)
    print("Message has been sent...")
    in_message = connection.recv(1024)
    in_message = in_message.decode()
    in_message = dh_decrypt(p,priv,co_pub,in_message)
    print("Client:", in_message)
