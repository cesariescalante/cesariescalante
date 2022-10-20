
usuario = input("ingrese nombre :")
caracteres = len(usuario)
alpha = usuario.isalnum()
if caracteres<7 or caracteres>12 and alpha == True:
    print("como minimo 7 caracteres , como maximo 12 y debe de contener por lo menos un numero")

else:
    print("su usuraio es :",usuario)



