
total = 0  # Inicializamos el acumulador

print("Ingrese números enteros para sumar. Ingrese 0 para terminar.")

while True:
    try:
        numero = int(input("Ingrese un número: "))
        if numero == 0:
            break  # Salir del bucle si se ingresa 0
        total += numero  # Acumular el número al total
    except ValueError:
        print("Error: Debe ingresar un número entero válido. Intente nuevamente.")

print(f"\nEl total acumulado es: {total}")