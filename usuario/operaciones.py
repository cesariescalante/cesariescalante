import random
import math


def entero (a):
    a =int(a)
    return a

def suma(b,c):
    return b+c

def lista():
    a = []
    for indice in range(1, 30):
        a.append(random.randint(1,100))
    b = sorted(a)
    print(a)
    print(b)

def eleva(e):
    print(math.pow(e,2))
    print(math.pow(e,3))
    return e
def raiz(f):
    print(math.sqrt(f))
    return f




