# Solicitar la edad al usuario
edad = int(input("Por favor, ingrese su edad: "))

# Determinar la categoría según la edad
if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")