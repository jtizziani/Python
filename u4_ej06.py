"""
Ejercicio 6
Escriba un programa que pida la fecha segun el formato 04/12/1973 y lo retome segun
el formato 1973/12/04

"""
from datetime import date
from datetime import datetime

fecha = str(input("Ingrese una fecha(formato dd/mm/aaaa): "))
fecha1 = datetime.strptime(fecha, "%d/%m/%Y")
fecha3 = datetime.strftime(fecha1, "%Y/%m/%d")
#print(fecha1)
print(fecha3)
