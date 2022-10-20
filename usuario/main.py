def usuario(a):
    caracteres = len(a)

    if caracteres < 7:
        print("El nombre de usuario puede contener solo letras y números")
    elif caracteres > 12:
        print("El nombre de usuario puede contener solo letras y números")

    else:
        print("usuario creado correctamente",a.isalnum())