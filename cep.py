import requests

cep = input("Digite o cep: ")
#alterar caso tenha (-)(.)( ) no cep
cep = cep.replace("-", "").replace(".","").replace(" ","")

#tamanho do cep tem que ser 8
if len(cep) == 8:
    link = f'https://viacep.com.br/ws/{cep}/json/'
    requesicao = requests.get(link)
    dicreq = requesicao.json()
    logradouro = dicreq['logradouro']
    complemento = dicreq['complemento']
    bairro = dicreq['bairro']
    uf = dicreq['uf']
    estado = dicreq['estado']
    regiao = dicreq['regiao']
    ddd = dicreq['ddd']
    print(f"CEP: {cep}\nLogradouro: {logradouro}\nComplemento: {complemento}\nBairro: {bairro}\nUF: {uf}\nEstado: {estado}\nRegião: {regiao}\nDDD: {ddd}")
else:
    print("CEP INVÁLIDO")