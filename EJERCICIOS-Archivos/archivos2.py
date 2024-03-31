# Escribir un programa que premita grabar un archivo los datos de lluvia caida drante un año. Cada linea del archivo se grabará con el siguiente formato
# <dia>;<mes>;<lluvia caida en mm> por ejemlo 25;5;319

archivo = open("EJERCICIOS-Archivos/archivos/archivo_lluvia.txt", "a")
 

while True:
    try:   
        dia = int(input("ingrese el día (1-31): "))
        mes = int(input("ingrese el mes (1-12): "))
        lluvia_caida= float(input("ingrese la lluvia caida en mm: "))

        if not (1 <= dia <= 31 and 1 <= mes <= 12):
            raise ValueError("Los valores de día y mes deben estar dentro de los rangos adecuados")

        archivo.write(f"{dia};{mes};{lluvia_caida}\n")
    
        continuar = input("Desea ingresar mas datos? (s/n): ")
        if continuar.lower() != 's':
            break
       
    except ValueError as e: 
        print("Error:", e)
        print("Por favor ingrese valores válidos.") 


archivo.close()

print("Los datos de lluvia han sido guardados exitosamente.")
