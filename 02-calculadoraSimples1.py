from tkinter import *

janela = Tk()
janela.title('calculadora simples')
janela['bg']='gray'

entrd = Entry(janela, width=35, borderwidth=5, font='Times 10 bold', fg='green', bg='light gray')
entrd.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky=W+E)



#entrd.insert(0, 'seu nome')
def Botao_clicado(numero):
    #entrd.delete(0, END)
    atual = entrd.get()

    entrd.delete(0, END)

    entrd.insert(0, str(atual) + str(numero))

def Botao_limpar():
    entrd.delete(0, END)
    
def Botao_mais():
    primeiro_numero = entrd.get()
    global p_num
    global matematica
    matematica = 'mais'
    p_num = int(primeiro_numero)
    entrd.delete(0, END)
    
def Botao_igual():
    segundo_numero = entrd.get()
    entrd.delete(0, END)
    
    if matematica == 'mais':
        entrd.insert(0, p_num + int(segundo_numero))
        
    if matematica == 'menos':
        entrd.insert(0, p_num - int(segundo_numero))
        
    if matematica == 'vezes':
        entrd.insert(0, p_num * int(segundo_numero))
        
    if matematica == 'divisao':
        entrd.insert(0, p_num / int(segundo_numero))
        
        
def Botao_menos():
    primeiro_numero = entrd.get()
    global p_num
    global matematica
    matematica = 'menos'
    p_num = int(primeiro_numero)
    entrd.delete(0, END)

def Botao_vezes():
    primeiro_numero = entrd.get()
    global p_num
    global matematica
    matematica = 'vezes'
    p_num = int(primeiro_numero)
    entrd.delete(0, END)
    
def Botao_dividir():
    primeiro_numero = entrd.get()
    global p_num
    global matematica
    matematica = 'divisao'
    p_num = int(primeiro_numero)
    entrd.delete(0, END)

bt1 = Button(janela, text='1', padx=40, pady=20, command=lambda: Botao_clicado(1), bg='light gray', fg='dark green',
font='Times 10 bold')
bt2 = Button(janela, text='2', padx=40, pady=20, command=lambda: Botao_clicado(2), bg='light gray', fg='dark green',
font='Times 10 bold')
bt3 = Button(janela, text='3', padx=40, pady=20, command=lambda: Botao_clicado(3), bg='light gray', fg='dark green',
font='Times 10 bold')
bt4 = Button(janela, text='4', padx=40, pady=20, command=lambda: Botao_clicado(4), bg='light gray', fg='dark green',
font='Times 10 bold')
bt5 = Button(janela, text='5', padx=40, pady=20, command=lambda: Botao_clicado(5), bg='light gray', fg='dark green',
font='Times 10 bold')
bt6 = Button(janela, text='6', padx=40, pady=20, command=lambda: Botao_clicado(6), bg='light gray', fg='dark green',
font='Times 10 bold')
bt7 = Button(janela, text='7', padx=40, pady=20, command=lambda: Botao_clicado(7), bg='light gray', fg='dark green',
font='Times 10 bold')
bt8 = Button(janela, text='8', padx=40, pady=20, command=lambda: Botao_clicado(8), bg='light gray', fg='dark green',
font='Times 10 bold')
bt9 = Button(janela, text='9', padx=40, pady=20, command=lambda: Botao_clicado(9), bg='light gray', fg='dark green',
font='Times 10 bold')
bt0 = Button(janela, text='0', padx=40, pady=20, command=lambda: Botao_clicado(0), bg='light gray', fg='dark green',
font='Times 10 bold')

bt_mais = Button(janela, text='+', pady=20, command=Botao_mais)
bt_igual = Button(janela, text='=', pady=20, command=Botao_igual)
bt_menos = Button(janela, text='-', padx=40, pady=20, command=Botao_menos)
bt_vezes = Button(janela, text='X', padx=39, pady=20, command=Botao_vezes)
bt_dividir = Button(janela, text='/', padx=40, pady=20, command=Botao_dividir)

bt_limpar = Button(janela, text='limpar', pady=20, command= Botao_limpar)


# colocando botoes em grid

bt1.grid(row=3, column=0)
bt2.grid(row=3, column=1)
bt3.grid(row=3, column=2)

bt4.grid(row=2, column=0)
bt5.grid(row=2, column=1)
bt6.grid(row=2, column=2)

bt7.grid(row=1, column=0)
bt8.grid(row=1, column=1)
bt9.grid(row=1, column=2)

bt0.grid(row=4, column=0)

bt_limpar.grid(row=4, column=1, columnspan=2, sticky=W+E)
bt_mais.grid(row=3, column=4, sticky=W+E)
bt_igual.grid(row=5, column=0, columnspan=5, sticky=W+E)

bt_menos.grid(row=2, column=4)
bt_vezes.grid(row=1, column=4)
bt_dividir.grid(row=4, column=4)

janela.mainloop()