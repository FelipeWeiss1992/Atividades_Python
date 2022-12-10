from flask import Flask, render_template, request, redirect
from pessoa import Pessoa

pessoa1 = Pessoa('Felipe', '30', 1.81)
pessoa2 = Pessoa('Haiko', '17', 1.75)
pessoa3 = Pessoa('Jean', '40', 1.85)


lista = [pessoa1,pessoa2,pessoa3]

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

    pessoa = Pessoa(nome, idade, altura)

    lista.append(pessoa)

    return redirect('/')


app.run(debug=True)