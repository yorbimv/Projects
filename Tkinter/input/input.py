from tkinter import *

root = Tk()
root.title('Hola Mundo')


e = Entry(root, width=40)
e.pack()
e.insert(0, "Ingresa texto:     ")           #El 0 indica desde donde inicia el text

def click():
    texto = e.get()
    textvariable.set(texto)
    valor = textvariable.get()
    print(valor)
    # l = Label(root, text=texto)
    # l.pack()
    e.delete(0, END)

btn = Button(root, text='click', command= click)
btn.pack()

textvariable = StringVar()
l = Label(root, textvariable=textvariable)
l.pack()

root.mainloop()
