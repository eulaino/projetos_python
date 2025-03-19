cargo = input("Digite qual cargo você exerce na empresa: ")
horasext = float(input("Digite as horas extras trabalhadas: "))
faltas = int(input("Digite quantas faltas você possui na empresa: "))
filhos = int(input("Digite quantos filhos você possui: "))

#Condição para obter salário de cada cargo
if cargo == "gerente":
    salario = 2000
elif cargo == "supervisor":
    salario = 900
elif cargo == "servente":
    salario = 300
else:
    print("Cargo não encontrado.")

#Cálculo das horas extras
horaextcalc = (((salario)/240)*2)*horasext

#Cálculo das faltas
faltascalc = ((salario)/30)*faltas

#Cálculo de filhos
filhoscalc = ((salario)*3/100)*filhos

#Proventos
proventos = (salario+horaextcalc+filhoscalc)

#INSS
inss = (proventos)*(10/100)

#Descontos
descontos = (faltascalc+inss)

#Salário Líquido
salarioliq = round(float(proventos-descontos),2)

print("Seu salário líquido é de: R$",salarioliq)
