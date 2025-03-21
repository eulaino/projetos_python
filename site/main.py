from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def page():
    return render_template("page.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    if nome_usuario == "laino":
        return render_template("usuarios.html", cargo="adm", nome_usuario=nome_usuario)
    else:
        return render_template("usuarios.html", cargo="user", nome_usuario=nome_usuario)
    
@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":  
    app.run(debug=True)