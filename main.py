from autorDao import autorDao
from autor import Autor

while(True):
    try:
        n = int(input("Você quer interagir com? 0-Autor/1-Trabalho/2-Sair: "))

        if(n < 0 or n > 2):
            raise NameError
    except NameError:
        print("Valor Inválido!!")
        
    if(n == 2):
        break
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
            nome = str(input("Inserir o Nome:"))
            email = str(input("Inserir a E-mail:"))
            a = Autor(nome, email)
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
