from tkinter import *

janela = Tk()

e = Entry(janela, width=50, borderwidth=5 , bg='light gray', fg='dark green')
e.pack()

def apertado():
    if e.get():
        lb = Label(janela, text='voce escreveu ' + e.get())
    else:
        lb = Label(janela, text='voce nao escreveu nada')
    lb.pack()

bt = Button(janela , width=50,
            text='clique', 
            command=apertado)

bt.pack()





janela.mainloop()

