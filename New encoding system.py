import time as t
from baseconv import base64 as b64
from baseconv import BaseConverter as BC

while 1:
    m_array = []
    m_array.clear()

    myCon = BC('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')

    '''for x in range(0,64):
        if x == 0:
                pass
        if x == 1:
                m = 1
                m = m*x
        if x > 1:
                m = m*x'''

    m = input(str)
    for x in m:
        m_array.append(ord(x))
        m_array.append(',')
    m_array.append(int(hex(hash(t.time())),16))
    m = ''.join(map(str, m_array))
    print(m)
    m = m.replace(',','')

    print('The amount of possible combinations is: \n',m)

    y = b64.encode(m)

    print('The amount of posssible combos in base64 form is: \n',y)

    z = myCon.encode(m)
    print('The amount of possible combinations in custom form is: \n',z)

    print(len(m))

    print(len(y))

    print(len(z))

    print(t.time())

    t.sleep(20)


