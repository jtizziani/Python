"""
Ejercicio 4
Escriba un programa que permita tomar una palabra retorne las vocales que contenga
junto con la cantidad de veces que se repite.


"""

v = ['a','e','i','o','u']
p = str(input("Ingrese una palabra:"))
mininuscula = p.lower()
#print(mininuscula)
min = list(mininuscula)
#print(min)
for x in v:
    cont = 0 
    for y in min:
      if x == min:
         cont =+ 1          
    print("La vocal",x,"aparece",min.count(x),"veces")    
    


"""
def cont_vocales(p):
      v = ['a','e','i','o','u']
      mininuscula = p.lower()
      min = list(mininuscula)
      for x in v:
          cont = 0
          for y in min:
            if x == min:
               cont =+ 1          
      print("La vocal",x,"aparece",min.count(x),"veces")  


p = str(input("ingrese una palabra"))
cont_vocales(p)
"""
