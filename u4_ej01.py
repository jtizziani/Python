"""
Ejercicio 1
Escribir un programa que tome el valor del nombre del usuario por consola y luego
lo imprima por pantalla



"""
from tkinter import *
print(f"Ingrese su nombre:")
p = input()

Label(text=f"Hola: {p}").pack()
mainloop()