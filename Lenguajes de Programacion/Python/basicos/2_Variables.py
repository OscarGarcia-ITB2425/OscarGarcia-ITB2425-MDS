### VARIABLES ###

#Podemos crear variables de texto:

my_variable = "variable de texto"

#Tambien podemos crear variables con numeros:

edad = 34

#I obiamente tambien podemos crear variables con numeros boleanos:

argumento = False

#De esta manera podemos encadenar varias variables en un mismo "print" separados por comas:

print(my_variable,edad,argumento)

#Tambien podemos concadenar variables preguardadas con texto normal:

print("Texto normal recien escrito+", my_variable)

#Tambien puedes crear varias variables en una sola linea de codigo:

nombre, apellido, cumpleaños = "oscar", "garcia fernan", "el 1 de febrero"

#Variable la cual rellenamos nosotros mismos una vez ejecutado el script o programa --> comando "input"

nombre = input("Intoduce tu nombre:")

# ¿Podemos forzar el tipo de dato de una variable?: --> NO

nombre: str = "mohamed"
print (type(nombre))


#FUNCIONES DEL SISTEMA:oscar

#funcion "len" --> esta funcion cuenta el nuemero de caracteres, contados los espacios.
print(len("hola mundo"))