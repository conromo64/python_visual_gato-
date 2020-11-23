from tkinter import *

root = Tk()

cell = Entry(root, width=20)
cell.grid(padx=5, pady=5, row=0, column=0)
cell.insert(0, 'Identificador')

cell = Entry(root, width=20)
cell.grid(padx=5, pady=5, row=0, column=1)
cell.insert(0, 'Nombre')

cell = Entry(root, width=20)
cell.grid(padx=5, pady=5, row=0, column=2)
cell.insert(0, 'Puntos')

for r in range(1, 3):
    for c in range(0, 3):
        cell = Entry(root, width=20)
        cell.grid(padx=5, pady=5, row=r, column=c)
        cell.insert(0, '[{}, {}]'.format(r, c))

root.mainloop()