cargo = input("Digite qual cargo você exerce na empresa: ")
horasext = float(input("Digite as horas extras trabalhadas: "))
faltas = int(input("Digite quantas faltas você possui na empresa: "))
filhos = int(input("Digite quantos filhos você possui: "))

#Condição para obter salário de cada cargo
match cargo:
    case "gerente":
        salario = 2000
    case "supervisor":
        salario = 900
    case "servente":
        salario = 300
    case _:
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
salarioliq = round(float(proventos-descontos),3)

print(f"Salário líquido: R${salarioliq}")
