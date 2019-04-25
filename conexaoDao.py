import psycopg2

class Conexao:
    
    def conectar():
        return psycopg2.connect('host=localhost port=1234 dbname=pythonic user=postgres password=postgres')