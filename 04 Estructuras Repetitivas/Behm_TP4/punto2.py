
# Solicitar al usuario un número entero
numero = input("Ingrese un número entero: ")

# Verificar si el valor ingresado es un número entero válido
if numero.lstrip('-').isdigit():
    # Eliminar el signo negativo si existe y contar los dígitos
    cantidad_digitos = len(numero) if numero[0] != '-' else len(numero) - 1
    print(f"El número {numero} tiene {cantidad_digitos} dígitos.")
else:
    print("Error: Debe ingresar un número entero válido.")
