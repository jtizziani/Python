### Pasar a lista
F={'nombre':{'primero':'Juan','segundo':'Marcelo'},'trabajo':['profesor','ingeniero']}

### Campos claves 'nombre' y 'trabajo'
P=list(F.keys())

### Campos valores [{'primero':'Juan','segundo':'Marcelo'},['profesor','ingeniero']]

print(P)

S=list(F.values())
print(S)
#input()

### Herramientas de sistema

import sys, os
print(len(dir(sys)))
print(len(dir(os)))

print(dir(sys))
print(dir(os))

# Imprime plataforma 
print(sys.platform)

# El mayor entero dimensionado de forma nativa en la maquina
print(sys.maxsize)

# Version del sistema
print(sys.version)

# Diccionarios donde busca los modulos en el orden en el cual busca 
print(sys.path)

## OS esta compuesto por variables y funciones que mapean el sistema operativo en 
#  el que corre Python
print(os.getpid())
print(os.getcwd())