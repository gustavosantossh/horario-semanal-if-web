import sqlite3

class Horario:
    def __init__(self):
        self.conn = sqlite3.connect("app/database/horario_semanal_if_web.db", check_same_thread=False)

        self.cursor = self.conn.cursor()

    def searchAll(self) -> list:
        try:
            query = f"SELECT * FROM horarios"
            self.cursor.execute(query)
            self.conn.commit()
            
            return self.cursor.fetchall()
        except:
            pass
        
    def searchHorario(self, data: str) -> list:
        try:
            query = f"SELECT * FROM horarios WHERE turma LIKE ? OR curso LIKE ?"
            param = f"%{data}%"
            self.cursor.execute(query, (param, param))
            self.conn.commit()
            
            return self.cursor.fetchall()
        except Exception as e:
           print(f"Nenhum dado retornado. Erro: {e}")
           return []
       
    def findHorarioEdit(self, id):
        searchHorarioById = f"SELECT * FROM horarios WHERE id = ?"
        self.cursor.execute(searchHorarioById, (id,))

        resultado = self.cursor.fetchall()

        return resultado
    
    def editar(self, turma: str, curso: str, disciplina: str, dia_semana: str, horario_aula: str, sala: str, professor: str, id) -> bool:
        try:
            query = f"UPDATE horarios SET turma = ?, curso = ?, disciplina = ?, dia_da_semana = ?, horario_da_aula = ? , sala = ?, professor = ? where id = ?"

            self.cursor.execute(query, (turma, curso, disciplina, dia_semana, horario_aula, sala, professor, id))
            self.conn.commit()
            
            return True
        except sqlite3.Error as e:
            print("Tente novamente: ", e)
        
            
    def create(self, turma: str, curso: str, disciplina: str, dia_semana: str, horario_aula: str, sala: str, professor: str) -> bool:
        try:

            query = f"INSERT INTO horarios (turma, curso, disciplina, dia_da_semana, horario_da_aula, sala, professor) VALUES (?, ?, ?, ?, ?, ?, ?)"

            self.cursor.execute(query, (turma, curso, disciplina, dia_semana, horario_aula, sala, professor,))
            self.conn.commit()
            
            return True
        except sqlite3.Error as e:
            print("Error: ", e)
            return False
            
    def delete(self, id) -> bool:
        try:
            query = f"DELETE FROM horarios WHERE id = ?"

            self.cursor.execute(query, (id,))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"erro: {e}")
            return False