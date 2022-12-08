from flask import Flask,render_template
from pessoa import Pessoa

#Variavel de referencia FLask
app = Flask(__name__)

#Criando Rota   
@app.route("/")
def inicio():
    pessoa1 = Pessoa('Felipe','30','1.80')
    pessoa2 = Pessoa('Haiko','15','1.50')
    pessoa3 = Pessoa('Jean','42','1.95')

    lista = [pessoa1, pessoa2, pessoa3]

    return render_template("index.html", titulo = "Tabela", pessoas = lista)

@app.route("/novo")
def novo():
    return "Titulo Rota Nova"

#Iniciando
app.run()