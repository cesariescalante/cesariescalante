"""13. Haciendo el uso de *args y **kwargs aplicarlo debidamente para usar
decorar una función que recibirá 4 argumentos los cuales se
multiplicaran entre ellos.
Mensaje previo al usar el decorador “Está por ejecutarse la función” y
mensaje luego de usar el decorador “La función ha sido ejecutado
correctamente”"""


def operacionA(operacionB):
    def operacionC(*args,**kwargs):
        print("Está por ejecutarse la función")
        resultado = operacionB(*args,**kwargs)
        print("La funcion a sido ejecutado correctamente")
        return resultado
    return operacionC

@operacionA
def operacion(a,b,c,d):
    var= a*b*c*d
    print(a,"x",b,"x",c,"x",d,"=",var)


a=int(input("ingrese un valor a: "))
b=int(input("ingrese un valor b: "))
c=int(input("ingrese un valor c: "))
d=int(input("ingrese un valor d: "))
operacion(a,b,c,d)