from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Hola Mundo: ')

tree = ttk.Treeview(root)
tree['columns'] = ['Nombre', 'Telefono', 'Empresa']

#Indices
# tree.column('#0')                   
tree.column('#0', width=0, stretch=NO)                   
tree.column('Nombre')
tree.column('Telefono')
tree.column('Empresa')

#Heading, la parte de arriba
# tree.heading('#0', text = 'id')
tree.heading('#0')
tree.heading('Nombre', text = 'Nombre')
tree.heading('Telefono', text = 'Telefono')
tree.heading('Empresa', text = 'Empresa')

tree.grid(column=0, row=0)

tree.insert('',END, 'lala', values = ('Uno', 'Dos', 'tres'), text ='Chanchito feliz')
tree.insert('',END, 'lele', values = ('cuatro', 'cinco', 'seis'), text ='Chanchito triste')
tree.insert('',END, 'lili', values = ('4', '5', '6'), text ='hijo Chanchito')





root.mainloop()