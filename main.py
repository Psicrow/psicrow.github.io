from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/arquivos')
def arquivos():
    return render_template('arquivos.html')

lista_users =['nome1','nome2','nome3']
@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html',lista_users=lista_users)

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)