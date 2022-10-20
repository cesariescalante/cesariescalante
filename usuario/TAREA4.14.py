"""14. Crear un decorador donde imprimirá la cantidad de argumentos que
tiene la función a decorar usando *args y **kwargs.
Mensaje previo “La cantidad de argumentos que tiene la función es”
mensaje post “La función decoradora terminó de ejecutarse
correctamente”
"""

def operacionA(operacionB):
    def operacionC(*args,**kwargs):
        print("La cantidad de argumentos que tiene la función es")
        resultado = operacionB(*args,**kwargs)
        print("La función decoradora terminó de ejecutarse correctamente")
        return resultado
    return operacionC

@operacionA
def operacion(*args):
    var= args
    var=len(var)
    print(var)


a=int(input("ingrese un valor a: "))
b=int(input("ingrese un valor b: "))
c=int(input("ingrese un valor c: "))
d=int(input("ingrese un valor d: "))
operacion(a,b,c,d)