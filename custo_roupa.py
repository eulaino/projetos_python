tecido = input("Digite o tipo de tecido: ")
botoes = int(input("Digite a quantidade de botões: "))
forro = input("Você precisará de forro? ")

if tecido == "algodão":
    tecido = 40.00
    precobotao = float(botoes*1.20)
    precoforro = 20.00
elif tecido == "seda":
    tecido = 80.00
    precobotao = float(botoes*1.10)
    precoforro = 35.00
elif tecido == "linho":
    tecido = 35.00
    precobotao = float(botoes*2.00)
    precoforro = 70.00
else:
    print("Tecido não encontrado")

if forro == "s":
    total = tecido+precobotao+precoforro
    print("Custo total da roupa com forro: R$",total)
elif forro == "n":
    total = tecido+precobotao
    print("Custo total da roupa com forro: R$",total)
else:
    print("Não foi possível calcular o custo.")


