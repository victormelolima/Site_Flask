from app import db
from sqlalchemy import Table, Column, Integer, String, ForeignKey, String, Boolean

class Pessoa(db.Model):
	__tablename__ = "pessoas"

	idPessoa = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(200)) 
	email = db.Column(db.String(100), unique=True)
	senha = db.Column(db.String(100))
	imagem = db.Column(db.String(1000))
	cpf = db.Column(db.String(20))


	@property
	def is_authenticated(self):
		return True


	@property
	def is_active(self):
		return True	


	@property
	def is_anonymous(self):
		return False


	
	def get_id(self):
		return str(self.idPessoa)	


	def __init__(self, pnome, pemail, psenha, pimagem, pcpf):
		self.nome = pnome 
		self.email = pemail
		self.senha = psenha
		self.imagem = pimagem
		self.cpf = pcpf
	def __repr__(self):
		return "<Pessoa(idPessoa={0}, nome=\"{1}\", email=\"{2}\", CPF=\"{3}\", senha=\"{4}\", imagem=\"{5}\")>'.format( self.idPessoa, self.nome, self.email, self.senha, self.imagem)"

class Curso(db.Model):
	__tablename__ = "cursos"

	idCurso = db.Column(db.Integer, primary_key=True)
	titulo= db.Column(db.String(1000)) 
	descricao = db.Column(db.Text)
	valor = db.Column(db.Float)
	def __init__(self, ctitulo, cdescricao, cvalor):
		self.titulo = ctitulo 
		self.descricao = cdescricao
		self.valor = cvalor
	
	def __repr__(self):
		return "<Curso(idCurso={0}, Titulo=\"{1}\", Descricao=\"{2}\", Valor=\"{3}\")>'.format( self.idCurso, self.titulo, self.descricao, self.valor)"

class CursaCurso(db.Model):
	__tablename__ = "cursaCurso"

	idCursaCurso = db.Column(db.Integer, primary_key=True)
	pessoa = db.Column(db.Integer, db.ForeignKey('pessoas.idPessoa')) 
	curso = db.Column(db.Integer, db.ForeignKey('cursos.idCurso'))
	pessoaDado = db.relationship('Pessoa', foreign_keys=pessoa) 
	cursoDado = db.relationship('Curso', foreign_keys=curso)
	def __init__(self, pid, cid):
		self.pessoa = pid 
		self.curso = cid
	def __repr__(self):
		return "<CursaCurso(idCursaCurso={0}, Pessoa=\"{1}\", Curso=\"{2}\", PessoaDado=\"{3}\", cursoDado=\"{4}\")>'.format( self.idCursaCurso, self.pessoa, self.curso, self.pessoaDado, self.cursoDado)"

class MinistraCurso(db.Model):
	__tablename__ = "ministraCurso"

	idMinistraCurso = db.Column(db.Integer, primary_key=True)
	pessoa = db.Column(db.Integer, db.ForeignKey('pessoas.idPessoa'))
	curso = db.Column(db.Integer, db.ForeignKey('cursos.idCurso'))
	pessoaDado = db.relationship('Pessoa', foreign_keys=pessoa) 
	cursoDado = db.relationship('Curso', foreign_keys=curso) 
	def __init__(self, pid, cid):
		self.pessoa = pid
		self.curso = cid
	def __repr__(self):
		return "<CursaCurso(idMinistraCurso={0}, Pessoa=\"{1}\", Curso=\"{2}\", PessoaDado=\"{3}\", cursoDado=\"{4}\")>'.format( self.idMinistraCurso, self.pessoa, self.curso, self.pessoaDado, self.cursoDado)"

class Aula(db.Model):
	__tablename__ = "aulas"

	idAula = db.Column(db.Integer, primary_key=True)
	curso = db.Column(db.Integer, db.ForeignKey('cursos.idCurso')) 
	numero = db.Column(db.Integer)
	tituloAula = db.Column(db.Text)
	descricaoAula = db.Column(db.Text)
	status = db.Column(db.Boolean)
	cursoDado = db.relationship('Curso', foreign_keys=curso) 
	def __init__(self, curso, numAula, titulo, descricao, status):
		self.curso = curso
		self.numero = numAula
		self.descricaoAula = descricao
		self.tituloAula = titulo
		self.status = status
	def __repr__(self):
		return "<Aula(idAula={0}).format( self.idAula)"


class Video(db.Model):
	__tablename__ = "videos"

	idVideo = db.Column(db.Integer, primary_key=True)
	aula = db.Column(db.Integer, db.ForeignKey('aulas.idAula')) 
	videoEndereco = db.Column(db.Text)
	descricaoVideo = db.Column(db.Text)
	aulaDado = db.relationship('Aula', foreign_keys=aula) 
	def __init__(self, vaula, vEndereco, vDescricao):
		self.aula = vaula
		self.videoEndereco = vEndereco
		self.descricaoVideo = vDescricao
	def __repr__(self):
		return "<Video(idVideo={0}, aula=\"{1}\", videoEndereco=\"{2}\", descricaoVideo=\"{3}\")>'.format( self.idVideo, self.aula, self.videoEndereco, self.descricaoVideo)"