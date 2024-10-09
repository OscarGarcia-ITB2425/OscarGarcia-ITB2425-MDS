###CONDICIONALES###

mi_condicion = True

if mi_condicion:
    print("Se imprime a consecuencia del 'if' ") #--> Un condicional normal donde si es "true" se ejecuta el codigo adjunto.

mi_condicion = (5*2)+1

if mi_condicion == 11:
    print("tu numero es 11!") #--> En este otro condicional simplemente continua con el codigo cuando "mi_condicion" es igual a 11
else:
    print("tu numero no es 11!") #--> Con el "else" continuamos el codigo en caso de que el "if" no se cumpla.

# Podemos utilizar los operadores logicos para especificar los condicionales:

if mi_condicion > 10 and mi_condicion < 20:
    print("tu numero esta entre el 10 i el 20")

elif mi_condicion == 50:
                              #--> Con el comando "elif" agrego otra comprovacion antes de saltar al "else" en caso de no cumplirse el "if"
    print("tu numero es 50")

else:
    print("tu numero esta fuera del rango entre 10 i 20")