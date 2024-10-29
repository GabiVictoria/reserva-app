from flask import Flask, render_template, request, redirect, url_for
from reserva_app import metodos

app = Flask("reservas")

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/cadastro")
def cadastro():
    return render_template('cadastro.html')

@app.route("/cadastro", methods = ['POST'])
def cadastrar_pessoa():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['password'] 
    admin = False
    metodos.save_cadastro(nome, admin, email, senha )
    return render_template('login.html')

@app.route("/cadastrar_sala")   
def cadastrar_sala():
    return render_template('cadastrar-sala.html')

@app.route("/cadastrar_sala", methods = ['POST'])
def formulario_sala():
    tipo = request.form['tipo'].strip()
    descricao = request.form['descricao'].strip()
    capacidade = request.form['capacidade'].strip() 
    ativo = True
    metodos.save_salas(tipo, descricao, capacidade, ativo)
    return render_template('listar-salas.html', salas = metodos.get_salas())
    

@app.route("/reservar_sala")
def reservarsala(): 
    return render_template("reservar-sala.html", salas = metodos.get_salas())


@app.route("/reservar_sala", methods = ['POST'])
def reservar_sala():
    sala = request.form['sala']
    d_inicio = request.form['inicio']
    d_fim = request.form['fim']
    ativo = True
    metodos.save_reservas( sala, d_inicio, d_fim, ativo)

    reserva = {
        "sala": sala,
        "inicio": d_inicio,
        "fim": d_fim,
        "ativo": ativo
    }

    return render_template('reserva/detalhe-reserva.html', reservas = reserva)

@app.route("/listar_salas")
def listar_sala():
    return render_template('listar-salas.html', salas = metodos.get_salas())

@app.route("/templates/reservas")
def reservas():
    return render_template('reservas.html')

@app.route("/detalhe_reserva")
def detalhe_reserva():
    return render_template('reserva/detalhe-reserva.html')

app.run()