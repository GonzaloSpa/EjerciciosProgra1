def grabarRangoAltura():
    archivo = open("EJERCICIOS-Archivos\\archivos\\archivo_atleta.txt", "a")
    
    
    deporte = input("Especifique el deporte: ")
    archivo.write(f"{deporte}\n")
    
    contador_atleta = 0
    while True:
        contador_atleta += 1
        altura_atleta = input(f"Especifique altura del atleta {contador_atleta}: ")
        archivo.write(f"{altura_atleta} altura del atleta {contador_atleta}\n")
        continuar = input("Desea ingresar mas datos? (s/n): ")
        if continuar.lower() != 's':
            break
       

        
def grabarPromedio():
    archivo = open("EJERCICIOS-Archivos\\archivos\\archivo_atleta.txt", "r")
    lineas = archivo.readlines()
    
    alturas = []
    
    for linea in lineas:
        palabras = linea.split()
    
        primera_palabra = palabras[0]
    
        try:
            altura = float(primera_palabra)
            alturas.append(altura)
        except ValueError:
            pass    
      
    if alturas:
        promedio = sum(alturas) / len(alturas)
        
    nuevo_archivo = open("EJERCICIOS-Archivos\\archivos\\archivo_atleta_promedio.txt", "a")
    nuevo_archivo.write(f"la altura promedio de los deportistas es {promedio}")
    
    archivo.close()
    nuevo_archivo.close()


grabarPromedio()
    