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

# Aprovecharé conversor_general para forzar la base decimal y filtrar según rango ASCII (32 - 126)
def filtro_ascii_valido(numero,base_origen):
    numero_en_decimal = int(convertor_general(numero,base_origen,10))
    if numero_en_decimal >= 32 and numero_en_decimal <= 126:
        return True
    # Else pa demostrar que lo hice yo y no la ia :v (completamente forzado)
    else:
        return False


# Esta función lee todos los digitos que se consideren validos, que esten de corrido en un archivo y luego muestra el resultado de este numero despues de la conversión llamando a convertor_general
def leer_numero_completo(digitos_validos, file, base_origen, base_destino_elegida, NBO):
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

    # Esto evita lectura de caracter vació, asique luego de esta comprobación puedo hacer el filtrado ASCII y deberia funcionar por cortocircuito
    if whole_number and filtro_ascii_valido(whole_number,base_origen):

        print(
            f"valor: {convertor_general(whole_number, base_origen, base_destino_elegida)} "
            f"(Original: {NBO}{whole_number})"
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
        leer_numero_completo(DIGITOS_VALIDOS_BINARIO, file, 2, base_destino_elegida,"Binario *")
    elif curr_char == "&":
        leer_numero_completo(DIGITOS_VALIDOS_OCTAL, file, 8, base_destino_elegida,"Octal &")
    elif curr_char == "#":
        leer_numero_completo(DIGITOS_VALIDOS_DECIMAL, file, 10, base_destino_elegida,"Decimal #")
    elif curr_char == "!":
        leer_numero_completo(DIGITOS_VALIDOS_HEXADECIMAL, file, 16, base_destino_elegida, "Hexadecimal !")
    # Si file.read() lee un "" significa que el archivo el archivo ya termino
    elif curr_char == "":
        break

