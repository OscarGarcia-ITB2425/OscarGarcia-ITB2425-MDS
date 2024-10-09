### TUPLAS ###

my_tuple = tuple()
my_other_tuples = () 
#"""La gran diferencia entre las tuplas i las listas es que los valores de las tuplas son
# constantes, no puedes añadir ni quitar elementos."""

my_tuple = (34, 35, 75, 29, 64, 97, 72, 14)
my_other_tuples = ("Gucci", "Ralph Lauren", "Porche", "NIKE", "BOSS")
my_sum_tuple = my_tuple + my_other_tuples
print(my_sum_tuple) #Pero si que se pueden formar nuevas tuplas por medio de la suma de otras dos tuplas.

del my_tuple #--> Con la funcion "del" Borro completamente la tupla del sistema de forma completa.

#"""En caso de tener que cambiar un dato de la tupla cambia el tipo de estructura
# a una lista en la qual si podremos trabajar. (todo que no es lo aconsejable)"""