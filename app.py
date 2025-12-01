from flask import Flask, render_template

app = Flask(__name__)

# ROTAS DO PROTÓTIPO (estáticas)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/perfil")
def perfil():
    return render_template("perfil.html")

@app.route("/pre-cadastro")
def pre_cadastro():
    return render_template("pre-cadastro.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")


# ROTA PING (opcional para test)
@app.route("/ping")
def ping():
    return {"status": "ok", "message": "Ministerium backend ativo"}

if __name__ == "__main__":
    app.run(debug=True)
