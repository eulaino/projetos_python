#Saída
verif = int(input("Digite o número: "))

#Cálculo
def verificar(number):
    if number % 2 == 0:
        print("O número é par.")
    else:
        print("O número é impar.")

#Resultado
resultado = verificar(verif)


