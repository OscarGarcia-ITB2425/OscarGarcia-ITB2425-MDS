###BUCLES LOOPS CICLOS###


#LOOPS CON EL WHILE:

loop_condicion = 0

while loop_condicion < 100:  #--> El "while" funciona de forma parecida al "if" de manera que: si es true entonces el bucle continua.
    print(loop_condicion)
    loop_condicion += 3
else:
    print("Tu condicion es igual o mas grande que 100") #--> en python a los "while" se le pueden adjuntar un  "else"

print("El codigo continua")
 
loop_condicion = 15
while loop_condicion <20 and loop_condicion > 10: #--> Puedes utilizar los operadores logicos para complicar mas los bucles
    print("tu condicion esta entre 10 i 20")

    break #--> Con el comando "break" terminas el bucle.

#BUCLES FOR:

my_list = ["oscar", "Garcia", 18, "49294288k", "Sant Vicents Dels Horts"]

for datos_personales in my_list: #--> Con el bucle "for" repetimos el mismo codigo con las diferentes posibilidades de la lista o estructura de datos
    print(datos_personales) 
