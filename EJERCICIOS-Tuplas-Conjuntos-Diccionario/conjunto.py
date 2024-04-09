# Ingresar la frase desde el teclado y usar un conjunto para eliminar las palabras repetidas, dejando un solo ejmplar en cada una. Mostrar las palabras ordenados segun 
# su longitud

frase = input("Escribir una frase: ")
palabras = frase.split()

conjunto_palabras = set()

for palabra in palabras:
    conjunto_palabras.add(palabra)
    
palabras_ordenadas = sorted(conjunto_palabras, key=len)




print(palabras_ordenadas)