#Vamos a pedir la edad para luego comprobar si es mayor o menor de edad

#Primero quiero comprovar si quiere salir o no
while True:
    edad = input("Introdice tu edad: (o pon 'salir' si quieres salir):")

    if edad.lower() == "salir":
        break
#si no quiere salir entonces convertire el input en un entero i luego comparare si es mayor o menor que 18
    try:
        edad = int(edad)
        if edad >= 18:
            print("Eres mayor de edad")
        else:
            print("Eres menor de edad")
    except edad == ValueError:
        print("Por favor introduzca un numero o escriba 'salir' para salir")



