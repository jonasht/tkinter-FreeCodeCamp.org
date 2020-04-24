from tkinter import *
from PIL import ImageTk, Image


janela = Tk()
janela.title('imagens')

janela.iconbitmap('04-imagens3/pequeno.ico')


minha_img0 = ImageTk.PhotoImage(Image.open("04-imagens3/i0.png"))
minha_img1 = ImageTk.PhotoImage(Image.open("04-imagens3/i1.png"))
minha_img2 = ImageTk.PhotoImage(Image.open("04-imagens3/i2.png"))
minha_img3 = ImageTk.PhotoImage(Image.open("04-imagens3/i3.png"))
minha_img4 = ImageTk.PhotoImage(Image.open("04-imagens3/i4.png"))
minha_img5 = ImageTk.PhotoImage(Image.open("04-imagens3/i5.png"))

minha_img6 = ImageTk.PhotoImage(Image.open("04-imagens3/i6.png"))
minha_img7 = ImageTk.PhotoImage(Image.open("04-imagens3/i7.png"))
minha_img8 = ImageTk.PhotoImage(Image.open("04-imagens3/i8.png"))
minha_img9 = ImageTk.PhotoImage(Image.open("04-imagens3/i9.png"))
minha_img10 = ImageTk.PhotoImage(Image.open("04-imagens3/i10.png"))

imagem_lista = [minha_img0, minha_img1, minha_img2, minha_img3, minha_img4, minha_img5,
                minha_img6, minha_img7, minha_img8, minha_img9, minha_img10]

status = Label(janela, text='imagem 0 de' + str(len(imagem_lista)), bd=1, relief=SUNKEN,
               anchor=E,)

minha_lb = Label(image=minha_img0)
minha_lb.grid(row=0, column=0, columnspan=3)
imagem_numero = 0
def Frente(imagem_numero):
    global minha_lb
    global bt_frente
    global bt_tras
    
    minha_lb.grid_forget()
    minha_lb = Label(image=imagem_lista[imagem_numero-1])
    bt_frente = Button(janela, text='>>>', command=lambda: Frente(imagem_numero+1), fg='blue')
    bt_tras = Button(janela, text='<<<', command=lambda: Tras(imagem_numero-1), fg='blue')
    
    if imagem_numero == len(imagem_lista):
        bt_frente = Button(janela, text='>>>', state=DISABLED, fg='blue')
        
    minha_lb.grid(row=0, column=0, columnspan=3)
    bt_tras.grid(row=1, column=0)
    bt_frente.grid(row=1, column=2)
    
        # atualização do status BAR
    status = Label(janela, text='imagem ' + str(imagem_numero) + ' de' + str(len(imagem_lista)), bd=1, relief=SUNKEN,
               anchor=E,)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    
def Tras(imagem_numero):
    global minha_lb
    global bt_frente
    global bt_tras
    
    minha_lb.grid_forget()
    minha_lb = Label(image=imagem_lista[imagem_numero-1])
    bt_frente = Button(janela, text='>>>', command=lambda: Frente(imagem_numero+1))
    bt_tras = Button(janela, text='<<<', command=lambda: Tras(imagem_numero-1))
    
    if imagem_numero == 1:
        bt_tras = Button(janela, text='<<<', state=DISABLED)
    minha_lb.grid(row=0, column=0, columnspan=3)
    bt_tras.grid(row=1, column=0)
    bt_frente.grid(row=1, column=2)
    
    # atualização do status BAR
    status = Label(janela, text='imagem ' + str(imagem_numero) + ' de' + str(len(imagem_lista)), bd=1, relief=SUNKEN,
               anchor=E,)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

bt_tras = Button(janela, text='<<<', command=Tras, state=DISABLED, fg='blue')
bt_sair = Button(janela, text='<SAIR>', command=janela.quit, fg='blue')
bt_frente = Button(janela, text='>>>', command=lambda: Frente(0), fg='blue')

bt_tras.grid(row=1, column=0)
bt_sair.grid(row=1, column=1)
bt_frente.grid(row=1, column=2, pady=10 )

status.grid(row=2, column=0, columnspan=3, sticky=W+E)

janela.mainloop()