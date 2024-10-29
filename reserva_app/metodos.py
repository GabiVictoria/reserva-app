from .conexao_bd import conexao_fechar, conexao_abrir

def get_cadastro():
   con = conexao_abrir("127.0.0.1", "estudante1", "estudante1", "reservas_bd")
  
   cursor = con.cursor()
   sql = "SELECT * FROM Usuarios"
   # Criando o cursor com a opção de retorno como dicionário  
   cursor = con.cursor(dictionary=True)
   cursor.execute(sql)

   for (registro) in cursor:
       print(str(registro['id_usuario']) + " - "+ registro['nome'])
       

   cursor.close()
   conexao_fechar(con)



def save_cadastro( nome, admin, email, senha):
    con = conexao_abrir("127.0.0.1", "estudante1", "estudante1", "reservas_bd")

    cursor = con.cursor()
    sql = "INSERT INTO Usuarios (nome, adm, email, senha) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, ( nome, admin, email, senha))
    con.commit()
    cursor.close()

    conexao_fechar(con)

def get_salas():
   con = conexao_abrir("127.0.0.1", "estudante1", "estudante1", "reservas_bd")

   cursor = con.cursor()
   sql = "SELECT * FROM Salas"
   # Criando o cursor com a opção de retorno como dicionário  
   cursor = con.cursor(dictionary=True)
   cursor.execute(sql)

   salas = []
    
    # Iterando sobre os registros e adicionando-os à lista
   for registro in cursor:
        salas.append({
            "id_salas": registro["id_salas"],
            "tipo": registro["tipo"]
        })

   cursor.close()
   conexao_fechar(con)
   return salas
   
def save_salas( tipo, descricao, capacidade, ativo):     
    con = conexao_abrir("127.0.0.1", "estudante1", "estudante1", "reservas_bd")
  
    cursor = con.cursor()
    sql = "INSERT INTO Salas ( tipo, descricao, capacidade, ativo_salas) VALUES ( %s, %s, %s, %s)"
    cursor.execute(sql, ( tipo, descricao, capacidade, ativo))
    con.commit()
    cursor.close()
    
    conexao_fechar(con)

def main():
    con = conexao_abrir("127.0.0.1", "estudante1", "estudante1", "reservas_bd")
  
    save_salas(con, "sala de quimica", "sim" ,"45", True)
    get_salas(con)

    conexao_fechar(con)


def get_reservas():
   con = conexao_abrir("127.0.0.1", "estudante1", "estudante1", "reservas_bd")

   cursor = con.cursor()
   sql = "SELECT * FROM Reservas"
   # Criando o cursor com a opção de retorno como dicionário  
   cursor = con.cursor(dictionary=True)
   cursor.execute(sql)
   conexao_fechar(con)

   for (registro) in cursor:
       print(str(registro['id_reserva']) + " - "+ str(registro['fk_Salas_id_salas']))

   cursor.close()


   
def save_reservas(  sala, d_inicio, d_fim, ativo):  
    con = conexao_abrir("127.0.0.1", "estudante1", "estudante1", "reservas_bd")
     
    cursor = con.cursor()
    sql = "INSERT INTO Reservas (fk_Salas_id_salas, d_inicio, d_fim, ativo_reserva) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, ( sala, d_inicio, d_fim, ativo))
    con.commit()
    cursor.close()
    conexao_fechar(con)

if __name__ == "__main__":
   main()
 
