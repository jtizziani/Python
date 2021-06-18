### Encadenamiento
F={'nombre':{'primero':'Juan','segundo':'Marcelo'},'trabajo':['profesor','ingeniero']}
print(F)
print('nombre')
print(F['nombre']['primero'])
print(F['nombre']['segundo'])
print(F['trabajo'])

print(F['trabajo'][0])

print(F['trabajo'][1])
F['trabajo'].append('pintor')
print(F)
print(F['trabajo'][2])
input()