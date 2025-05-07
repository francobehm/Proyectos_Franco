nombre = input("Ingrese su nombre: ")

while True:
    print("\nOpciones de formato:")
    print("1. Nombre en MAYÚSCULAS")
    print("2. nombre en minúsculas")
    print("3. Nombre con primera letra mayúscula")
    
    opcion = input("\nElija una opción (1, 2 o 3): ")
    
    if opcion in ("1", "2", "3"):
        break
    print("¡Opción no válida! Por favor ingrese 1, 2 o 3")

if opcion == "1":
    resultado = nombre.upper()
elif opcion == "2":
    resultado = nombre.lower()
else:
    resultado = nombre.title()

print("\nResultado:", resultado)