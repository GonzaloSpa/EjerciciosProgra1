# Escribir una funcion que reciba como parametro una tupla con una fecha (dia,mes,anio) y que devuelva una cadena
# de caracteres con la misma fecha en formato extendido 12 de Octubre de 2020 - 

def cambiar_formato_fecha (fecha):
    meses = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre"
             "Diciembre"]
     
    dia, mes, anio = fecha
    
    cadena_fecha = f"{dia} de {meses[mes]} de {anio}"
    
    return cadena_fecha

# Ejecucion


fecha_tupla = (12,1,1998)
cambiando_formato = cambiar_formato_fecha(fecha_tupla)
print(cambiando_formato)

