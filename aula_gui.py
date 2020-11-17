from time import strftime, strptime
from tkinter import Tk, Label, Button, Entry, END
from tkinter.messagebox import showinfo


def computar():
    global data_input
    data = data_input.get()
    dia_da_semana = strftime('%A',strptime(data, '%d %b %Y'))
    mensagem = f'{data} foi em um(a) {dia_da_semana}'
    showinfo(message=mensagem)
    data_input.delete(0, END)

root = Tk()
root.title(string='Olá Mundo')

# Label
label = Label(root, text='Digite a data: ')
label.grid(row=0, column=0)

# Entry
data_input = Entry(root)
data_input.grid(row=0, column=1)

# Botao
botao_ver = Button(root, text='Ver data',command=computar)
botao_ver.grid(row=1, column=0, columnspan=2)

root.mainloop()
