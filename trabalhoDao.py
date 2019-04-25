import psycopg2
from trabalho import Trabalho
from conexaoDao import Conexao
class trabalhoDao:

    
    def listar():
        con = Conexao.conectar()
        # try:
        #     with con.cursor() as cur:
        cur = con.cursor()
        cur.execute('SELECT * FROM "Trabalho"') 
        r = cur.fetchall()
        lista = []
        for i in range(0, len(r)):
            t = Trabalho(r[i][1], r[i][2], r[i][3], r[i][4])
            t.cod = r[i][0]
            t.dataHoraAtualizacao = r[i][5]
            lista.append(t)
        cur.close()
        return lista
        # except:
        #     print("Deu Ruim")
    def buscar(cod):
        con = Conexao.conectar()
        try:
            with con.cursor() as cur:
                cur.execute("""SELECT * FROM "Trabalho" WHERE cod=%s""", [cod] )
                r = cur.fetchall()
                t = Trabalho(r[0][1], r[0][2], r[0][3], r[0][4])
                t.cod = r[0][0]
                t.dataHoraAtualizacao = r[0][5]
                cur.close()
                return t
        except:
            print("Deu Ruim")
    def editar(t):
        con = Conexao.conectar()
        try:
            with con.cursor() as cur:
                cur.execute("""UPDATE "Trabalho" SET conteudo = %s , nota = %s, "dataEntrega" = %s, titulo = %s, "dataHoraAtualizacao" = %s WHERE cod = %s""", [t.conteudo, t.nota, t.dataEntrega, t.titulo, t.dataHoraAtualizacao, t.cod])
                con.commit()
                cur.close()
        except:
            print("Deu Ruim")
    def inserir(t):
        con = Conexao.conectar()
        
        try:
            with con.cursor() as cur:
                t.cod = cur.execute("""INSERT INTO "Trabalho" (conteudo, nota, "dataEntrega", titulo, "dataHoraAtualizacao") VALUES (%s, %s, %s, %s, %s) RETURNING cod""", [t.conteudo, t.nota, t.dataEntrega, t.titulo, t.dataHoraAtualizacao])
                con.commit()
                cur.close()
                con.close()
        except:
            print("Deu Ruim")
    
    def deletar(cod):
        con = Conexao.conectar()
        try:
            with con.cursor() as cur:
                cur.execute("""DELETE FROM "Trabalho" WHERE cod=%s""", [cod] )
                con.commit()
                cur.close()
                con.close()
        except:
            print("Deu Ruim")