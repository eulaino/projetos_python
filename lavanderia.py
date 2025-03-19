camisas = int(input("Digite o número de camisas: "))
calcas = int(input("Digite o número de calças: "))
meias = int(input("Digite o número de meias: "))

valorcamisa = float(camisas*9.50)
valorcalca = float(calcas*15.00)
valormeia = float(meias*1.20)
total = valorcamisa+valorcalca+valormeia

print("O total gasto na lavanderia foi: R$", total)
