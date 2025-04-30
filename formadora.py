def calcular_media(notas):
    return sum(notas) / len(notas)

cursos_disponiveis = ("Python", "Java", "JavaScript")
alunos = []
cpfs_cadastrados = set()
print(f"Olá, confira nossos cursos: {cursos_disponiveis[0]}, {cursos_disponiveis[1]}, {cursos_disponiveis[2]}")
while True:
    cpf = input("Digite o CPF do aluno: ")
    cpf = cpf.replace("-", "")
    if len(cpf) < 11:
        print(f"O CPF {cpf} contém menos que 11 dígitos!")
        break
    if cpf in cpfs_cadastrados:
        print("CPF CADASTRADO.")
        continue
    nome = input("Nome: ")
    curso = input("Curso: ")
    for i in range(3):
        notas = [float(input(f"Nota {i+1}: "))]
    media = calcular_media(notas)
    situacao = "Aprovado" if media >= 7 else "Reprovado"

    aluno = {
        "nome": nome,
        "cpf": cpf,
        "curso": curso,
        "notas": notas,
        "media": media,
        "situacao": situacao
    }

    alunos.append(aluno)
    cpfs_cadastrados.add(cpf)

    continuar = input("Deseja cadastrar outro aluno? (s/n): ")
    if continuar.lower() != 's':
        break

for nome in alunos:
    nome_aluno = nome['nome']
    cpf_aluno = nome['cpf']
    media_aluno = nome['media']
    situacao = nome['situacao']
    curso = nome['curso']

    print(f"Nome do Aluno: {nome_aluno}")
    print(f"CPF do Aluno: {cpf_aluno}")
    print(f"Média do Aluno: {media_aluno}")
    print(f"Situação do Aluno: {situacao}\n")
    tables = f""" <tr>
                    <td>{nome_aluno}</td><td>{cpf_aluno}</td><td>{curso}</td><td>{media_aluno}</td><td>{situacao}</td>
                </tr> """



arquivo = open("index.html", "w")
conteudo_html = """
        <html>
        <head>
            <style>
                table {
                    width: 80%;
                    margin: 20px auto;
                    border-collapse: collapse;
                    font-family: Arial;
                }
                th, td {
                    border: 1px solid #999;
                    padding: 8px;
                    text-align: center;
                }
                th {
                    background-color: #f2f2f2;
                }
                .aprovado {
                    background-color: #d4edda;
                }
                .reprovado {
                    background-color: #f8d7da;
                }
            </style>
        </head>
        <body>
            <h2 style="text-align:center;">Relatório de Alunos</h2>
            <table>
                <tr>
                    <th>Nome</th><th>CPF</th><th>Curso</th><th>Média</th><th>Situação</th>
                </tr>
                """+tables+"""
            </table>
        </body>
        </html>

    """
arquivo.write(conteudo_html)
arquivo.close()
