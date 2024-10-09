### STRINGS ###

my_string = "Este es mi esting numero 1"

my_other_string = "este es otro string que he creado"

letras_de_mi_string = len(my_string) + len(my_other_string) #--> Aqui estamos calulando la cantidad de caracteres de una cadena de texto con la funcion "len" nativa de python

suma_de_strings = (my_string + " " + my_other_string) #--> Aqui estamos sumando varias cadenas de texto de manera que se superponen en el orden deseado.

string_con_salto_de_linea = "Este string tiene\nun salto de linea" #--> con el comando "\n" podemos saltar a la siguiente linea de texto.

string_con_tabulacion = "\tEste string tiene tabulacion" #--> Con el comando "\t" podemos añadir una tabulacion al string

print(string_con_salto_de_linea)





















### FORMATEO DE STRINGS ###

mi_nombre, mi_apellido, mi_edad = "oscar", "garcia fernan", 18

string_formateado = "Me llamo %s %s y mi edad es %d" %(mi_nombre, mi_apellido,mi_edad) 
string_formateado_2 = "My name is {} {} and my age is {}".format(mi_nombre,mi_apellido,mi_edad)
string_formateado_3 = f"Mi nombre es {mi_nombre} {mi_apellido} y mi edad es {mi_edad}" #--> LA MEJOR FORMA DE FORMATEAR!!!

"""Lo que hemos hecho aqui
   es asignar a cada "%s" un
   valor como si metieramos 
   la variable dentro del string """

print(string_formateado, string_formateado_2, string_formateado_3)


#Desempaquetando caracteres:
language = "python"
a,b,c,d,e,f = language #--> Dividimos el string en letras para poder jugar con ellas a nuestro antojo

print(a)
print(e)


#Dividir strings
language_dividido = language[2:5]
print(language_dividido)


#Funciones con stirngs

print(language.capitalize()) #--> Pone en majusculas las primera letra

print(language.upper()) #-->Pone todo el string en MAJUSCULAS

print(language.count("t")) #--> Va a contar las veces que sale el caracter que queramos.

print(language.isnumeric())#--> Nos dice si el string es un numero o no

print(language.lower())#--> Nos pone todo el string en minusculas

print(language.lower().isupper()) #--> Podemos concadenar varias funciones de string una al lado de la otra.