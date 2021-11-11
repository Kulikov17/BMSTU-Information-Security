from math import sqrt
from random import choices, choice

def getListSimpleNumbers(n):
    listNumber = [num for num in range(2, n + 1)]

    for num in range(2, int(sqrt(n + 1)) + 1):
        for j in range(len(listNumber)):
            if j >= len(listNumber):
                break
            if num != listNumber[j] and listNumber[j] % num == 0:
                listNumber.pop(j)

    return listNumber

def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)

def phi(n):
    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result += 1
    return result

def eList(phi_n):
    list = []
    for i in range(2, phi_n):
        if (gcd(i, phi_n) == 1):
            list.append(i)
    return list

def bezout(a, b):
    '''An implementation of extended Euclidean algorithm.
    Returns integer x, y and gcd(a, b) for Bezout equation:
        ax + by = gcd(a, b).
    '''
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
    return (x, y, a)


def RSA(message, key, n):
    res = ""
    for sym in message:
        ch = pow(ord(sym), key, n)
        res += chr(ch)
    return res

def bezout(a, b):
    '''An implementation of extended Euclidean algorithm.
    Returns integer x, y and gcd(a, b) for Bezout equation:
        ax + by = gcd(a, b).
    '''
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q

    return a

p, q = choices(getListSimpleNumbers(24), k = 2)
n = p * q
phi_n = (p - 1) * (q - 1)
e = choice(eList(phi_n))
d = bezout(e, n)

decrypt = RSA("hello", e, n)
encrypt = RSA(decrypt, d, n)

print(decrypt)
print(encrypt)


