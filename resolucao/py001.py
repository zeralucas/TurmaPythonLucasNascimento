print("="*60)

frase = input("Digite uma franse: ")
letra = input("Digite uma letra: ")

print("{} A letra foi encontrada {} vezes.".format(" "*5, frase.count(letra)))
print("{} A letra foi encontrada pela primeira vez na posição {} vezes.".format(" "*5, frase.index(letra)+1))
print("{} A letra foi encontrada pela última vez na posição {}.".format(" "*5, frase.rindex(letra)+1))

print("="*60)