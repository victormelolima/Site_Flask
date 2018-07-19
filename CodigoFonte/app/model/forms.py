from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, FileField, FloatField, TextField
from wtforms.validators import DataRequired

class LoginForm(Form):
	email = StringField("email", validators=[DataRequired()])
	senha = PasswordField("senha", validators=[DataRequired()])
	lembrar = BooleanField("lembrar")	


class RegistrarForm(Form):
	nome =  StringField("nome", validators=[DataRequired()])
	cpf =  StringField("cpf", validators=[DataRequired()])
	imagem =  FileField("imagem")
	email = StringField("email", validators=[DataRequired()])
	senha = PasswordField("senha", validators=[DataRequired()])


class RegistrarCursoForm(Form):
	titulo = StringField("titulo", validators=[DataRequired()])
	descricao = TextField("descricao", validators=[DataRequired()])
	valor =	FloatField("valor", validators=[DataRequired()])

class RegistrarAulaForm(Form):
	tituloAula = StringField("tituloAula", validators=[DataRequired()])
	descricaoAula = TextField("descricaoAula", validators=[DataRequired()])
	
class RegistrarVideoForm(Form):
	videoEndereco = FileField("videoEndereco", validators=[DataRequired()])
	descricaoVideo = TextField("descricaoVideo", validators=[DataRequired()])