# Una funcion que reciba como parametro una cadena de caracteres conteniendo una direccion de correo electronico y devuelva una tupla con las
# distintas partes que componene dicha direccion. ejemplo gspaltro@uade.edu.ar -> (alguien, uade, edu, ar)

def separar_email (email):
    lista = []
    for caracter in email:
        if caracter == "@" or caracter == ".":
            lista.append(" ")
        else:
            lista.append(caracter)
    string = ''.join(lista).split()
    a_tupla = tuple(string)
    return a_tupla

#Ejecuion
print (separar_email("gspaltro@uade.edu.ar"))