class Autor:

    def __init__(self, nome, email):
        self._nome = nome
        self._email = email

    @property
    def cod(self):
        return self._cod

    @cod.setter
    def cod(self, cod):
        self._cod = cod

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, conteudo):
        self._nome = nome

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    def __str__(self):
        return 'Código: ' + str(self._cod) + '\n Nome: ' + self._nome + '\n E-mail: ' + self._email