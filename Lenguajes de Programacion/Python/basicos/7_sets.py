### SETS ###

my_set = set()
my_other_set = {}# Inicialmente se define como un dicionario

my_other_set ={"Ôscar","Garcia", 35, "azul"} #Ahora si que es un set

#print(my_other_set[0]) #--> No se pueden llamar a los datos de un set

my_other_set.add("oscarr_gar") #--> añado otro elemento

print(my_other_set) #--> aqui me doy cuenta de que los sets no son estructuras ordenadas como las listas o las tuplas

my_other_set.add("oscarr_gar") #--> Aqui descubrimos que los sets no admiten repetidos.

print("Garcia" in my_other_set)
print("bebesita" in my_other_set) # Esta es la sintaxix para comprobar que un elemento esta dentro de un set

my_other_set.remove("Ôscar")

my_set = {"oscar", "eric", "mama", "papa"}
my_other_set = {3, 4, 45, 94, 35, 72}   #--> Redefinimos los dos sets iniciales

#Funciones basicas de los sets:
my_set = my_set.union(my_other_set)
print(my_set)                      #--> Aqui he utilizado la funcion "union" para juntar unir dos sets

my_set = my_other_set.difference(my_set)
print(my_set)                         #--> con esta otra funcion "difference" bucamos la direncia entre los dos sets (lo que se podria entender como una resta de sets)

