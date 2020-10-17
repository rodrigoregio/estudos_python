class Funcionario:
    def __init__(self, name='', admission='01/01/2000', salary=1):
        """Método construtor que inicializa os valores"""
        self.nome = name
        self.admissao = admission
        self.salario = salary

    def get_nome(self):
        """Retorna o nome do funcionario"""
        return self.nome

    def set_nome(self, name):
        """Altera o nome do funcionario"""
        self.nome = name

    def get_admissao(self):
        """Retorna a data de admissão do funcionario"""
        return self.admissao

    def set_admissao(self, admission):
        """Altera a data de admissão do funcionario"""
        self.admissao = admission

    def get_salario(self):
        """Retorna o salario do funcionario"""
        return self.salario

    def set_salario(self, salary):
        """Altera o salario do funcionario"""
        self.salario = salary

    def get(self):
        """Retorna o funcionario como string"""
        return 'Funcionario({}, {}, {})'.format(self.get_nome(), self.get_admissao(), self.get_salario())

    def __repr__(self):
        """Retorna a representatividade do funcionario (retorna o funcionario.get())"""
        return self.get()

    def __str__(self):
        """Retorna o funcionario como string (retorna o funcionario.get())"""


class Gerente(Funcionario):
    def __init__(self, name='', admission='01/01/2000', salary=100):
        """Método construtor de um gerente"""
        self.nome = name
        self.admissao = admission
        self.salario = salary

    def set_salario(self, porcentagem):
        """altera o salario de acordo com a porcentagem do bonus"""
        self.salario = self.salario + (self.salario * (porcentagem / 100))

    def get(self):
        """Retorna o gerente em formato string"""
        return 'Gerente({}, {}, {})'.format(self.get_nome(), self.get_admissao(), self.get_salario())

    def __repr__(self):
        """Retorna a representatividade da classe, que alias é o get_gerente()"""
        return self.get()

    def __str__(self):
        """Retorna o gerente como string"""
        return self.get()


class Teste:
    def __init__(self, string_de_teste='Isto é um teste'):
        self.mensagem = string_de_teste

    def __repr__(self):
        return 'Classe de teste({})'.format(self.mensagem)
