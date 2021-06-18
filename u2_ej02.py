# Ejercico 2
# Para concatenar texto se utiliza el signo +
# Cree una lista de frutas de 2 elementos, y realice un programa con tkinter que muestre
# un oracion conteniendo los 2 elementos de la lista concatenandolos con texto para formar 
# una oracion con sentido

import tkinter as tk
root = tk.Tk()

frutas = ['limonero','kinotos']
label = tk.Label(root, text='Tengo una planta de '+frutas[1]+' y una planta de '+frutas[0]) 
label.pack(padx=30, pady=30)
root.mainloop()