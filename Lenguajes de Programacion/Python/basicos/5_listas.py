### LISTAS ###

my_list = list()

my_other_list = []

my_list = [13, 34, 45, 25, 25, 64, 23, 14, 73] #--> una lista es una cantidad de datos

my_other_list = [27, 8.99, "Oscar", "Garcia"]# --> las listas pueden guardar varios tipos de datos

print(my_other_list[2]) #-->podemos llamar a cualquier valor de la lista segun su indice

print(my_list.count(25)) #--> Nos muestra cuantas veces aparece el dato en una lista

edad, altura, nombre, apellido = my_other_list #--> Estamos agenciando los valores de la lista a diferentes variables
print(altura)

edad, altura, nombre, apellido = my_other_list[0], my_other_list[1], my_other_list[2], my_other_list[3]
print(edad) #Es lo mismo de antes pero reasignado a mano

print(my_list + my_other_list) #--> Se pueden concadenar listas

#Funciones para listas

my_other_list.append("Ins gabriela mistral") #Con "append" añadimos un dato mas al final de la lista
print(my_other_list)

my_other_list.insert(2,"geminis") # Mientras que con "insert" lo añadimos en el indice que escojamos
print(my_other_list)

my_other_list[2] = "capricornio" #podemos cambiar el valor de cualquier dato de la lista
print(my_other_list)

my_other_list.remove("Oscar") #--> Aqui estamos quitando el dato que nosotros queramos
print(my_other_list)

my_other_list.pop() #Aqui estamos quitando el ultimo por defecto pero no desaparece solo de desapila
print(my_other_list)

del my_other_list[2]#--> Aqui estoy eliminando un indice de la lista de forma permanente

my_copy_list = my_other_list.copy()

my_other_list.clear()#--> Con la funcion "clear" Vaciamos completamente la lista

my_copy_list.reverse()
print(my_copy_list)