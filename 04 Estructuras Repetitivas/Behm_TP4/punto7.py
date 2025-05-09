
def calcular_suma():
    while True:
        try:
            # Solicitar al usuario un número entero positivo
            numero = int(input("Ingrese un número entero positivo: "))
            
            if numero < 0:
                print("Error: El número debe ser positivo. Intente nuevamente.")
                continue
            
            # Calcular la suma usando la fórmula de Gauss
            suma = numero * (numero + 1) // 2
            
            print(f"La suma de todos los números desde 0 hasta {numero} es: {suma}")
            break
            
        except ValueError:
            print("Error: Debe ingresar un número entero válido. Intente nuevamente.")

# Llamar a la función
calcular_suma()