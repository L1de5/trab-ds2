import datetime
from trabalhoDao import trabalhoDao
from trabalho import Trabalho
from autorDao import autorDao
from autor import Autor

a1 = Autor('João Pedro', 'pedrinho@gueto.com')
a1.cod = 0
autorDao.salvar(a1)

a2 = Autor('Rodrigo Martins', 'lildigs@rap.com')
a2.cod = 0
autorDao.salvar(a2)

a3 = Autor('Luis Henrique Jacinto', 'jacintinho@delas.com')
a3.cod = 0
autorDao.salvar(a3)

t1 = Trabalho('Greve dos Caminhoneiros', 10, datetime.datetime(2018, 5, 10), 'Comer ou Correr?')
t1.cod = 0
trabalhoDao.salvar(t1, 1)

t2 = Trabalho('Conquista e Galanteio', 8, datetime.datetime(2018, 5, 20), 'Como Conquistar elas')
t2.cod = 0
trabalhoDao.salvar(t2, 3)

a1 = Autor('João Pedro Prestes', 'pedrinho2@gueto.com')
a1.cod = 1
autorDao.salvar(a1)

t1 = Trabalho('Greve dos Caminhoneiros2', 8, datetime.datetime(2018, 5, 10), 'Comer ou Correr?2')
t1.cod = 1
trabalhoDao.salvar(t1, 1)

autorDao.deletar(2)
trabalhoDao.deletar(2)

t = trabalhoDao.listar()
for i in range(0, len(t)):
    print(t[i])
print(trabalhoDao.buscar(1))
a = autorDao.listar()
for i in range(0, len(a)):
    print(a[i])
print(autorDao.buscar(3))

