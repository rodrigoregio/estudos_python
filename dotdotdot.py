import math


class Ponto:
    """Representa um ponto no plano cartesiano com as coordenadas X e Y."""

    def __add__(self, valor1, valor2):
        self.x = self.x + valor1
        self.y = self.y + valor2

    def __add__(self, valor):
        self.x = self.x + valor
        self.y = self.y + valor

    def __repr__(self):
        """Muda a representatividade da classe ao escrever somente ponto no Python Console"""
        return 'Ponto({}, {})'.format(self.x, self.y)

    def __str__(self):
        """Exibe a string abaixo ao dar um print no objeto"""
        return 'Há um ponto na coordenada X - {}, e na Y - {})'.format(self.x, self.y)

    def __init__(self, coord_x=0, coord_y=0):
        """Atribui os valores 0 ás coordenadas x e y ao inicializar o ponto."""
        self.x = coord_x
        self.y = coord_y

    def set_x(self, coord_x):
        """Modifica a coordenada X do ponto."""
        self.x = coord_x

    def set_y(self, coord_y):
        """Modifica a coordenada Y do ponto."""
        self.y = coord_y

    def move(self, coord_x, coord_y):
        """Adiciona os dados (coordX e coordY) ao ponto."""
        self.x += coord_x
        self.y += coord_y

    def get(self):
        """Retorna as coordenadas do ponto no plano cartesiano."""
        return self.x, self.y

    def get_x(self):
        """Retorna a coordenada X."""
        return self.x

    def get_y(self):
        """Retorna a coordenada Y."""
        return self.y

    def distancia(self, ponto):
        """Retorna a distancia entre dois pontos."""
        distancia = math.sqrt(math.pow(self.x - ponto.x, 2) + math.pow(self.y - ponto.y, 2))
        return distancia
