from flask import Flask, render_template, redirect, request
from models.cerveja import Cerveja

app=Flask(__name__)
lista_cervejas = []

@app.route('/')
def inc():
    return render_template('index.html', nome_pag = "Inicial")

@app.route('/listar')
def listar():
    return render_template('listar.html', nome_pag = "Listar", lista = lista_cervejas)

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html', nome_pag = "Cadastrar")

@app.route('/salvar', methods = ["POST"])
def salvar():
    nome = request.form["nome"]
    tipo = request.form["tipo"]
    preço = request.form["preço"]
    validade = request.form["validade"]
    nova_cerveja = Cerveja(nome, tipo, preço, validade)
    lista_cervejas.append(nova_cerveja)
    return redirect ("/listar")
    

@app.route('/fazer-pedido')
def fazerPedido():
    return render_template('fazer-pedido.html', nome_pag = "Fazer Pedido")

@app.route('/Efetuar Pedido', methods = ["POST"])
def efeutar_pedido():
    return "Efetuar Pedido"


    
app.run()