from tkinter import *
from PIL import ImageTk, Image


janela = Tk()
janela.title('imagens')

janela.iconbitmap('03-imagens/pequeno.ico')

minha_img = ImageTk.PhotoImage(Image.open("homem.png"))

minha_lb = Label(image=minha_img)
minha_lb.pack()

bt_sair = Button(janela, text='sair', command=janela.quit)
bt_sair.pack()

janela.mainloop()