# escribir una funcion que reciba dos vectores en forma de tupla y devuelva un valor de vedad indicando si son ortogonales o no.

def son_ortogonales(vector1, vector2):
    if len(vector1) != len(vector2):
        return False
    
    resultado_final = sum(a * b for a, b in zip(vector1, vector2))
    return resultado_final == 0


# ejecucion 

v1 = (2,3)
v2 = (-3, 2)

print (son_ortogonales(v1, v2))
