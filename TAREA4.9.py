"""9. Crear una función que pida al usuario un número entero entre 1 y 20 y
guarde en un fichero (que no existe) con el nombre tabla.txt la tabla
de multiplicar de ese número, done n es el número introducido."""
def tabla (n):
    archivo = open("tabla.txt", "a+")
    archivo = open("tabla.txt", "w")
    if n>1 and n<20:

        for i in range(1,11):
            resultado = i * n
            resultado = str(resultado)
            print(n,"x",i,"=",resultado)
            archivo.writelines(resultado + "\n")



    else:
        print("Error valor entre 1 y 20")


tabla(4)
#archivo = open("tabla.txt", "a+")
#archivo = open("tabla.txt", "w")
#archivo.write("archivo")
#archivo.close()