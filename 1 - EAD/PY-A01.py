palavra = "infinity school"

contador = 0



for letra in palavra:

    if letra in ('aeiou'):
        print(letra)
        contador += 1

print(contador)