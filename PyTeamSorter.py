import random

quantidade = int(input("Quantidade de pessoas: "))
n_grupos = int(input("Digite a quantidade de grupos: "))
quantidade += 1
participantes = []

for x in range(1,quantidade):
    nome = input(f"Digite o nome {x}: ")
    participantes.append(nome)
    #print(participantes)

random.shuffle(participantes)
grupos = [[] for i in range(n_grupos)]
for i, nome in enumerate(participantes):
    grupos[i % n_grupos].append(nome)

for i, grupo in enumerate(grupos, 1):
    if quantidade > 0:
        print(f"\nGrupo {i}: {grupo}")
#sorteado = random.choice(participantes)
#remover = participantes.remove(sorteado)
#print(f'O sorteado é: {sorteado}')