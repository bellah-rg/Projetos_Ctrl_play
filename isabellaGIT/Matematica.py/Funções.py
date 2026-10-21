from random import randint

def sortear(*nomes):
    sorteado = nomes[randint(0, len(nomes)-1)]
    return sorteado

nomeSorteado = sortear("Gustavo", "Mauricio", "Isabella")

if nomeSorteado == "Isabella":
    premio = 1000
else:
    premio = 1

print(nomeSorteado)
