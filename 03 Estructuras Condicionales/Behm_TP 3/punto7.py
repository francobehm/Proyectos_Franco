texto = input("Ingrese una frase o palabra: ")
if texto and texto[-1].lower() in "aeiou":
    texto += "!"
print(texto)