"""10. Crear una función donde se permitirá guardar el nombre, apellido y
edad de un usuario en un fichero (agenda.txt), cada usuario tiene que
estar guardado en una línea diferente y cada dato de una persona tiene
que estar separados por comas."""

def datos(nombre,apellido,edad):
    file = open("agenda.txt","a+")
    file = open("agenda.txt","w")
    #nombre = str(input("ingrese nombres :"))
    file.writelines(nombre + "," + "\n")
    #apellido = str(input("ingrese aqpellidos: "))
    file.writelines(apellido + ","+"\n")
    #edad = str(input("ingrese edad : "))
    file.writelines(edad +"\n")


nombre = str(input("ingrese nombres :"))
apellido = str(input("ingrese aqpellidos: "))
edad = str(input("ingrese edad : "))
datos(nombre,apellido,edad)
