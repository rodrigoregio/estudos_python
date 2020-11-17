from html.parser import HTMLParser


class MyParser(HTMLParser):
    identacao: int

    def __init__(self):
        HTMLParser.__init__(self)
        self.identacao = 0

    def handle_starttag(self, tag, attrs):
        if tag not in {'br', 'p', 'link', 'meta', 'img', 'b'}:
            print('{}{} iniciou'.format(self.identacao * ' ', tag))
            self.identacao = self.identacao - 2

    def handle_endtag(self, tag):
        if tag not in {'br', 'p', 'link', 'meta', 'img', 'b'}:
            print('{}{} terminou'.format(self.identacao * ' ', tag))
            self.identacao = self.identacao - 2


infile = open('D:\GitHub\mysiteandblog\_site\index.html')
content = infile.read()
infile.close()
# from aula_web_parser import *
teste = MyParser()
teste.feed(content)
