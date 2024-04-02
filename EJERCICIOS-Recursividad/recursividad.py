# Escribir una funcion que devuelva la cantidad de digitos de un numero entero, sin utilizar cadenas de caracteres

def obtener_numero_de_digitos(numero):
    if abs(numero) < 10:
        return 1
    else: 
        return 1 + obtener_numero_de_digitos(numero // 10)

print(obtener_numero_de_digitos(2210))

# Se utiliza recursividad para la resolucion 