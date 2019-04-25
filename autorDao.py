import psycopg2
from autor import Autor
from conexaoDao import Conexao
class autorDao:

    
    def listar():
        con = Conexao.conectar()
        try:
            with con.cursor() as cur:
                cur.execute('SELECT * FROM "Autor"') 
                r = cur.fetchall()
                lista= []
                for i in range(0, len(r)):
                    a = Autor(r[i][1], r[i][2])
                    a.cod = r[i][0]
                    lista.append(a)
                cur.close()
                return lista
        except:
            print("Deu Ruim")
    def buscar(cod):
        con = Conexao.conectar()
        try:
            with con.cursor() as cur:
                cur.execute("""SELECT * FROM "Autor" WHERE cod=%s""", [cod] )
                r = cur.fetchall()
                a = Autor(r[0][1], r[0][2])
                a.cod = r[0][0]
                cur.close()
                return a
        except:
            print("Deu Ruim")
    def editar(a):
        con = Conexao.conectar()
        try:
            with con.cursor() as cur:
                cur.execute("""UPDATE "Autor" SET nome = %s , email = %s WHERE cod = %s""", [a.nome, a.email, a.cod])
                con.commit()
                cur.close()
        except:
            print("Deu Ruim")
    def inserir(a):
        con = Conexao.conectar()
        try:
            with con.cursor() as cur:
                a.cod = cur.execute("""INSERT INTO "Autor" (nome, email) VALUES (%s, %s) RETURNING cod""", [a.nome, a.email])
                con.commit()
                cur.close()
                con.close()
        except:
            print("Deu Ruim")
    
    def deletar(cod):
        con = Conexao.conectar()
        try:
            with con.cursor() as cur:
                cur.execute("""DELETE FROM "Autor" WHERE cod=%s""", [cod] )
                con.commit()
                cur.close()
                con.close()
        except:
            print("Deu Ruim")