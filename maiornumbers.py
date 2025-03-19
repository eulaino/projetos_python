
n1 = float(input("Qual o primeiro número: "))
n2 = float(input("Qual o segundo número: "))

def numbers(num1,num2):
    if num1 > num2:
        print(f"O {num1} é maior que o {num2}")
    elif num1 < num2:
        print(f"O {num2} é maior que o {num1}")
    elif num1 == num2:
        print(f"{n1} é igual a {n2}")
    else:
        print("Números não compreendidos")

resultado = numbers(n1,n2)


