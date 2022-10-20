"""6. Creando un archivo principal donde llamará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones.
- La primera función cargará una un número entero que pedirá al
usuario que ingrese por consola un valor.
- La segunda función solamente sumará dos valores.
- Desde el archivo principal importar al módulo y sumar dos valores
usando las funciones anteriormente creadas en el módulo
"""


from operaciones import entero, suma


var = input("ingrese un valor1: ")
var2 = input("ingrese un valor2: ")

car = entero(var)
car1 = entero(var2)
sum = suma(car,car1)
print("la suma total es:", sum)

