import psycopg2
from abc import ABCMeta, abstractmethod

class Conexao:
    
    __metaclass__ = ABCMeta

    @abstractmethod
    def Conectar():
        pass

class Conectar:

    def entrar():
        return psycopg2.connect('host=localhost port=1234 dbname=pythonic user=postgres password=postgres')

    
