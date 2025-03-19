operacao = input("Qual operação deseja utilizar? ")
if operacao == "soma":
    n1 = float(input("Primeiro número: "))
    n2 = float(input("Segundo número: "))
    soma = n1+n2
    resultado = float(soma)
    print(resultado)
elif operacao == "subtração": 
    n1 = float(input("Primeiro número: "))
    n2 = float(input("Segundo número: "))
    subt = n1-n2
    resultado = float(subt)
    print(resultado)
elif operacao == "multiplicação": 
    n1 = float(input("Primeiro número: "))
    n2 = float(input("Segundo número: "))
    mult = n1*n2
    resultado = float(mult)
    print(resultado)
else:
    n1 = float(input("Primeiro número: "))
    n2 = float(input("Segundo número: "))
    div = n1/n2
    resultado = float(div)
    print(resultado)
