from calendar import monthrange
from tkinter import Tk, Label, Entry, Button

entrada_ano, entrada_mes=0


def cal(ano, mes):
    dia_da_semana_inicio, total_dias = monthrange(ano, mes)
    dias_semana_abreviado = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']
    conteudo_mes = []
    raiz = Tk()
    for dia in range(7):
        rotulo = Label(raiz, text=dias_semana_abreviado[dia])
        rotulo.grid(row=0, column=dia)
    semana = 1
    for i in range(1, total_dias + 1):
        rotulo = Label(raiz, text=str(i))
        rotulo.grid(row=semana, column=dia_da_semana_inicio)

        dia_da_semana_inicio += 1
        if dia_da_semana_inicio > 6:
            semana += 1
            dia_da_semana_inicio = 0
    raiz.mainloop()

def ver_calendario():
    ano = entrada_ano.get()

def formulario_mes():
    raiz=Tk()
    rotulo_ano = Label(raiz, text='Ano: ')
    rotulo_ano.grid(row=0, column=0)
    entrada_ano = Entry(raiz)
    entrada_ano.grid(0, 1)
    rotulo_mes = Label(raiz, text='Mês: ')
    rotulo_mes.grid(row=1, column=0)
    entrada_mes = Entry(raiz)
    entrada_mes.grid(row=1, column=1)
    botao = Button(raiz,text='Ver calendário',command=ver_calendario)
    botao.grid(row=2, column=0, columnspan=2)
