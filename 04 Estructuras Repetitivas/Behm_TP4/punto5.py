import random

def juego_adivina_numero():
    numero_secreto = random.randint(0, 9)
    intentos = 0
    
    print("¡Adivina el número secreto entre 0 y 9!")
    
    while True:
        try:
            intento = int(input("Ingresa tu número: "))
            intentos += 1
            
            if intento < 0 or intento > 9:
                print("Por favor ingresa un número entre 0 y 9.")
                continue
            
            if intento < numero_secreto:
                print("El número secreto es mayor.")
            elif intento > numero_secreto:
                print("El número secreto es menor.")
            else:
                print(f"¡Felicitaciones! Adivinaste el número en {intentos} intentos.")
                break
                
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")

# Iniciar el juego
juego_adivina_numero()
