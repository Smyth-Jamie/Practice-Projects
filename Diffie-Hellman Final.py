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

a_val = 4
b_val = 7
divi = 500000

def dh_key_generator(p,g,val):
    Capitol = g**int(val)%p
    return Capitol



def diffie_Hellman_encrypt(p,priv,pub,message,div):
    encrypted_list = []

    s = pub**int(priv) % p

    print("User private key: ", priv)
    print("User public key: ", pub)
    print("User encryption key: ", s)

    x = len(message)
    for i in range(0, x):
        encrypted_val = (int(message[i])*s)/div
        encrypted_list.append(encrypted_val)
    return encrypted_list

def diffie_Hellman_decrypt(p,priv,pub,encrypted_values,div):
    decrypted_list = []
    s = pub**int(priv)%p
    print('Encryption key: ', s)
    x = len(encrypted_values)
    for i in range(0, x):
        d_val = ((encrypted_values[i])/s)*div
        decrypted_list.append(round(d_val))
    return decrypted_list

while 1:
    print("Please input a message to encrypt: ")
    weho = input(str)

    ascii_make(weho)

    a_pub = dh_key_generator(53201,678,a_val)
    b_pub = dh_key_generator(53201,678,b_val)

    encrypted = diffie_Hellman_encrypt(53201,a_val,b_pub, ascii_list,divi)
    print(encrypted)

    decrypted = diffie_Hellman_decrypt(53201,b_val,a_pub, encrypted,divi)
    print(decrypted)

    decoded = ascii_decode(decrypted)
    print(decoded)
    ascii_list.clear()

