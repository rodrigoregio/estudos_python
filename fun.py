class Funcionario:
    def __init__(self, name, admis, sal):
        """Inicializa a criação do objeto e atribui os atributos"""
        self.nome = name
        self.data_admissao = admis
        self.salario = sal

    # getters
    def get_nome(self):
        """retorna o nome do funcionario"""
        return self.nome

    def get_data_admissao(self):
        """retorna data de admissão do funcionário"""
        return self.data_admissao

    def get_salario(self):
        """retorna o salário do funcionário"""
        return self.salario

    # setters
    def set_nome(self, name):
        """altera o nome do funcionário"""
        self.nome = name

    def set_data_admissao(self, data_admissao):
        """altera a data de admissão do funcionário"""
        self.data_admissao = data_admissao

    def set_salario(self, sal):
        """altera o salário do funcionário"""
        self.salario = sal


def Gerente(Funcionario):
    def set_salario(self, porcentagem):
        """altera o salario do funcionario de acordo com a porcentagem"""
        self.salario = self.salario * (porcentagem / 100)
        return self.salario
