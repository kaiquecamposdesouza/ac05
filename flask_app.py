from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##### Configurar o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bancoDeDados.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#####


class Apontamento(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(25), nullable=True)
    sobrenome = db.Column(db.String(25), nullable=True)
    email = db.Column(db.String(25), nullable=True)
    assunto = db.Column(db.String(25), nullable=True)
    mensagem = db.Column(db.String(25), nullable=True)
    


    @property
    def serializar(self):
        return {

            'id': self.id,
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem
            
        }

db.create_all()

@app.route('/inicio')
@app.route('/')
def mostra_inicio():
    return render_template('contato.html')

@app.route('/login', methods=['GET', 'POST'])
def funcionarios():
    if request.method == 'GET':
        print(request.form['nome'])
        usuario = Apontamento(nome=request.form['nome'], sobrenome=request.form['sobrenome'], email=request.form['email'], assunto=request.form['assunto'], mensagem=request.form['mensagem'])
        db.session.add(usuario)
        db.session.commit()
        return render_template('contato.html')

    if request.method == 'POST':
        ultimos10 = Apontamento.query.order_by(-Apontamento.id).limit(10).all()
        print(ultimos10)
        return jsonify(contato=[i.serializar for i in ultimos10])