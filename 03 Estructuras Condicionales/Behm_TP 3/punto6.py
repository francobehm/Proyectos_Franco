import random
from statistics import mode, median, mean

# Generar lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

# Calcular las medidas estadísticas
try:
    moda_valor = mode(numeros_aleatorios)
    mediana_valor = median(numeros_aleatorios)
    media_valor = mean(numeros_aleatorios)
    
    # Mostrar resultados
    print("Lista generada (primeros 10 elementos):", numeros_aleatorios[:10], "...")
    print(f"\nModa: {moda_valor}")
    print(f"Mediana: {mediana_valor}")
    print(f"Media: {media_valor:.2f}")  # Mostramos con 2 decimales

    # Determinar el tipo de sesgo
    if media_valor > mediana_valor > moda_valor:
        print("\nLa distribución tiene sesgo positivo (a la derecha)")
    elif media_valor < mediana_valor < moda_valor:
        print("\nLa distribución tiene sesgo negativo (a la izquierda)")
    else:
        print("\nLa distribución no tiene sesgo claro o es simétrica")

except StatisticsError:
    # En caso de que no haya una moda única
    moda_valor = "No hay moda única"
    print("\nNo se puede determinar la moda (múltiples valores con la misma frecuencia máxima)")
    print(f"Mediana: {mediana_valor}")
    print(f"Media: {media_valor:.2f}")
    print("\nNo se puede determinar el sesgo sin moda única")
    
