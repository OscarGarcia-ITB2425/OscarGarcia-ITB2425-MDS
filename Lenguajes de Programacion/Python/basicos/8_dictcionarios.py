###DICIONARIOS###

my_dict = dict() #--> Forma clasica de formar un dictcionario

my_other_dict = {
    "Nombre":"Oscar", 
    "Apellido":"Garcia",           #--> Los datos de los dicionarios siempre van en parejas con la "llave o clave"  i el valor que le asignemos a cada llave o valor
    "edad":18,                                  
    "habilidades":["python", "basket", "Gym"] #--> Aqui he añadido un valor en formato de lista.     
    }


print(len(my_other_dict)) #--> el numero que nos va a devolver es el de la cantidad de Llaves o claves del dictcionario

print(my_other_dict["Nombre"]) #--> Podemos llamar a una de las claves del dicionario devolviendonos su valor 

my_other_dict["edad"] = 23 #--> Ahora he cambiado el valor relacionado con la clave "edad"

my_other_dict["ciudad"] = "Sant Vicents Dels Horts" #--> I aqui hemos añadido directamente otra clave con su valor

print(my_other_dict) #--> Aqui tambien nos daremos cuenta de los dictcionarios son estructuras ordenadas.

del my_other_dict["ciudad"] #--> con la funcion "del" puedo eliminar cualquier clave del dictcionario que yo aceda
print(my_other_dict)


print("Apellido" in my_other_dict) #--> Para comprovar si un valor esta o no en un dictcionario lo busco por su clave

#Funciones basicas con los dict:

print(my_other_dict.values())#--> me devuelve solo los valores
print(my_other_dict.items())#--> me devuelve todos los items en forma de lista
print(my_other_dict.keys())#--> me devuelve solo las claves

my_new_dict = dict.fromkeys(my_other_dict) #-->Con el comando "fromkeys" he creado un nuevo dictcionario con todas las claves de otro dicionario pero vacias
print(my_new_dict)

my_new_dict = dict.fromkeys(my_other_dict, 28) #--> Ahora ademas le he añadido un segundo parametro para rellenar las claves con un valor "28 en este caso"
print(my_new_dict)