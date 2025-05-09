# Programa para calcular la media de 100 números enteros ingresados por el usuario

def calcular_media():
    total_numeros = 100  # Cambiar este valor para probar con menos números
    suma = 0
    contador = 0

    print(f"Ingrese {total_numeros} números enteros (uno por uno):")

    while contador < total_numeros:
        try:
            numero = int(input(f"Número {contador + 1}/{total_numeros}: "))
            suma += numero
            contador += 1
        except ValueError:
            print("Error: Debe ingresar un número entero válido. Intente nuevamente.")

    media = suma / total_numeros
    print(f"\nLa media de los {total_numeros} números ingresados es: {media:.2f}")

# Versión alternativa para pruebas rápidas (usando solo 5 números)
def version_prueba():
    total_numeros = 5  # Versión reducida para pruebas
    calcular_media_alternativa(total_numeros)

def calcular_media_alternativa(cantidad):
    suma = 0
    numeros = []
    
    print(f"\n[VERSIÓN DE PRUEBA - Ingrese solo {cantidad} números]")
    
    for i in range(cantidad):
        while True:
            try:
                num = int(input(f"Número {i+1}/{cantidad}: "))
                numeros.append(num)
                suma += num
                break
            except ValueError:
                print("¡Error! Ingrese un número entero válido.")
    
    media = suma / cantidad
    print("\nResultado:")
    print(f"Suma total: {suma}")
    print(f"Cantidad de números: {cantidad}")
    print(f"Media calculada: {media:.2f}")

# Menú principal
print("1. Versión completa (100 números)")
print("2. Versión de prueba (5 números)")
opcion = input("Seleccione una opción (1/2): ")

if opcion == "1":
    calcular_media()
else:
    version_prueba()