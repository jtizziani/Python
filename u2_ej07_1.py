"""
Ejercicio 7 opcional
Intente realizar los ejercicios 1, 2, y 3 con tkinter

# Ejercico 1
# Cree una lista de frutas de 7 elementos, y realice un programa que muestre el tercer 
# elemento de la lista en pantalla 

frutas=['naranjas','bananas','manzanas','peras','frutillas','melon','uvas']
print("El tercer elemento de la lista frutas es: "+frutas[2])
"""

from tkinter import *
frutas=['naranjas','bananas','manzanas','peras','frutillas','melon','uvas']
Label(text="El tercer elemento de la lista frutas es: "+frutas[2]).pack()
mainloop()

