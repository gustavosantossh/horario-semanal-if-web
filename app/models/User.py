import sqlite3

class User:
    def __init__(self):
        self.conn = sqlite3.connect("app/database/horario_semanal_if.db")
        
        self.cursor = self.conn.cursor()
      
    # def create(self, email: str, senha: str):
    #     if not email or not senha:
    #         return False
    #     else:
    #         try:
    #             hashPassword = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
    #             query = f"INSERT INTO user (email, senha) VALUES (?, ?)"
    #             self.cursor.execute(query, (email, hashPassword))
    #             self.conn.commit()               
    #             self.conn.close()
                
    #             return True
                
    #         except sqlite3.IntegrityError as e:
    #             print(e)
    
    # def loginUser(self, email: str, senha: str) -> bool:
    #     try: 
    #         query = f'SELECT email, senha from user WHERE email = ?'
    #         self.cursor.execute(query, (email,))
    #         resultado = self.cursor.fetchone()
            
    #         if resultado:
    #             verifyPassword = bcrypt.checkpw(senha.encode(), resultado[1])
    #         else:
    #             return False
            
    #         self.cursor.close()
    #         self.conn.close()
            
    #     except sqlite3.Error as e:
    #         print(e)
        
    #     if verifyPassword and resultado:
    #         return True
    #     else:
    #         return False
    
    def email_existe(self, email):
        self.cursor.execute("SELECT email from user WHERE email = ?", (email,))
        return self.cursor.fetchone() is not None
            