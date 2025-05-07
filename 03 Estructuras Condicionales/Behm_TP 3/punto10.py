# Solicitar datos al usuario
hemisferio = input("¿En qué hemisferio te encuentras? (N para Norte / S para Sur): ").upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

# Validar datos de entrada
if hemisferio not in ['N', 'S']:
    print("Error: Hemisferio debe ser N (Norte) o S (Sur)")
elif mes < 1 or mes > 12:
    print("Error: Mes debe estar entre 1 y 12")
elif dia < 1 or dia > 31:
    print("Error: Día debe estar entre 1 y 31")
else:
    # Determinar la estación según la fecha y hemisferio
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        estacion_norte = "invierno"
        estacion_sur = "verano"
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        estacion_norte = "primavera"
        estacion_sur = "otoño"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        estacion_norte = "verano"
        estacion_sur = "invierno"
    else:  # 21/9 al 20/12
        estacion_norte = "otoño"
        estacion_sur = "primavera"

    # Mostrar resultado según hemisferio
    if hemisferio == 'N':
        print(f"\nActualmente es {estacion_norte} en el hemisferio norte")
    else:
        print(f"\nActualmente es {estacion_sur} en el hemisferio sur")