"""
Ejercicio 5
Escriba un programa que tome 5 numeros cualesquiera y determine caules son divisibles por 2
      ingreso 5 nros y los guardo en un arreglo
      recorro el arreglo o me fijo cual es divisible por 2(resto 0)
      si es divisible por 2 lo guardo en otro arreglo2
      imprimo arreglo2


"""

nro1 = int(input("Ingrese nro1: "))
nro2 = int(input("Ingrese nro2: "))
nro3 = int(input("Ingrese nro3: "))
nro4 = int(input("Ingrese nro4: "))
nro5 = int(input("Ingrese nro5: "))

lista = [nro1, nro2, nro3, nro4, nro5]
print(lista)
for i in lista:
    if i%2 == 0:
        print("El numero",i,"es divisible por 2")
    else:
        print("El numero",i,"no es divisible por 2")
