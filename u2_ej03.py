"""
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

diccionario = {'identificador':{'nombre':'Jorge','apellido':'Tizziani'}, 'telefono':'011001'}
print(diccionario.keys())
print(diccionario.values())
valores = diccionario.values()
claves = diccionario.keys()
#print(f"{claves}:{valores}")
print(f"las claves son {claves} y los valores {valores}")


"""
PREGUNTA:
Cree que para guardar y recuperar informacion es mejor un dicionario o una lista?
Justifique la respuesta:
Segun lo leido y entenddido los diccionarios son mejores para guardar y recuperar informacion
ya que presentangran flexibilidad y donde los elementos se almacenan por claves en lugar de 
por su posicion; los diccionarios toman el lugar de los registros 

"""
