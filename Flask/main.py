from flask import Flask,render_template, request, redirect
from pessoa import Pessoa


pessoa1 = Pessoa('Felipe','30','1.80')
pessoa2 = Pessoa('Haiko','15','1.50')
pessoa3 = Pessoa('Jean','42','1.95')

lista = [pessoa1, pessoa2, pessoa3]
#Variavel de referencia FLask
app = Flask(__name__)

#Criando Rota   
@app.route("/")
def inicio():

    return render_template("index.html", titulo = "Lista Pessoas", pessoas = lista)

@app.route("/cadastrar")
def novo():
    return render_template('novo.html', titulo = 'Cadastro Pessoa')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    altura = request.form['altura']

    pessoa = Pessoa(nome, idade, altura)
    lista.append(pessoa)

    return redirect ('/')

#Iniciando

app.run(debug=True)

