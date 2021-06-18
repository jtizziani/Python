"""
Ejercicio 2
Escribir un programa que permita ingresar un numero y calcule el factorial




"""
from tkinter import *
nro = int(input("Ingrese Nro a calcular Factorial:"))
factorial = 1
if (nro == 0):
    factorial = 1
else: 
    for i in range(1, nro+1):
        factorial = factorial*i

Label(text=f"El factorial de {nro} es {factorial}").pack()
mainloop()