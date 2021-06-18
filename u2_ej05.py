"""
Ejercicio 5
 Para pasar un valor de string a entero se utiliza el comando int(), 
 asi
 int("2")
 Tome dos valores por consola, y guarde en una lista:
 [primer_valor, segundo_valor, la_suma_de_los_valores]
 Muestre en pantalla la lista.

"""

lista = ['valor1','valor2',"valor3"]
print("Ingrese un valor1:")
lista[0]=input()
print("Ingrese un valor2:")
lista[1]=input()
lista[2]=int(lista[0])+int(lista[1])
print(lista)

