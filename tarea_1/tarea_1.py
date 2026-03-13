import time

DIGITOS_VALIDOS_BINARIO = "01"
DIGITOS_VALIDOS_OCTAL = "01234567"
DIGITOS_VALIDOS_DECIMAL = "0123456789"
DIGITOS_VALIDOS_HEXADECIMAL = "0123456789ABCDEF"

# Al final si o si deberiamos (probablemente) hacer la transformacion intermedia a decimal ya que las herramientas/operadores que tenemos son para trabajar en esta base


def convertor_general(num_original, base_origen, base_destino):
    total = 0
    potencia_actual = 0
    # asi voltean string los vio
    for digit in str(num_original)[::-1]:
        total += int(digit) * base_origen**potencia_actual
        potencia_actual += 1

    # Ahora tengo que encontrar la potencia mas grande por la que poder dividir el numero e ir bajando

    resultado = ""
    potencia_actual = 0
    while total >= base_destino ** (potencia_actual + 1):
        potencia_actual += 1
    while total > 0:
        next_num = 0
        while total >= (next_num + 1) * base_destino**potencia_actual:
            next_num += 1
        total -= next_num * base_destino**potencia_actual
        potencia_actual -= 1
        resultado += str(next_num)
    return resultado


# Esta función lee todos los digitos que se consideren validos, que esten de corrido en un archivo y luego muestra el resultado de este numero despues de la conversión llamando a convertor_general
def leer_numero_completo(digitos_validos, file, base_origen, base_destino_elegida):
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
        print(
            f"valor: {convertor_general(whole_number, base_origen, base_destino_elegida)} original: {whole_number}"
        )


print("--- DECODIFICADOR DE NOTAS ---\n")
base_destino_elegida = 0
while base_destino_elegida not in [2, 8, 10, 16]:
    base_destino_elegida = int(
        input("Ingrese la base en la que desea visualizar los datos (2, 8, 10, 16): ")
    )
    if base_destino_elegida not in [2, 8, 10, 16]:
        print("Ingrese una base valida por favor")

# El cursor del file se mantiene aunque pase este a una funcion y luego vuelva al contexto global al parecer

file = open("notas_dm.txt", "r")
while True:
    curr_char = file.read(1)
    # print(curr_char)
    if curr_char == "*":
        leer_numero_completo(DIGITOS_VALIDOS_BINARIO, file, 2, base_destino_elegida)
    elif curr_char == "&":
        leer_numero_completo(DIGITOS_VALIDOS_OCTAL, file, 8, base_destino_elegida)
    elif curr_char == "#":
        leer_numero_completo(DIGITOS_VALIDOS_DECIMAL, file, 10, base_destino_elegida)
    elif curr_char == "!":
        leer_numero_completo(
            DIGITOS_VALIDOS_HEXADECIMAL, file, 16, base_destino_elegida
        )
    # Si file.read() lee un "" significa que el archivo el archivo ya termino
    elif curr_char == "":
        break
