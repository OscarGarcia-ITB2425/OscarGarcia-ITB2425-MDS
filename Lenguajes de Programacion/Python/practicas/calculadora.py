
while True:
# Pedir la operación al usuario

    problema = input("Introduzca el problema a resolver: ")

# Evaluar la expresión usando eval()
    try:
        resultado = eval(problema)
        print("El resultado es:", resultado)
    except ZeroDivisionError:
        print("Error: División por cero")
    except Exception as e:
        print("Error en la expresión:", e)
