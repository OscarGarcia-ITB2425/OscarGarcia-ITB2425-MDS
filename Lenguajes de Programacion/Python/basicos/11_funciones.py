
###FUNCIONES###


primer_numero = int(input("primer numero:"))

segundo_numero = int(input("segundo numero:"))

def suma_de_dos_numeros (primer_numero, segundo_numero):  #--> esto seria el ejempo de una funcion de sencilla para sumar dos valores. 
    print(primer_numero + segundo_numero)


suma_de_dos_numeros(primer_numero, segundo_numero)


def suma_con_return (primer_numero, segundo_numero):
    return primer_numero + segundo_numero           #--> con la funcion "return" ahora podemos guardar el valor en una variable
mi_resultado = suma_con_return(12,23)
print(mi_resultado)


def print_nombre (nombre, apellido):
    print(f"{nombre} {apellido}") #-->aqui utilizo el formateo de strings de la clase 4

print_nombre(apellido = "Garcia", nombre = "Oscar") #--> yo puedo cambiar el orden en el que le doy las variables si las defino cada una.

def nombre_apellido(nombre, apellido, alias= "sin alias"):
    print(f"{nombre} {apellido} {alias}")                  #--> le puedo indicar que una variable en caso de estar vacia darle un valor por defecto































