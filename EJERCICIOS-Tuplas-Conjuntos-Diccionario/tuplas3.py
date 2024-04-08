# escribir una funcion que indique si dos fichas de domino encajan o no. Las fichas son recibidas en dos tuplas ejemplo (3, 4) y (3, 5) la funcion 
# devuelve True o False

def es_domino(ficha1, ficha2):
    for numero in ficha1:
        if numero in ficha2:
            return True
    return False


#ejecucion 

f1 = (5, 6)
f2 = (6, 3)

print (es_domino(f1, f2))