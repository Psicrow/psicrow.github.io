from flask_wtf import Flaskform
from wtforms import StringField, PasswordField, SubmitField
from wtfforms.validators import DataRequided, Lenght, Email, Equalto

class FormCriarConta(Flaskform):
    username = StringField('Nome de Usuario', validators=[DataRequided()])
    email = StringField('E-mail', validators=[DataRequided(),Email()])
    senha = PasswordField('Senha', validators=[DataRequided(), Lenght(6)])
    confirmacao_senha = PasswordField('Confirmar Senha', validators=[DataRequided(), Equalto('senha')])
    botao_submit = SubmitField('Criar Conta')

class FormLogin(Flaskform):
    username = StringField('Username ou Email', validators=[DataRequided()])
    senha = PasswordField('Senha', validators=[DataRequided()])
    botao_submit = SubmitField('Entrar')