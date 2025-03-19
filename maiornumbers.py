
def numbers(num1,num2):
    if num1 > num2:
        print(f"O {num1} é maior que o {num2}")
    elif num1 < num2:
        print(f"O {num2} é maior que o {num1}")
    else:
        print("Números não compreendidos")

n1 = input("Qual o primeiro número: ")
n2 = input("Qual o segundo número: ")
resultado = numbers(n1,n2)
print(resultado)


