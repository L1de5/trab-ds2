import psycopg2
from autor import Autor
class autorDao:

    
    def listar():
        con = psycopg2.connect('host=localhost port=1234 dbname=pythonic user=postgres password=postgres')
        cur = con.cursor()
        
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
        con = psycopg2.connect('host=localhost port=1234 dbname=pythonic user=postgres password=postgres')
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
    # def editar(cod, a):
    #     con = psycopg2.connect('host=localhost port=1234 dbname=pythonic user=postgres password=postgres')
    #     try:
    #         with con.cursor() as cur:
    #             cur.execute("""UPDATE "Autor" SET nome = 'ja2o' , email = 'odi2o.com' WHERE cod = %s""", (cod, ))
    #             cur.close()
    #     except:
    #         print("Deu Ruim")
    def inserir(a):
        con = psycopg2.connect('host=localhost port=1234 dbname=pythonic user=postgres password=postgres')
        try:
            with con.cursor() as cur:
                print(cur.execute("""INSERT INTO "Autor" (nome, email) VALUES ('jasdaus', 'asdasd') RETURNING cod"""))
                cur.close()
        except:
            print("Deu Ruim")
    
    def deletar(cod):
        con = psycopg2.connect('host=localhost port=1234 dbname=pythonic user=postgres password=postgres')
        try:
            type(cod)
            cur = con.cursor()
            cur.execute("""DELETE FROM "Autor" WHERE cod = %s""", [cod])
            cur.close()
        except:
            print("Deu Ruim")