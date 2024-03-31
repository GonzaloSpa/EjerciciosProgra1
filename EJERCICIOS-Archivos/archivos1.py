""" desarrollar un programa que elimine los comentarios de un programa de python y los docstings"""
import re 

def eliminar_comentarios_y_docstrings(linea):
    try:
        linea = re.sub(r'#[^\n]*', '', linea) #Expresion regular para eliminar un comentario de una linea
        
        # Expresión regular para eliminar docstrings de una línea
        linea = re.sub(r'(\'\'\'.*?\'\'\'|\"\"\".*?\"\"\")', '', linea)
    
        return linea
    except FileNotFoundError:
        print("No existe el archivo")

#ejecucion 

archivo_entrada = 'EJERCICIOS-Archivos\entrada.py'
archivo_salida = 'EJERCICIOS-Archivos\salida.py'   # crar esos archivos para comprobar el funcionamiento

# Abrir el archivo de entrada y leer su contenido línea por línea
with open(archivo_entrada, 'r') as archivo_entrada:
    lineas = archivo_entrada.readlines()

# Filtrar las líneas eliminando comentarios y docstrings
lineas_filtradas = [eliminar_comentarios_y_docstrings(linea) for linea in lineas]

# Escribir el contenido filtrado en el archivo de salida
with open(archivo_salida, 'w') as archivo_salida:
    archivo_salida.writelines(lineas_filtradas)

print("Se han eliminado los comentarios y docstrings del archivo de entrada.")