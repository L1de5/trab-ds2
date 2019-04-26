import psycopg2
from autor import Autor
from conexaoDao import Conectar
class autorDao:

    
    def listar():
        con = Conectar.entrar()
        try:
            with con.cursor() as cur:
                cur.execute('SELECT * FROM "Autor" ORDER BY cod') 
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
        con = Conectar.entrar()
        try:
            with con.cursor() as cur:
                cur.execute("""SELECT * FROM "Autor" WHERE cod=%s""", [cod] )
                r = cur.fetchone()
                a = Autor(r[1], r[2])
                a.cod = r[0]
                cur.close()
                return a
        except:
            print("Deu Ruim")
    def salvar(a):
        con = Conectar.entrar()
        cur = con.cursor()
        cur.execute("""SELECT COUNT(*) FROM "Autor" WHERE cod=%s""", [a.cod])  
        test = cur.fetchone()
        if(test[0] > 0):
            try:
                with con.cursor() as cur:
                    cur.execute("""UPDATE "Autor" SET nome = %s , email = %s WHERE cod = %s""", [a.nome, a.email, a.cod])
                    con.commit()
                    cur.close()
            except:
                print("Deu Ruim")
        elif(test[0] == 0):
            try:
                with con.cursor() as cur:
                    a.cod = cur.execute("""INSERT INTO "Autor" (nome, email) VALUES (%s, %s) RETURNING cod""", [a.nome, a.email])
                    con.commit()
                    cur.close()
                    con.close()
            except:
                print("Deu Ruim")
    
    def deletar(cod):
        con = Conectar.entrar()
        try:
            with con.cursor() as cur:
                cur.execute("""DELETE FROM "Autor" WHERE cod=%s""", [cod] )
                con.commit()
                cur.execute("""SELECT COUNT(*) FROM "TrabalhoAutor" WHERE cod=%s""", [cod])  
                test = cur.fetchone()
                if(test[0] > 0):
                    try:
                        with con.cursor() as cur:
                            cur.execute("""UPDATE "TrabalhoAutor" SET codAutor='' WHERE codAutor=%s""", [cod])
                            con.commit()
                    except:
                        print("Deu Ruim")
                cur.close()
                con.close()
        except:
            print("Deu Ruim")