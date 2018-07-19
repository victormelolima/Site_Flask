from flask import render_template, redirect, url_for
from app import app, db, lm
from app.model.forms import *
from app.model.tables import *
from flask_login import login_user, logout_user
from sqlalchemy import desc

@lm.user_loader
def load_user(idPessoa):
	return Pessoa.query.filter_by(idPessoa=idPessoa).first()

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/base')
def base():
	return render_template("base.html")

@app.route('/login', methods=["GET", "POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
	 	pes = Pessoa.query.filter_by(email=form.email.data).first()
	 	if pes and pes.senha==form.senha.data:
	 		login_user(pes)		
	 		return redirect(url_for("index"))
	 	else:
	 		return render_template("login.html", form=form, mens="Nome de Usuário ou senha Incorretos!")
	else:
		return render_template("login.html", form=form)

@app.route('/registrar', methods=["GET", "POST"])
def registrar():
	form = RegistrarForm()
	if form.validate_on_submit():
		dados = Pessoa(form.nome.data, form.email.data, form.senha.data, form.imagem.data, form.cpf.data)
		db.session.add(dados)
		db.session.commit()
		form = LoginForm()
		return redirect(url_for("login"))
	else:
		return render_template("registrar.html", form=form)

@app.route('/logout')
def sair():
	logout_user()
	return redirect(url_for("index"))

@app.route('/cadastrarCurso')
@app.route('/cadastrarCurso/<int:idPessoa>', methods=["GET", "POST"])
def cadastrarCurso(idPessoa):
	form = RegistrarCursoForm()
	if form.validate_on_submit():
		dados = Curso(form.titulo.data, form.descricao.data, form.valor.data)
		db.session.add(dados)
		db.session.commit()
		cursos = Curso.query.order_by(desc(Curso.idCurso)).first()
		idCurso = cursos.idCurso
		dadosmc = MinistraCurso(idPessoa, idCurso)
		db.session.add(dadosmc)
		db.session.commit()
		return redirect(url_for("listarMeusCursos", idPessoa=idPessoa))
	else:
		return render_template("cadastrarcurso.html", form=form)


@app.route('/listarCursos')
def listarCursos():
	cursos = Curso.query.all()
	return render_template("listacursos.html", cursos=cursos)


@app.route('/listarCursos/<int:idPessoa>')
def listarMeusCursos(idPessoa):
	cursaCursos = CursaCurso.query.filter_by(pessoa=idPessoa).all()
	ministraCursos = MinistraCurso.query.filter_by(pessoa=idPessoa).all()
	return render_template("meuscursos.html", cursaCursos=cursaCursos, ministraCursos=ministraCursos )


@app.route('/inscrever/<int:idPessoa>/<int:idCurso>')
def inscrever(idPessoa, idCurso):
	dados = CursaCurso(idPessoa, idCurso)
	db.session.add(dados)
	db.session.commit()
	return redirect(url_for("listarMeusCursos", idPessoa=idPessoa))


@app.route('/perfil/<int:idPessoa>', methods=["GET", "POST"])
def perfil(idPessoa):
	p = Pessoa.query.get(idPessoa);
	form = RegistrarForm()
	if form.validate_on_submit():
		p.nome = form.nome.data
		p.email = form.email.data 
		p.senha = form.senha.data 
		p.imagem = form.imagem.data
		p.cpf = form.cpf.data 
		db.session.add(p)
		db.session.commit()
		return redirect(url_for("perfil", idPessoa=idPessoa))
	form.nome.data = p.nome
	form.email.data = p.email
	form.senha.data = p.senha
	form.imagem.data = p.imagem
	form.cpf.data = p.cpf
	return render_template("perfil.html", form=form)


@app.route('/cursodetalhes/<int:idCurso>')
def cursoDetalhes(idCurso):
	ministraCursos = MinistraCurso.query.filter_by(curso=idCurso).first()
	print(ministraCursos)
	curso = Curso.query.get(idCurso)
	aula = Aula.query.filter_by(curso=idCurso).order_by(Aula.numero).all()
	return render_template('cursodetalhes.html', aula=aula, curso=curso, ministraCursos=ministraCursos)


@app.route('/addaula/<int:idCurso>', methods=["GET", "POST"])
def addAula(idCurso):
	form1 = RegistrarAulaForm()
	form2 = RegistrarVideoForm()
	if form1.validate_on_submit() and form2.validate_on_submit():
		numAula1 = Aula.query.filter_by(curso=idCurso).order_by(desc(Aula.numero)).first()
		if numAula1:
			numAula = numAula1.numero+1
		else:
			numAula = 1
		aula = Aula(idCurso, numAula, form1.tituloAula.data, form1.descricaoAula.data, 0)
		db.session.add(aula)
		db.session.commit()
		a = Aula.query.filter_by(curso=idCurso).order_by(desc(Aula.idAula)).first()
		al = a.idAula
		video = Video(al, form2.videoEndereco.data, form2.descricaoVideo.data )
		db.session.add(video)
		db.session.commit()
		return redirect(url_for("cursoDetalhes", idCurso=idCurso))
	return  render_template("addaula.html", form1=form1, form2=form2)


@app.route('/acompanharaula/<int:idAula>')
def acompanharAula(idAula):
	aula = Aula.query.get(idAula)
	video = Video.query.filter_by(aula=idAula).first()
	print(video)
	#	print(descricaoVideo)
	return  render_template("acompanharaula.html", aula=aula, video=video)