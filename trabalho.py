from datime import datetime


class Trabalho:

    def __init__(self, conteudo, dataEntrega, nota, titulo):
        self._cod = None
        self._conteudo = conteudo
        self._dataEntrega = dataEntrega
        self._nota = nota
        self._titulo = titulo
        self._dataHoraAtualizacao = datetime.datetime.now()
    @property
    def cod(self):
        return self._cod

    @property
    def conteudo(self):
        return self._conteudo

    @conteudo.setter
    def conteudo(self, conteudo):
        self._conteudo = conteudo

    @property
    def dataEntrega(self):
        return self._dataEntrega

    @dataEntrega.setter
    def dataEntrega(self, dataEntrega):
        self._dataEntrega = dataEntrega

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nota):
        self._nota = nota

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo
    
    @property
    def dataHoraAtualizacao(self):
        return self._dataHoraAtualizacao

    @dataHoraAtualizacao.setter
    def dataHoraAtualizacao(self):
        self._dataHoraAtualizacao =  datetime.datetime.now()
    
    def __str__(self):
        return 'Código: ' + str(self._cod) + '\n conteudo: ' + self._conteudo + '\n Data de Entrega: ' + self._dataEntrega.strftime('%d/%m/%Y') + '\n nota: ' + self._nota + '\n Titulo:' + self_titulo + '\n Data e Hora de Atualização: ' + self._dataEntrega