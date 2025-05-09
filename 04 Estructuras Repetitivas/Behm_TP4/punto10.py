
def invertir_numero():
    while True:
        numero = input("Ingrese un número entero positivo: ")
        
        # Validar que sea un número positivo
        if not numero.isdigit():
            print("Error: Debe ingresar un número entero positivo.")
            continue
        
        # Invertir los dígitos
        numero_invertido = numero[::-1]  # Invierte la cadena
        
        # Eliminar ceros a la izquierda en el número invertido
        numero_invertido = numero_invertido.lstrip('0')
        
        # Manejar caso especial cuando el número era 0
        if not numero_invertido:
            numero_invertido = '0'
        
        print(f"El número invertido es: {numero_invertido}")
        break

# Llamar a la función
invertir_numero()