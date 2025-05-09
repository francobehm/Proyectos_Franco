# Programa para sumar números entre dos valores (excluyéndolos)

# Solicitar los dos números al usuario
try:
    num1 = int(input("Ingrese el primer número entero: "))
    num2 = int(input("Ingrese el segundo número entero: "))
    
    # Determinar el rango correcto (maneja si num1 > num2)
    inicio = min(num1, num2) + 1
    fin = max(num1, num2)
    
    # Calcular la suma
    suma = 0
    for numero in range(inicio, fin):
        suma += numero
    
    # Mostrar resultado
    print(f"La suma de los números entre {num1} y {num2} (excluyéndolos) es: {suma}")

except ValueError:
    print("Error: Ambos valores deben ser números enteros.")
    