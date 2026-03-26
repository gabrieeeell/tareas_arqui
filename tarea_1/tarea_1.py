import conversores

DIGITOS_VALIDOS_BINARIO = "01"
DIGITOS_VALIDOS_OCTAL = "01234567"
DIGITOS_VALIDOS_DECIMAL = "0123456789"
DIGITOS_VALIDOS_HEXADECIMAL = "0123456789ABCDEF"

# Variable global para el mensaje
mensaje = ""
# Variable global para el contador (para cumplir con el formato en el que se muestran los datos)
n = 1




"""
Nombre: convertor_general()
Entradas:
- num_original: string
- base_origen: int
- base_destino: int

Descripción:
Esta función se encarga de conectar cada una de las transformaciones de base presentes en el archivo "conversores".
Recibe el número, la base de origen y la base de destino, luego de esto ve a que base se debe converir el número. 
Si la base origen es igual a la destino entonces no se modifica nada. 
Si la base origen es 10, entonces se llama a la función que transforma un número de base 10 a cualquier base.
Si la base destino es 10, entonces se llama a la función que transforma desde cualquier base a base 10.
Si la base destino es 2 se ve si la base origen es 8 o 16 (ya que no puede ser 10), y se llama a las respectivas funciones
que transforman de octal a binario y de hexadecimal a binario.
Si la base origen es 16 y la base destino es 8, entonces se llama a la conversion de hexadecimal a octal.
Si la base origen es 8 y la base destino es 16, se llama a la conversión de octal a hexadecimal.
Finalmente si la base origen es 2, entonces se llama a la función que transforma binarios en octales o hexadecimales (ya que usa la lógica de agrupación de bits).

Salida: Retorna un string con la representación del número en la base destino solicitada.
"""
def convertor_general(num_original, base_origen, base_destino):
    if base_destino == base_origen:
        return num_original
    elif base_origen == 10:
        return conversores.desde_decimal(int(num_original), base_destino)
    elif base_destino == 10:
        return conversores.a_decimal(num_original, base_origen)
    elif base_destino == 2:
        if base_origen == 8:
            return conversores.Octal_a_binario(num_original)
        elif base_origen == 16:
            return conversores.Hexa_a_binario(num_original)
    elif base_origen == 16 and base_destino == 8:
        return conversores.hexa_a_octal(num_original)
    elif base_origen == 8 and base_destino == 16:
        return conversores.octal_a_hexa(num_original)
    elif base_origen == 2:
        return conversores.desde_binario_a_hexa_o_octal(num_original, base_destino)

"""
Nombre: filtro_ascii_valido()
Entradas:
- numero: string 
- base_origen: int

Descripción:
Esta función se encarga de ver si un número en cierta base cumple con que su valor en base 10 está dentro del rango ASCII.
Como se comentó en el foro, utilizamos la conversión a decimal para ver el rango ASCII.
Lo que hace la función es convertir el número, ver si está dentro del rango e ir almacenando el mensaje decodificado.

Salida: 
Booleano (True si el número es un carácter ASCII válido, False en caso contrario).
"""
def filtro_ascii_valido(numero, base_origen):
    numero_en_decimal = int(conversores.a_decimal(numero, base_origen))
    if numero_en_decimal >= 32 and numero_en_decimal <= 126:
        global mensaje
        mensaje += chr(numero_en_decimal)
        return True
    else:
        return False

"""
Nombre: leer_numero_completo()
Entradas:
- digitos_validos: string 
- file: el archivo de donde se está leyendo
- base_origen: int 
- base_destino_elegida: int 
- NBO: string (el nombre de la base original para el print, ej: "Octal &").

Descripción:
Esta función se encarga de extraer los datos encriptados del archivo, en el flujo del programa se llama cuando se detecta 
alguno de los carácteres que indican que luego viene un número (*, &, # y !).
Primero que todo lee carácter por carácter concatenando los dígitos válidos (para que no haya error si hay varios prefijos seguidos, por ejemplo el "!!68").
Luego se devuelve el cursor del archivo para que no exista la casualidad que quede justo encima de un caracter cuyo número haya que leer.
Posterior a esto se llama a la función convertor_general, con el número, la base origen y la base destino, como se comentó anteriormente, conversor general llama 
a los conversores presentes en el archivo "conversores.py" (Lo hicimos de esta forma ya que creemos que queda mas limpio el código).
Y además, se muestra el valor por pantalla con el formato pedido (por eso se incrementa el valor de la variable global "n"), pero solamente si se cumple
que está dentro del rango ASCII, ya que esta función retorna un booleano al mismo tiempo que va almacenando el mensaje encriptado.

Salida: No retorna un valor pero imprime en la consola el valor convertido a la base destino y el número original, siempre y cuando estén dentro del rango ASCII (osea 
que afecten al mensaje condificado).

"""
def leer_numero_completo(digitos_validos, file, base_origen, base_destino_elegida, NBO):
    numero_completo = ""
    while True:
        curr_char = file.read(1)
        if curr_char in digitos_validos:
            numero_completo += curr_char
        else:
            break
    file.seek(file.tell() - 1)
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
print(
    "[+] Procesando archivo: notas_dm.txt...\n[!] Filtrando ruido místico (valores fuera de rango ASCII)...\n"
)
print(
    f"LISTA DE VALORES EXTRAÍDOS (Base {base_destino_elegida}):\n--------------------------------------------------"
)
file = open("notas_dm.txt", "r")
while True:
    curr_char = file.read(1)
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
    elif curr_char == "":
        break
print("--------------------------------------------------\n")


print("\nMENSAJE DECODIFICADO:")
print(f"{mensaje}\n\n[Proceso finalizado con éxito]")
file.close()
