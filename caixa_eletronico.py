

saldo = float(input("Digite o valor do saldo: "))
operacao = input("Qual operação você deseja realizar (retirada ou depósito): ")

if operacao == "retirada":
    valor = float(input("Digite o valor que deseja retirar: "))
    novosaldo = saldo-valor
    print("Seu novo saldo é de:",novosaldo,"R$")
elif operacao == "deposito":
    valor = float(input("Digite o valor que você deseja depositar: "))
    novosaldo = float((saldo+valor))
    print("Seu novo saldo é de:",novosaldo,"R$")
else:
    print("Operação não encontrada.")