from tkinter import *

janela = Tk()
def apertado():
    lb = Label(janela, text='bt clicado')
    lb.pack()

bt = Button(janela, text='clique', padx=50, pady=50, bg='black', fg='pink', command=apertado)

bt.pack()





janela.mainloop()

