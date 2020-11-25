v = "Hello"
decimal_list = []
def deci_make(v):
    print(v)
    v = ''.join(v.split())
    q = bin(int(v, 36))
    print(q)
    x = (len(q) - 1)/8
    container = []
    byte_list = []
    q = q[2:]
    for x in range(0, int(x)):
        for i in range(0, 8):
            y = q[1]
            container.append(y)
            q = q[1:]
        z = ''.join(map(str, container))
        byte_list.append(z)
        container.clear()

    print(byte_list)

    for x in range(0, len(byte_list)):
        val = int(byte_list[x], 2)
        print(val)
        decimal_list.append(val)

    print(decimal_list)

deci_make("Hello World")

def ConvertToBinary(n):
    if n > 1:
        ConvertToBinary(n//2)
    print(n % 2,end = '')

def diffie_Hellman(p,g,a,b,message):
    A = g**int(a) % p

    B = g**int(b) % p

    Sa = B**int(a) % p
    Sb = A**int(b) % p

    print("User 1 private key: ", a)
    print("User 1 public key: ", A)
    print("User 2 private key: ", b)
    print("User 2 public key: ", B)
    print("User 1 encryption key: ", Sa)
    print("User 2 encryption key: ", Sb)
    x = len(decimal_list)
    for i in range(0, x):
        z = int(decimal_list[i])
        print(z)
        print_val = ConvertToBinary(z)
        print(ascii(print_val))


diffie_Hellman(53201, 678, 47, 675, decimal_list)
