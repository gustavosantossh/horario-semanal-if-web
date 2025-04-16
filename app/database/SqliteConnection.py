import sqlite3

class SqliteConnection():
    def __init__(self):
        self.conn = sqlite3.connect("app/database/horario_semanal_if_web.db")
        
        self.cursor = self.conn.cursor()
        
        self.tables()
        
    def tables(self):
        # TABELA DE USUARIOS
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email VARCHAR(255) UNIQUE,
            senha VARCHAR(255)
        )             
        """)
        
        # TABELA HORARIOS
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS horarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            turma VARCHAR(255),
            curso VARCHAR(255),
            disciplina VARCHAR(255),
            dia_da_semana VARCHAR(255),
            horario_da_aula VARCHAR(255),
            sala VARCHAR(255),
            professor VARCHAR(255)
            )    
        """)
            

