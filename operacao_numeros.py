
n1 = float(input("Qual o primeiro número: "))
n2 = float(input("Qual o segundo número: "))
operacao = input("Qual operação deseja fazer: ")

#Relação entre os números
def numbers(num1,num2):
    if num1 > num2:
        print(f"O {num1} é maior que o {num2}")
    elif num1 < num2:
        print(f"O {num2} é maior que o {num1}")
    elif num1 == num2:
        print(f"{n1} é igual a {n2}")
    else:
        print("Números não compreendidos")

#Operação
def operar(num1,num2):
    if operacao == "soma":
        soma = num1+num2
        print(f"O valor da soma é: {soma}")
    elif operacao == "subtração" or "subtrair" or "subtracao":
        sub = num1-num2
        print(f"O valor da subtração é: {sub}")
    else:
        print("Erro na operação!")

#Resultado
numbers(n1,n2)
operar(n1,n2)



