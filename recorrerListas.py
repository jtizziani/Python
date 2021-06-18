peliculas = ["pelicula1","pelicula2","pelicula3"]
print(peliculas)
print(peliculas[0])
print(len(peliculas))
# con append agregamos datos al final de la lista
peliculas.append("pelicula4")
print(peliculas)
# con pop removemos el ultimo dato de la lista
peliculas.pop()
print(peliculas)
# con extend agregamos un grupo de datos al final de la lista
peliculas.extend(["pelicula4","pelicula5","pelicula6"])
# con remove removemos un dato de la lista
print(peliculas)
peliculas.remove("pelicula3")
print(peliculas)
# con insert insertamos un dato en un lugar especifico de la lista
peliculas.insert(0,"pelicula0")
print(peliculas)
peliculas.insert(3,"pelicula3")
print(peliculas)
