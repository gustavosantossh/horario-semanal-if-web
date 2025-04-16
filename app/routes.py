from flask import render_template, url_for, request, redirect
from app.models.Horario import Horario

class Route:
    def __init__(self, app):
        self.rotas(app)
        self.Horario = Horario()
        self.data = [] 
        
    def rotas(self, app):
        @app.route("/")
        def index():
            self.data = self.Horario.searchAll()
            return render_template("index.html", data=self.data)
        
        @app.route("/create")
        def create():
            return render_template("create.html")
        
        @app.route("/store", methods=['POST'])
        def store():
            try:
                if request.method == "POST":
                    turma = request.form.get('turma')
                    curso = request.form.get('curso')
                    disciplina = request.form.get('disciplina')
                    dia_da_semana = request.form.get('dia_da_semana')
                    horario = request.form.get('horario')
                    sala = request.form.get('sala')
                    professor = request.form.get('professor')
                                        
                    salvar = self.Horario.create(turma, curso, disciplina, dia_da_semana, horario, sala, professor)
                    
                    if salvar:
                        return redirect(url_for("index"))  
                    else:
                        return "Error ao salvar os dados"
                    
            except Exception as e:
                return f"Ops, algo deu errado: {e}"
        
        @app.route("/editar/<int:id>")
        def editar(id):
            self.data = self.Horario.findHorarioEdit(id)
            return render_template("editar.html", data=self.data)
        
        @app.route("/deletar/<int:id>")
        def deletar(id):
            response = self.Horario.delete(id)
            
            if response:
                return redirect(url_for('index'))
            else:
                return "Error ao deletar"
            
        @app.route("/filtro")
        def filtro():
            filtro = request.args.get('search')
            
            if filtro:
                self.data = self.Horario.searchHorario(filtro)
            else:
                self.data = self.Horario.searchAll()
            
            return render_template("index.html", data=self.data)
        
        @app.route("/update/<int:id>", methods=['POST'])
        def update(id):
            try:
                if request.method == "POST":
                    turma = request.form.get('turma')
                    curso = request.form.get('curso')
                    disciplina = request.form.get('disciplina')
                    dia_da_semana = request.form.get('dia_da_semana')
                    horario = request.form.get('horario')
                    sala = request.form.get('sala')
                    professor = request.form.get('professor')
                                        
                    salvar = self.Horario.editar(turma, curso, disciplina, dia_da_semana, horario, sala, professor, id)
                    
                    if salvar:
                        return redirect(url_for("index"))  
                    else:
                        return "Error ao salvar os dados"
                    
            except Exception as e:
                return f"Ops, algo deu errado: {e}"