# Solicitar la contraseña al usuario
contraseña = input("Ingrese una contraseña (8-14 caracteres): ")

# Verificar la longitud usando len()
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")