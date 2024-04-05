#Realizar una funcion recursiva que devuelva la suma de los N numeros naturales 

def sumarNumerosNaturales(n):
    if n == 1:
        return 1 
    else:
        return n + sumarNumerosNaturales(n - 1)
    
# ejemplo 

ejemplo = sumarNumerosNaturales(5)
print(ejemplo)