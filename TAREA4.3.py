"""Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:"""

try:
    persona= { 'nombre':'Xavier', 'apellido':'Rodriguez', 'dni':'63325345'}
    print(persona['profesion'])
except KeyError:
    print("no se puede encontar el valor :" )

