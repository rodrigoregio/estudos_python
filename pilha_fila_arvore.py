# quociente é o resultado da divisão
# resto é o resto da divisão
# divisor no caso do exercicio é a base (de decimal para binário, base 2)
# dividendo é o que vai ser dividido
class Pilha:
    def __init__(self):
        self.data = []

    def empilha(self, x):
        self.data.append(x)

    def desempilha(self):
        if len(self.data) > 0:
            return self.data.pop(-1)

    def quem_ultimo(self):
        if len(self.data) > 0:
            return self.data[-1]

    def vazia(self):
        return not len(self.data) > 0


def dec2bin(x):
    minhaPilha = Pilha()
    while x > 0:
        minhaPilha.empilha(x % 2)
        x = x // 2
    print('resultado em binario:')
    while not minhaPilha.vazia():
        print('{}'.format(minhaPilha.desempilha()), end='')


class Fila:
    def __init__(self):
        self.data = []

    def insere(self, elemento):
        self.data.append(elemento)

    def remover(self):
        if len(self.data) > 0:
            return self.data.pop(0)

    def quem_proximo(self):
        if len(self.data) > 0:
            return self.data[0]

    def is_vazia(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def toda_fila(self):
        print('Fila:\n')
        for item in self.data:
            print(item, end=', ')
