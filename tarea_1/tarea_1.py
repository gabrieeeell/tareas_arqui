import time

DIGITOS_VALIDOS_BINARIO = "01"
DIGITOS_VALIDOS_OCTAL = "01234567"
DIGITOS_VALIDOS_DECIMAL = "0123456789"
DIGITOS_VALIDOS_HEXADECIMAL = "0123456789ABCDEF"

# Variable global para el mensaje
mensaje = ""
n = 1

# Al final si o si deberiamos (probablemente) hacer la transformacion intermedia a decimal ya que las herramientas/operadores que tenemos son para trabajar en esta base


def convertor_general(num_original, base_origen, base_destino):
    decimal_a_hexadecimal = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    hexadecimal_a_decimal = {
        valor: clave for clave, valor in decimal_a_hexadecimal.items()
    }
    total = 0
    potencia_actual = 0
    # Se convierte el numero a base 10, multiplicando cada digito por la pontencia que le corresponderia en base 10. ademas de considerar el caso
    # de que hubieran caracteres hexadecimales como A,B,C...
    for digit in str(num_original)[::-1]:  # asi voltean los string la gente sin atun
        if digit in hexadecimal_a_decimal:
            digit = hexadecimal_a_decimal[digit]
        total += int(digit) * base_origen**potencia_actual
        potencia_actual += 1

    resultado = ""
    potencia_actual = 0
    # Este bucle se usa para encontrar la potencia mas grande de la respectiva base por la que poder dividir el numero
    while total >= base_destino ** (potencia_actual + 1):
        potencia_actual += 1

    # El siguiente bucle ve cuantas veces "cabe" la potencia actual de la base destino en el total y agrega el este numero de veces al resultado
    # en su posición respectiva, luego disminuye "potencia actual" y repite el proceso

    # La segunda condición es para el caso de que el numero sea perfectamente divisible por una potencia superior a 0, ya que en este caso se
    # podria terminar el bucle sin haber agregado los ceros correspondientes al final
    while total > 0 or potencia_actual >= 0:
        next_num = 0
        while total >= (next_num + 1) * base_destino**potencia_actual:
            next_num += 1
        total -= next_num * base_destino**potencia_actual
        potencia_actual -= 1
        if next_num >= 10:
            resultado += decimal_a_hexadecimal[next_num]
        else:
            resultado += str(next_num)
    return resultado


# Aprovecharé conversor_general para forzar la base decimal y filtrar según rango ASCII (32 - 126)
def filtro_ascii_valido(numero, base_origen):
    numero_en_decimal = int(convertor_general(numero, base_origen, 10))
    if numero_en_decimal >= 32 and numero_en_decimal <= 126:
        # En este punto numero_en_decimal será cada numero en orden que sea válido dentro del rango ascci, por lo que se puede decodificar el mensaje e irlo almacenando
        # Conviene hacer la traducción ASCII debido a que los caracteres son válidos, se usa una variable global para ir almacenando el mensaje
        global mensaje
        mensaje += chr(numero_en_decimal)

        ## ESTAS 2 LINEAS SON PARA VER SI LA CONVERSIÓN SE HACIA CORRECTAMENTE, HAY QUE BORRARLAS DESPUÉS, PERO SE VE QUE EL 0x68 se traduce a 104 en base 10 pero la tarea
        # lo consdiera como di fuera 100, pq 100 es "d" en ASCII, pero al hacer la conversión correcta da 104, que es "h" en ASCII
        # print("el numero es" , numero, "en", base_origen)
        # print(numero_en_decimal)

        ##
        return True

    # Else pa demostrar que lo hice yo y no la ia :v (completamente forzado) [ademas la ia no usa variables globales 😎]
    else:
        return False


# Esta función lee todos los digitos que se consideren validos, que esten de corrido en un archivo y luego muestra el resultado de este numero despues de la conversión llamando a convertor_general
def leer_numero_completo(digitos_validos, file, base_origen, base_destino_elegida, NBO):
    numero_completo = ""
    while True:
        curr_char = file.read(1)
        if curr_char in digitos_validos:
            numero_completo += curr_char
        else:
            break

    # Esta linea es para devolver en un caracter el cursor del archivo, ya que el ultimo caracter que desecho esta función podria haber sido un "!"
    # por ejemplo, lo que alteraria el flujo de "notas_dm" si no se lee en el bucle principal

    file.seek(file.tell() - 1)

    # Esto evita lectura de caracter vació, asique luego de esta comprobación puedo hacer el filtrado ASCII y deberia funcionar por cortocircuito
    if numero_completo and filtro_ascii_valido(numero_completo, base_origen):
        global n
        print(
            f"valor {n}: {convertor_general(numero_completo, base_origen, base_destino_elegida)} "
            f"(Original: {NBO}{numero_completo})"
        )
        n += 1


print("--- DECODIFICADOR DE NOTAS ---\n")
base_destino_elegida = 0
while base_destino_elegida not in [2, 8, 10, 16]:
    base_destino_elegida = int(
        input("Ingrese la base en la que desea visualizar los datos (2, 8, 10, 16): ")
    )
    if base_destino_elegida not in [2, 8, 10, 16]:
        print("Ingrese una base valida por favor")

# El cursor del file se actualiza también en el contexto global cuando este se mueve en una función

file = open("notas_dm.txt", "r")
while True:
    curr_char = file.read(1)
    # print(curr_char)
    if curr_char == "*":
        leer_numero_completo(
            DIGITOS_VALIDOS_BINARIO, file, 2, base_destino_elegida, "Binario *"
        )
    elif curr_char == "&":
        leer_numero_completo(
            DIGITOS_VALIDOS_OCTAL, file, 8, base_destino_elegida, "Octal &"
        )
    elif curr_char == "#":
        leer_numero_completo(
            DIGITOS_VALIDOS_DECIMAL, file, 10, base_destino_elegida, "Decimal #"
        )
    elif curr_char == "!":
        leer_numero_completo(
            DIGITOS_VALIDOS_HEXADECIMAL, file, 16, base_destino_elegida, "Hexadecimal !"
        )
    # Si file.read() lee un "" significa que el archivo ya termino
    elif curr_char == "":
        break


print("\nMENSAJE DECODIFICADO:\n", mensaje)

# Una vez a un loco le pusieron un 0 en el certamen de progra pq no cerró el archivo :v
file.close()

