"""11. Crear una función que creará el archivo calificaciones.txt que contiene
las calificaciones de un curso.
Escribir un programa que contenga las siguientes funciones:
- Una función que guarde el nombre, 2 notas y el promedio (el
promedio lo calculará la función antes de escribirlo en el fichero)
- Y una función que leerá el fichero anterior y dirá si el alumno X,
aprobó o no, tener en cuenta que si tiene un promedio mayor a día
tendrá un mensaje de “Alumno X, aprobado” de lo contrario “Alumno
X, desaprobado”"""

def datos(nombre,nota1,nota2):
    file = open("calificaciones.txt","a+")
    file = open("calificaciones.txt","w")
    file.writelines(nombre + "\n")
    valor1 = str(nota1)
    file.writelines("nota1" "=" + valor1 +"\n")
    valor2 = str(nota2)
    file.writelines("nota2" + "=" + valor2 + "\n")
    prom = nota1 + nota2
    prom = prom/2
    prom =str(prom)

    file.writelines("promedio"+ "=" + prom)





def promedio():
    file = open("calificaciones.txt", "r")
    file = file.readlines()
    alumno =file[0]
    file = file[3]
    file = len(file)

    if file <=10:
        print("Alumno {} desaprobado".format(alumno))
    else:
        print("Alumono {} aprodado".format(alumno))




nombre = input("ingrese nombre: ")
nota1 = int(input("ingrese nota 1: "))
nota2 = int(input("ingrese nota 2: "))
datos(nombre,nota1,nota2)
promedio()