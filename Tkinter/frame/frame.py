from tkinter import *

root = Tk()
root.title('Hola Mundo')

frame = LabelFrame(root, text='', padx=50,pady=50, borderwidth=50)
frame = LabelFrame(root, text= 'frame', padx=10,pady=10, borderwidth=10)
frame.pack(padx=50, pady=50)


l = Label(frame, text='Estoy dentro de un frame')
btn = Button(frame, text='salir', command=root.quit)
l.pack()
btn.pack()

root.mainloop()