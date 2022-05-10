from tkinter import *

root = Tk()
root.title('Hola Mundo')
root.geometry('200x100')#ancho x alto


l = Label(root, text =' Hola mundo')
def click():
    l.pack()


btn = Button(root, text='Clickeame', command=click,foreground='red')
btn.pack()

root.mainloop()