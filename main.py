import math
import random
from collections import namedtuple

#https://en.wikipedia.org/wiki/RSA_(cryptosystem)

#euclidean 

def modInverse(a, m) : 
    a = a % m
    for x in range(1, m): 
        if ((a * x) % m == 1): 
            return x 
    return 1


def split_str(s):
  return [ch for ch in s]


def RSA_enc(m):
    p1 = 53
    p2 = 59
    e = 3

    #find n
    n = p1*p2

    encryptFunction = pow(m, e, n)

    #decryptFunction = pow(encryptFunction, d, n)

    return encryptFunction


def RSA_dec(m):
    p1 = 53
    p2 = 59
    e = 3

    #find n
    n = p1*p2

    #find phi
    lmd = (p1 - 1) * (p2 - 1)

    #mod inverse of e
    d = modInverse(e, lmd)

    encryptFunction = pow(m, e, n)

    decryptFunction = pow(encryptFunction, d, n)

    return decryptFunction


def main():

    text = "This message is encrypted using RSA"

    textArr = split_str(text)
    enc_Array = split_str(text)
    dec_Array = split_str(text)

    x = 0
    while x < len(textArr):
        textArr[x] = ord(textArr[x])
        #print(textArr[x])

        enc_Array[x] = RSA_enc(textArr[x])

        dec_Array[x] = RSA_dec(textArr[x])

        x += 1

    print("=========ENCRYPTED=========================== ")


    x = 0

    while x < len(enc_Array):
        print(enc_Array[x])
        x += 1

    print("===========DECRYPTED====================== ")

    x = 0

    while x < len(dec_Array):
        print(chr(dec_Array[x]))
        x += 1



if __name__ == "__main__":
    main()
