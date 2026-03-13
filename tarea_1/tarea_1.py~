import time

DIGITOS_VALIDOS_BINARIO = "01"
DIGITOS_VALIDOS_OCTAL = "01234567"
DIGITOS_VALIDOS_DECIMAL = "0123456789"
DIGITOS_VALIDOS_HEXADECIMAL = "0123456789ABCDEF"


# Esta función lee todos los digitos que se consideren validos, que esten de corrido en un archivo y luego usa la función que corresponda para transformar el numero segun la base elegida
def leer_numero_completo(digitos_validos, file):
    whole_number = ""
    while True:
        curr_char = file.read(1)
        if curr_char in digitos_validos:
            whole_number += curr_char
        else:
            break

    # Esta linea es para devolver en un caracter el cursor del archivo, ya que el ultimo caracter que desecho esta función podria haber sido un "!"
    # por ejemplo, lo que alteraria el flujo de "notas_dm" si no se lee en el bucle principal

    file.seek(file.tell() - 1)
    if whole_number:
        print(whole_number)


print("--- DECODIFICADOR DE NOTAS ---\n")
base_elegida = 0
while base_elegida not in ["2", "8", "10", "16"]:
    base_elegida = input(
        "Ingrese la base en la que desea visualizar los datos (2, 8, 10, 16): "
    )
    if base_elegida not in ["2", "8", "10", "16"]:
        print("Ingrese una base valida por favor")

# El cursor del file se mantiene aunque pase este a una funcion y luego vuelva al contexto global al parecer

file = open("notas_dm.txt", "r")
while True:
    curr_char = file.read(1)
    # print(curr_char)
    if curr_char == "*":
        leer_numero_completo(DIGITOS_VALIDOS_BINARIO, file)
    elif curr_char == "&":
        leer_numero_completo(DIGITOS_VALIDOS_OCTAL, file)
    elif curr_char == "#":
        leer_numero_completo(DIGITOS_VALIDOS_DECIMAL, file)
    elif curr_char == "!":
        leer_numero_completo(DIGITOS_VALIDOS_HEXADECIMAL, file)
    # Si file.read() lee un "" significa que el archivo el archivo ya termino
    elif curr_char == "":
        break
