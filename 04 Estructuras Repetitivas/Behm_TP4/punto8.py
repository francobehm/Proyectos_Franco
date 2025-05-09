# Programa para analizar 100 números enteros ingresados por el usuario

def analizar_numeros():
    # Inicializar contadores
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0
    ceros = 0  # Para contar los ceros, aunque no se solicitó
    
    print("Ingrese 100 números enteros (uno por uno):")
    
    # Solicitar exactamente 100 números
    for i in range(1, 101):
        while True:
            try:
                num = int(input(f"Número {i}/100: "))
                break
            except ValueError:
                print("Error: Debe ingresar un número entero válido. Intente nuevamente.")
        
        # Clasificar el número
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
            
        if num > 0:
            positivos += 1
        elif num < 0:
            negativos += 1
        else:
            ceros += 1
    
    # Mostrar resultados
    print("\nResultados:")
    print(f"- Números pares: {pares}")
    print(f"- Números impares: {impares}")
    print(f"- Números positivos: {positivos}")
    print(f"- Números negativos: {negativos}")
    print(f"- Ceros: {ceros} (información adicional)")

# Versión para pruebas rápidas (usando solo 5 números)
def version_prueba():
    global pares, impares, positivos, negativos, ceros
    pares = impares = positivos = negativos = ceros = 0
    cantidad = 5  # Cambiar a 100 para la versión final
    
    print(f"\n[VERSIÓN DE PRUEBA - Ingrese solo {cantidad} números]")
    
    for i in range(1, cantidad + 1):
        while True:
            try:
                num = int(input(f"Número {i}/{cantidad}: "))
                break
            except ValueError:
                print("Error: Debe ingresar un número entero válido. Intente nuevamente.")
        
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
            
        if num > 0:
            positivos += 1
        elif num < 0:
            negativos += 1
        else:
            ceros += 1
    
    print("\nResultados (prueba):")
    print(f"- Pares: {pares} | Impares: {impares}")
    print(f"- Positivos: {positivos} | Negativos: {negativos} | Ceros: {ceros}")

# Ejecutar el programa completo o la versión de prueba
opcion = input("¿Desea ejecutar la versión completa (100 números)? (s/n): ")

if opcion.lower() == 's':
    analizar_numeros()
else:
    version_prueba()
    
    
