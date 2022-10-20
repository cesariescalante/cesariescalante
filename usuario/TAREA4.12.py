"""12. Crear una función decoradora que dará los buenos días antes de
ejecutar una función a ser decorada y luego de ser ejecutada lanzará
un mensaje diciendo “Hasta luego”.
La función a decorar pedirá el nombre de una persona y retornará el
mensaje “Soy ‘nombre’”.
"""
def buenosdiasA(buenosdiasB):

    def buenosdiasC():
        print("Buenos dias")
        buenosdiasB()
        print("hasta luego")
    return buenosdiasC()


@buenosdiasA
def ingreso():
    var = input("ingrese su nombre")
    print(var,"soy hombre")