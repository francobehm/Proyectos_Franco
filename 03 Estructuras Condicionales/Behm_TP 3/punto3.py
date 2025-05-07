# Solicitar un número al usuario
numero = int(input("Por favor, ingrese un número par: "))

# Verificar si el número es par usando el operador módulo (%)
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")