from flask import Flask, render_template, request, redirect
from pessoa import Pessoa


lista = []

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html', titulo = 'Lista Pessoas', pessoas = lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo = 'Cadastro Pessoa')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    altura = request.form['altura']

    pessoas = Pessoa(nome, idade, altura)

    lista.append(pessoas)

    return redirect('/')


app.run(debug=True)