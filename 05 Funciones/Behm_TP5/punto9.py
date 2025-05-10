# Lista inicial
compras = [
    ["pan", "leche"],            # Cliente 1
    ["arroz", "fideos", "salsa"], # Cliente 2
    ["agua"]                     # Cliente 3
]

# --- Modificaciones ---
# a) Cliente 3: Agregar "jugo"
compras[2].append("jugo")  # Cliente 3 ahora tiene ["agua", "jugo"]

# b) Cliente 2: Reemplazar "fideos" por "tallarines"
compras[1][1] = "tallarines"  # Cliente 2 ahora tiene ["arroz", "tallarines", "salsa"]

# c) Cliente 1: Eliminar "pan"
compras[0].remove("pan")  # Cliente 1 ahora tiene ["leche"]

# --- Resultado Final ---
print("Lista actualizada con cambios detallados:")
for i, cliente in enumerate(compras, start=1):
    print(f"Cliente {i}: {cliente}")