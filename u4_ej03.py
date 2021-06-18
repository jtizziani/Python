"""
Ejercicio 3
escribir un programa que permita tomar un numero por consola y imprima los numeros
entre cero y el numero de menor a mayor separados por comas y luego de mayor a menor 
separados por comas. ejemplo se salida para 5

0,1,2,3,4,5
5,4,3,2,1,0

Ejercicio 4
Escriba un programa que permita tomar una palabra retorne las vocales que contenga
junto con la cantidad de veces que se repite.

Ejercicio 5
Escriba un programa que tome 5 numeros cualesquiera y determine caules son dicisibles por 2

Ejercicio 6
Escriba un programa que pida la fecha segun el formato 04/12/1973 y lo retome segun
el formato 1973/12/04
"""
def fn_nro_maymen(numero):
    arreglo = []
    for nro in range(numero + 1):
        arreglo.append(str(nro))
    arreglo1 = ", ".join(arreglo)
    arreglo2 = " ,".join(arreglo)[::-1]
    print(arreglo1)
    print(arreglo2)    


nro = int(input("Ingrese un nro: "))
fn_nro_maymen(nro)