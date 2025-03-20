#menu
print("Opções de Sanduíche:\n Big Bob´s - R$3,50\n Big Mac - R$3,80\n Sanduíche natural - R$2,00")
sanduiche = input("Qual o nome do sanduíche: ")

print("Opções de Bebidas:\n Coca Cola\n Suco\n Guaraná")
bebida = input("Qual o nome da bebida: ")

print("Opções de Sobremesas:\n Sorvete\n Torta")
sobremesa = input("Digite a sobremesa escolhida: ")

#segurança
sanduiche = sanduiche.replace("big bobs", "big bob").replace("bigbob", "big bob").replace("bigmac", "big mac")
bebida = bebida.replace("coca cola", "coca").replace("guarana", "guaraná")

#escolhas
match sanduiche:
    case "big bob":
        sanduiche = 3.50
    case "big mac":
        sanduiche = 3.80
    case "natural":
        sanduiche = 2.00
    case _:
        print("Sanduíche não encontrado.")

match bebida:
    case "coca":
        bebida = 1.20
    case "suco":
        bebida = 1.50
    case "guaraná":
        bebida = 1.25
    case _:
        print("Bebida não encontrada.")

match sobremesa:
    case "sorvete":
        sobremesa = 3.00
    case "torta":
        sobremesa = 2.00
    case _:
        print("Torta não encontrada.")

valor = round(float(sanduiche+bebida+sobremesa),2)
print(f"Valor total do lanche: R${valor}")