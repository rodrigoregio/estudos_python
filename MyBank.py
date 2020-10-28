# Classe para testar a fila do arquivo pilha_fila_arvore.py
# deve-se inserir 8 idosos e 4 normais
# e a cada 2 idosos que saem da fila deve-se remover um da fila normal
from pilha_fila_arvore import *


class Caixa:
    """Classe referente a um caixa"""

    def __init__(self, name='John'):
        """inicializa a classe Caixa"""
        self.nome = name
        self.atendidos = []
        self.atendendo = False

#   def is_atendendo(self, cliente):
#       """para saber se o caixa está atendendo"""
#       if self.atendendo:
#           self.atendidos.append(cliente)

    def quantos_atendidos(self):
        """retorna a quantidade de clientes atendidos pelo caixa"""
        return len(self.atendidos)


class Cliente:
    """Classe referente ao cliente"""

    def __init__(self, name, age):
        """método de inicialização do cliente"""
        self.nome = name
        self.idade = age
        # Aqui abaixo ele mesmo já diz qual tipo de fila pretende ir
        if self.idade > 60:
            self.tipo_fila = 'p'
        else:
            self.tipo_fila = 'n'

    def get_nome(self):
        """retorna o nome do cliente"""
        return self.nome

    def get_idade(self):
        """retorna a idade do cliente"""
        return self.idade

    def get_tipoFila(self):
        """retorna o tipo de fila"""
        return self.tipo_fila

    def __str__(self):
        """transforma o cliente em string"""
        return 'Cliente:\nNome: {}\nIdade: {}\nTipo de fila: {}\n\n'.format(self.nome, self.idade, self.tipo_fila)


class FilaDirecionador:
    """Classe que direciona o cliente á fila e ao caixa"""

    def __init__(self):
        """Inicializa os dois tipos de fila"""
        self.filaP = Fila()
        self.filaN = Fila()
        self.caixaC = Caixa()
        self.atendeP = 0  # este é um contador de clientes

    def vai(self, nomeCli, idadeCli):
        """Com os dados do cliente (nome e idade) instancia um cliente e o direciona á fila"""
        cli = Cliente(nomeCli, idadeCli)
        if cli.tipo_fila == 'n':
            self.filaN.insere(cli)
        else:
            self.filaP.insere(cli)

    def imprime_filaP(self):
        """imprime os clientes na fila preferencial"""
        print(self.filaP.toda_fila())

    def imprime_filaN(self):
        """imprime os clientes na fila normal"""
        print(self.filaN.toda_fila())

    def atender_proximo(self):
        """Atender proxima pessoa da fila"""
        if self.atendeP == 2 or self.filaP.is_vazia():
            # se atendeP (de atendeProximo) for igual a 2 ou a fila preferencial está vazia
            self.atendeP = 0  # zera o contador
            if not self.filaN.is_vazia():  # se a fila não estiver vazia
                self.caixaC.atendidos.append(self.filaN.remover())  # remova o cliente da fila e o adicione na lista de
                # clientes atendidos
        elif self.atendeP < 2:  #se atendeP menor que 2
            self.atendeP = self.atendeP + 1  # acrescente 1 a mesma variavel
            if not self.filaP.is_vazia():  # se a fila
                self.caixaC.atendidos.append(self.filaP.remover())
        if self.filaP.is_vazia() and self.filaN.is_vazia():
            self.caixaC.atendendo = False