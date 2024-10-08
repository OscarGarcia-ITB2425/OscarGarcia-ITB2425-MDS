###VAMOS A VERIFICAR UNAS FECHAS DE NACIMIENTO###

#Importamos la funcion "Datetime" 
from datetime import datetime

#Definimos el año actual
año_actual = datetime.now().year

while True:
    
    #Aqui voy a guardar las variabes dia, mes i año
    
    dia_usuario,mes_usuario,año_usuario = int(input("escribe tu dia:")), int(input("Escibe tu mes:")), int(input("Escribe Tu año")) 

    #Si el año es mayor que el año actual es una fecha erronea
    if año_usuario >= año_actual:
        
        print("Escribe una un año de nacimiento real")
    
    #Si el mes es mayor que 12 o menos de 1 --> La fecha es erronea
    elif mes_usuario >= 12 or mes_usuario <= 1:
       
        print("Escribe una un mes de nacimiento real")

    #Si el dia es mayor que 31 los meses que tienen 31, o mas de 30 los meses que tienen 30 dias o mas de 28 en febrero --> La fecha es erronea
    elif dia_usuario >= 31 or ( mes_usuario == (4,6,8,10,12) and dia_usuario >= 30)or (mes_usuario == 2 and dia_usuario >= 28):
        
        print("Escribe una un dia de nacimiento real")
    else:
       
        print("todo corecto, tu fecha de nacimiento es:",dia_usuario,"/",mes_usuario,"/",año_usuario )



            