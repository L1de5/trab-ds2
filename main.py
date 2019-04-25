import datetime
from trabalhoDao import trabalhoDao
from trabalho import Trabalho
from autorDao import autorDao
from autor import Autor


while(True):
    try:
        n = int(input("Você quer interagir com? 0-Autor/1-Trabalho/2-Sair: "))

        if(n < 0 or n > 2):
            raise NameError
    except NameError:
        print("Valor Inválido!!")
        
    
    if(n == 0):

        try:
            n = int(input("O que você precisa? 0-Inserir/1-Remover/2-Editar/3-Buscar/4-Listar/5-Sair: "))

            if(n < 0 or n > 5):
                raise NameError
        except NameError:
            print("Valor Inválido!!")
        if(n == 0):
            nome = str(input("Inserir o Nome:"))
            email = str(input("Inserir a E-mail:"))
            a = Autor(nome, email)            
            r = autorDao.inserir(a)
        if(n == 1):
            cod = int(input("Insira o Código:"))
            a = autorDao.deletar(cod)
        if(n == 2):
            cod = int(input("Inserir Código:"))
            nome = str(input("Inserir o Nome:"))
            email = str(input("Inserir a E-mail:"))
            a = Autor(nome, email)
            a.cod = cod
            r = autorDao.editar(a)
        if(n == 3):
            cod = int(input("Insira o Código:"))
            type(cod)
            a = autorDao.buscar(cod)
            print(a)
        if(n == 4):
            a = autorDao.listar()
            for i in range(0, len(a)):
                print(a[i])
        if(n == 5):
            break
    elif(n == 1):
        
        try:
            n = int(input("O que você precisa? 0-Inserir/1-Remover/2-Editar/3-Buscar/4-Listar/5-Sair: "))

            if(n < 0 or n > 5):
                raise NameError
        except NameError:
            print("Valor Inválido!!")
        
        if(n == 0):
            conteudo = str(input("Qual o Conteúdo?"))
            nota = int(input("Qual a nota?"))
            dia = int(input("Dia de Entrega?"))
            mes = int(input("Mês de Entrega?"))
            ano = int(input("Ano de Entrega?"))
            dataEntrega = datetime.datetime(ano, mes, dia)
            titulo = str(input("Qual o titulo?"))
            t = Trabalho( conteudo, nota, dataEntrega, titulo)            
            r = trabalhoDao.inserir(t)
        if(n == 1):
            cod = int(input("Insira o Código:"))
            t = trabalhoDao.deletar(cod)
        if(n == 2):
            cod = int(input("Inserir Código:"))
            conteudo = str(input("Qual o Conteúdo?"))
            nota = int(input("Qual a nota?"))
            dia = int(input("Dia de Entrega?"))
            mes = int(input("Mês de Entrega?"))
            ano = int(input("Ano de Entrega?"))
            dataEntrega = datetime.datetime(ano, mes, dia)
            titulo = str(input("Qual o titulo?"))
            t = Trabalho( conteudo, nota, dataEntrega, titulo)
            t.cod = cod
            t.dataHoraAtualizacao = datetime.datetime.now()
            r = trabalhoDao.editar(t)
        if(n == 3):
            cod = int(input("Insira o Código:"))
            type(cod)
            t = trabalhoDao.buscar(cod)
            print(t)
        if(n == 4):
            t = trabalhoDao.listar()
            for i in range(0, len(t)):
                print(t[i])
        if(n == 5):
            break
    elif(n == 2):
        break
