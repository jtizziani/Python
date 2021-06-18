"""
Ejercicio 7 opcional
Intente realizar los ejercicios 1, 2, y 3 con tkinter

Cree un diccionario con las claves:
    - Identificador
    - nombre
    - apellido
    - telefono
Nota: al ulilizar claves no utilice acentos u otros caracteres en espaniol.
Realice un programa que a partir del diccionario creado retorne en una oracion:
    1) El numero de elementos del diccionario
    2) Las claves del diccionario

"""

import tkinter as tk
root = tk.Tk()


diccionario = {'nombre':'Jorge','apellido':'Tizziani','dni':'21407958','telefono':'011001'}
valores = diccionario.values()
claves = diccionario.keys()

label = tk.Label(root, text = f'las claves son {claves} \n y los valores {valores}') 
label.pack(padx=40, pady=40)
root.mainloop()
