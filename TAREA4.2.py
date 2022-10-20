"""Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:
"""
try:
    lista = [2, 6, 10, 4, 5, 23, 1]
    lista[10]
except IndexError:
    print("Lista ingresa esta fuera de rango")