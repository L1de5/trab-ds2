import psycopg2
from trabalho import Trabalho
from conexaoDao import Conectar
class trabalhoDao:

    
    def listar():
        con = Conectar.entrar()
        try:
            with con.cursor() as cur:
                cur.execute('SELECT * FROM "Trabalho" ORDER BY cod') 
                r = cur.fetchall()
                lista = []
                for i in range(0, len(r)):
                    t = Trabalho(r[i][1], r[i][2], r[i][3], r[i][4])
                    t.cod = r[i][0]
                    t.dataHoraAtualizacao = r[i][5]
                    lista.append(t)
                cur.close()
                return lista
        except:
            print("Deu Ruim")
    def buscar(cod):
        con = Conectar.entrar()
        try:
            with con.cursor() as cur:
                cur.execute("""SELECT * FROM "Trabalho" WHERE cod=%s""", [cod] )
                r = cur.fetchone()
                t = Trabalho(r[1], r[2], r[3], r[4])
                t.cod = r[0]
                t.dataHoraAtualizacao = r[5]
                cur.close()
                return t
        except:
            print("Deu Ruim")
    def salvar(t, codAutor):
        con = Conectar.entrar()
        cur = con.cursor()
        cur.execute("""SELECT COUNT(*) FROM "Trabalho" WHERE cod=%s""", [t.cod])  
        test = cur.fetchone()
        try:
            cur.execute("""SELECT COUNT(*) FROM "Autor" WHERE cod=%s""", [codAutor])  
            test1 = cur.fetchone()
            if(test1[0] == 0):
                raise NameError
        except:
            print("Autor Não existe") 
        if(test[0] > 0):
            try:
                with con.cursor() as cur:
                    cur.execute("""UPDATE "Trabalho" SET conteudo = %s , nota = %s, "dataEntrega" = %s, titulo = %s, "dataHoraAtualizacao" = %s WHERE cod = %s""", [t.conteudo, t.nota, t.dataEntrega, t.titulo, t.dataHoraAtualizacao, t.cod])
                    cur.execute("""UPDATE "TrabalhoAutor" SET "codAutor" = %s WHERE "codTrabalho" = %s""", (codAutor, t.cod)) 
                    con.commit()
                    cur.close()
            except:
                print("Deu Ruim")
        elif(test[0] == 0):
            try:
                with con.cursor() as cur:
                    cur.execute("""INSERT INTO "Trabalho" (conteudo, nota, "dataEntrega", titulo, "dataHoraAtualizacao") VALUES (%s, %s, %s, %s, %s) RETURNING cod""", [t.conteudo, t.nota, t.dataEntrega, t.titulo, t.dataHoraAtualizacao])
                    con.commit()
                    t.cod = cur.fetchone()
                    cur.execute("""INSERT INTO "TrabalhoAutor" ("codAutor", "codTrabalho") VALUES (%s, %s)""",(codAutor, t.cod[0]))
                    con.commit()
                    cur.close()
                    con.close()
            except:
                print("Deu Ruim")
    
    def deletar(cod):
        con = Conectar.entrar()
        cur = con.cursor()
        try:
            with con.cursor() as cur:
                cur.execute("""DELETE FROM "Trabalho" WHERE cod=%s""", [cod] )
                cur.execute("""DELETE FROM "TrabalhoAutor" WHERE "codTrabalho"=%s""", [cod] )
                con.commit()
                cur.close()
                con.close()
        except:
            print("Deu Ruim")