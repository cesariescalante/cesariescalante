"""Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:"""

try:
    string = "Hello Pythonista"
    print(string/0)

except (ValueError, TypeError, IndexError):
    print("no se puede dividir un string")
except ZeroDivisionError:
    print("no se puede dividir entre cero un string")

