# Desarrollar una funcion que determine si una cadena de caracteres es capicúa, sin utilizar cadenas auxiliares ni rebanadas.
# Escribir ademas un programa que permita verificar su funcionamiento.


def es_capicua(cadena):
    longitud = len(cadena)
    for i in range(longitud // 2):
        if cadena[i] != cadena[longitud - i - 1]: # no rebanada, indexacion de la cadena
            return False
    return True   

# Ejecucion 

cadena = input("Ingrese una cadena de caracteres: ")
if es_capicua(cadena):
    print("La cadena es capicúa.")
else:
        print("La cadena no es capicúa.")