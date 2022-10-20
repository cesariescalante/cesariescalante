"""Crear una función para encontrar el error en el siguiente bloque de
código. Crea una excepción para evitar que tu programa se bloquee y
además imprime un mensaje al usuario la causa y/o solución:"""

def sumatoria (a,b):
    try:
        resultado = 80 + "Hola Pythonista"

    except TypeError:
        print("No se puede sumar un string con un dato tipo int")

    else:
        print(resultado)

sumatoria(4,5)
