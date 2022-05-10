from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Hola Mundo')

def click():
    messagebox.showinfo('Popup', 'Hola Mundo')                  #showwarning, showinfo, showerror


# def click():
#     respuesta = messagebox.askquestion('Popup', 'Hola Mundo')
#     if respuesta == 'yes':
#         messagebox.showinfo('Respuesta', 'la respuesta fue ' + respuesta)
#     else:
#         messagebox.showinfo('Respuesta', 'la respuesta fue ' + respuesta)
        


# def click():
#     respuesta = messagebox.askokcancel('Hola Mundo', 'Desea realizar algo?')
#     if respuesta :
#         messagebox.showinfo('Hola Mundo', 'La respuesta fue OK')
#     else:
#         messagebox.showinfo('Hola Mundo', 'La respuesta fue cancel')


# def click():
#     respuesta = messagebox.askyesno('Hola Mundo', 'Desea realizar algo?')
#     if respuesta :
#         messagebox.showinfo('Hola Mundo', 'La respuesta fue YES')
#     else:
#         messagebox.showinfo('Hola Mundo', 'La respuesta fue NO')


btn = Button(root, text = 'Presioname', command=click)
btn.pack()

#Salir
exit = Button(root, text= 'Salir', command = root.quit)
exit.pack()

root.mainloop()