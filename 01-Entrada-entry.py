from tkinter import *

janela = Tk()

e = Entry(janela, width=50, bg='light gray', fg='dark green')
e.pack()

def apertado():
    lb = Label(janela, text='bt clicado')
    lb.pack()

bt = Button(janela, 
            text='clique', 
            command=apertado)

bt.pack()





janela.mainloop()

