# Solicitar magnitud del terremoto al usuario
try:
    magnitud = float(input("Ingrese la magnitud del terremoto (escala de Richter): "))
    
    # Clasificar el terremoto según su magnitud
    if magnitud < 3:
        categoria = "Muy leve (imperceptible)"
    elif 3 <= magnitud < 4:
        categoria = "Leve (ligeramente perceptible)"
    elif 4 <= magnitud < 5:
        categoria = "Moderado (sentido por personas, pero generalmente no causa daños)"
    elif 5 <= magnitud < 6:
        categoria = "Fuerte (puede causar daños en estructuras débiles)"
    elif 6 <= magnitud < 7:
        categoria = "Muy fuerte (puede causar daños significativos)"
    else:
        categoria = "Extremo (puede causar graves daños a gran escala)"
    
    # Mostrar resultado
    print(f"\nPara una magnitud de {magnitud} en la escala de Richter:")
    print(f"Categoría: {categoria}")

except ValueError:
    print("Error: Por favor ingrese un valor numérico válido")