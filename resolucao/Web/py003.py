from flask import Flask, render_template, request, redirect
from alunos import Alunos
app = Flask(__name__)


pagina_nome = "SÓCIO-TORCEDOR"
aluno1 = Alunos("Lucas", "Nascimento Silva", 47999452020)
aluno2 = Alunos("Lucas", "Nascimento Silva", 47999452121)
aluno3 = Alunos("Lucas", "Nascimento Silva", 47999462323)
aluno4 = Alunos("Lucas", "Nascimento Silva", 47999472525)
aluno5 = Alunos("Lucas", "Nascimento Silva", 47999482626)
lista_alunos = [aluno1, aluno2, aluno3, aluno4, aluno5]



#print(aluno1.nome_completo())
@app.route("/")
def Inicio():
    return render_template("index.html", Nome=pagina_nome, lista = lista_alunos)


@app.route("/novo")
def novo():
    return render_template("novo.html")

@app.route("/salvar", methods = ["POST"])
def salvar():
    nome = request.form["nome"]
    sobrenome = request.form["sobrenome"]
    telefone = request.form["telefone"]
    alunoNovo = Alunos (nome, sobrenome, telefone)
    lista_alunos.append(alunoNovo)
    return redirect("/")
app.run()