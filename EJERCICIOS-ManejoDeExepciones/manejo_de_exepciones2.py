# Realizar una funcion que reciba como parametros dos cadenas de caracteres conteniendo numeros realeas, sume varios valores 
# y devuelva el resultado como un numero real. Devolver -1 si alguna de las cadenas no contiene un numero valido.

def sumar_numeros_reales(cadena1, cadena2):
    try: 
        if float(cadena1) and float(cadena2):
            True  
    except ValueError:
        return -1
    resultado = float(cadena1) + float(cadena2)
    return resultado
    
    
        
cadenaOne = "43.2"        
cadenaTwo = "1"        
print (sumar_numeros_reales(cadenaOne, cadenaTwo))



