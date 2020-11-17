from tkinter import Tk, Button
from tkinter.messagebox import showinfo
from time import strftime, localtime, gmtime,


def hora_atual():
    hora = strftime('Dia: %d %b %Y\nHora: %H:%M:%S %p\n', localtime())
    showinfo(message=hora)
    print('Hora local:\n', hora)


def hora_atual_greenwitch():
    hora = strftime('Dia: %d %b %Y\nHora: %H:%M:%S %p\n', gmtime())
    showinfo(message=hora)
    print('Hora de Greenwich:\n', hora)


raiz = Tk()
botao_local = Button(raiz,
                     text='Cliqu para ver a hora atual',
                     command=hora_atual)
botao_local.pack()
botao_greenwich = Button(raiz,
                         text='Clique aqui para ver a hora de greenwich',
                         command=hora_atual_greenwitch)
botao_greenwich.pack()
raiz.mainloop()
