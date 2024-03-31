# desarrollar una funcion que ingrese por teclado un numero natural. La funcion rechaza cualquier ingreso inválido de datos utilizando exepciones.
# Controla que se ingrese un numero, que ese numero sea entero y mayor a cero.
def es_numero_natural():
    while True:
        try:
            numero = int(input("ingrese un número natural: "))
            if numero <= 0:
                print("Debe ingresar un número mayor que a cero")
            else:
                return numero
        except ValueError:
            print("El valor ingresado no es un numero natural") 
            
# ejecutar programa 

numero_natural = es_numero_natural()
print("Ha ingresado el número natural:", numero_natural) 