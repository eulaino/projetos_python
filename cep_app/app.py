import customtkinter as ctk
import requests
import time

ctk.set_appearance_mode('dark')

def validar_cep():
    cep = campo_cep.get()
    cep = cep.replace("-", "").replace(".","").replace(" ","")
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
        resultado_log.configure(text=f"Logradouro: {logradouro}")
        resultado_com.configure(text=f"Complemento: {complemento}")
        resultado_bai.configure(text=f"Bairro: {bairro}")
        resultado_uf.configure(text=f"UF: {uf}")
        resultado_est.configure(text=f"Estado: {estado}")
        resultado_reg.configure(text=f"Região: {regiao}")
        resultado_reg.configure(text=f"DDD: {ddd}")
    else:
        resultado_log.configure(text="CEP INVÁLIDO") 
        

app = ctk.CTk()
app.title("Sistema de Login")
app.geometry('320x340')

#campo label
labelcep = ctk.CTkLabel(app,text="CEP:")
labelcep.pack(pady=10)

#campo form
campo_cep = ctk.CTkEntry(app,placeholder_text='Digite o CEP')
campo_cep.pack(pady=10)

#button
botao_cep = ctk.CTkButton(app,text="Verificar CEP", command=validar_cep)
botao_cep.pack(pady=10)


#resultado
#resultado_cep = ctk.CTkLabel(app,text="")
resultado_log = ctk.CTkLabel(app,text="")
resultado_com = ctk.CTkLabel(app,text="")
resultado_bai = ctk.CTkLabel(app,text="")
resultado_uf = ctk.CTkLabel(app,text="")
resultado_est = ctk.CTkLabel(app,text="")
resultado_reg = ctk.CTkLabel(app,text="")
resultado_ddd = ctk.CTkLabel(app,text="")

#resultado_cep.pack()
resultado_log.pack()
resultado_com.pack()
resultado_bai.pack()
resultado_uf.pack()
resultado_est.pack()
resultado_reg.pack()
resultado_ddd.pack()

app.mainloop()