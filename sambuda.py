print("Opções de Sanduíche:\n Big Bob´s - R$3,50\n Big Mac - R$3,80\n Sanduíche natural - R$2,00")
sanduiche = input("Qual o nome do sanduíche: ")
print("Opções de Bebidas:\n Coca Cola\n Suco\n Guaraná")
bebida = input("Qual o nome da bebida: ")
print("Opções de Sobremesas:\n Sorvete\n Torta")
sobremesa = input("Digite a sobremesa escolhida: ")


if sanduiche == "big bobs" or "big bob´s":
    sanduiche = 3.50
elif sanduiche == "big mac":
    sanduiche = 3.80
elif sanduiche == "natural":
    sanduiche = 2.00
else:
    print("Sanduíche não encontrado.")

if bebida == "coca cola" or "coca-cola":
    bebida = 1.20
elif bebida == "suco":
    bebida = 1.50
elif bebida == "guaraná" or "guarana":
    bebida = 1.25
else:
    print("Bebida não encontrada.")

if sobremesa == "sorvete":
    sobremesa = 3.00
elif sobremesa == "torta":
    sobremesa = 2.00
else:
    print("Torta não encontrada.")

valor = float(sanduiche+bebida+sobremesa)
print("Valor total do lanche: R$",valor)