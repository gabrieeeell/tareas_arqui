import math

# Conversores

"""
Diccionario para realizar conversión de números octales a binarios
"""
OCTAL_A_BINARIO = {
    "0": "000",
    "1": "001",
    "2": "010",
    "3": "011",
    "4": "100",
    "5": "101",
    "6": "110",
    "7": "111",
}

"""
Se invirtió el diccionario anterior para realizar la agrupación de bits y transformar un
número binario a octal
"""
BINARIO_A_OCTAL = {binario: octal for octal, binario in OCTAL_A_BINARIO.items()}


"""
Diccionario para realizar conversión de números hexadecimales a binarios
"""
HEXADECIMAL_A_BINARIO = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}
"""
Se invirtió el diccionario anterior para realizar la agrupación de bits y transformar un
número binario a hexadecimal
"""
BINARIO_A_HEXADECIMAL = {
    binario: hexadecimal for hexadecimal, binario in HEXADECIMAL_A_BINARIO.items()
}


########################################## DECIMAL ######################################

"""
Nombre: a_decimal()
Entradas:
- num_original: string 
- base_origen: int 

Descripción:
Esta función transforma un número de cualquier base a decimal, para esto lo que hace es, primero que todo definir un diccionario en caso de 
que se esté trabajando con números hexadecimales, de forma que se puedan traducir las letras a números.
Luego lo que se hace es dar vuelta el número original (que puede ser binario, octal o hexadecimal solamente) e ir multiplicando el valor del dígito,
con la base elevada a la potencia actual (que comienza en 0 y va incrementando, debido a esto se da vuelta el número original, ya que a priori no sabemos el
largo total del número).
Finalmente se va guardando el resultado. 

Salida: Retorna un número entero que representa el valor en base 10.
"""


def a_decimal(num_original: str, base_origen):
    decimal_a_hexadecimal = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    hexadecimal_a_decimal = {
        valor: clave for clave, valor in decimal_a_hexadecimal.items()
    }
    total = 0
    potencia_actual = 0
    for digit in num_original[::-1]:
        if digit in hexadecimal_a_decimal:
            digit = hexadecimal_a_decimal[digit]
        total += int(digit) * base_origen**potencia_actual
        potencia_actual += 1
    return total


"""
Nombre: desde_decimal()
Entradas:
- num_original: int 
- base_destino: int

Descripción:
La función primero ve la potencia más grande de la base destino que es menor a num_original, para depués ver exactamente cuantas veces cabe esta en num_original
y añadir la cantidad "n" de veces que haya cabido la potencia como digito al resultado, ademas de restar "n * (base_destino ** potencia_actual)" a num_original.
Luego se repite el proceso pero disminuyendo en uno la potencia y se empezando a trabajar con el digito de la derecha del resultado (ya que el disminuir al 
potencia que esta diviendo, debe tener menor significancia el digito
Cabe resaltar que la cantidad "n" de veces que quepa la potencia en el numero siempre sera menor a "base_destino" ya que sino se hubiera empezado a trabajar
con una potencia mayor al principio de la función y el resulado de "num_original - (n * base_destino**potencia_actual)" como debe ser menor a 
"base_destino**potencia_actual", se tendra que al disminuir en uno la potencia acutal, "base_destino**(potencia_actual - 1)" solo podra caber (base_destino - 1)
veces como maximo en lo que quede de num_original

Salida: Un string de la representación del num_original pero en la base_destino elegida
"""


def desde_decimal(num_original: int, base_destino):
    decimal_a_hexadecimal = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    resultado = ""
    potencia_actual = 0
    # Este bucle se usa para encontrar la potencia mas grande de la respectiva base por la que poder dividir el numero
    while num_original >= base_destino ** (potencia_actual + 1):
        potencia_actual += 1

    # El siguiente bucle ve cuantas veces "cabe" la potencia actual de la base destino en el total y agrega el este numero de veces al resultado
    # en su posición respectiva, luego disminuye "potencia actual" y repite el proceso

    # La segunda condición es para el caso de que el numero sea perfectamente divisible por una potencia superior a 0, ya que en este caso se
    # podria terminar el bucle sin haber agregado los ceros correspondientes al final
    while num_original > 0 or potencia_actual >= 0:
        next_num = 0
        while num_original >= (next_num + 1) * base_destino**potencia_actual:
            next_num += 1
        num_original -= next_num * base_destino**potencia_actual
        potencia_actual -= 1
        if next_num >= 10:
            resultado += decimal_a_hexadecimal[next_num]
        else:
            resultado += str(next_num)
    return resultado


###### Hexadecimal & Octal ######

"""
Nombre: hexa_a_octal()
Entradas:
- num_hexa: string

Descripción:
Se tiene un "binario_parcial_del_hexadecimal" que son los ultimos digitos del hexadecimal que todavia no se hayan usado, pero convertidos a binario,
en el bucle principal, se mantiene que los bits de este numero siempre sean almenos 3, para transformar 3 bits en su digito octal equivalente, añadiendo este
al resultado
Al final de la función, si llego a sobrar una cantidad de bits < 3, en "binario_parcial_del_hexadecimal", se rellena con 0 para que llegue a 3 bits y se
pasa a octal

Salida: Un string de la representacion octal del hexadecimal de entrada
"""


# Por email se dijo que las conversiones se tienen que hacer sin tener una "base puente" entre 2 bases, sin embargo entre octal y hexadecimal esto es imposible cumplirlo al 100%
# almenos que se use un diccionario con 4096 entradas, por lo que ire conviertiendo solo algunos digitos del hexadecimal a la vez e ire pasando estos a octal
# entonces se podria decir que estoy haciendo una conversion "parcial" a binario
def hexa_a_octal(num_hexa: str):
    # fmt: off
    resultado = ""
    binario_parcial_del_hexadecimal = ""
    num_hexa = num_hexa[::-1]
    while len(num_hexa) > 0:
        if len(binario_parcial_del_hexadecimal) < 3:
            binario_parcial_del_hexadecimal = HEXADECIMAL_A_BINARIO[num_hexa[0]] + binario_parcial_del_hexadecimal
            num_hexa = num_hexa[1:]
        # Ocupo los 3 primeros digitos para pasarlos a su representacion octal y luego los saco de la variable
        resultado = BINARIO_A_OCTAL[binario_parcial_del_hexadecimal[-3:]] + resultado # obtengo los 3 ultimos digitos

        binario_parcial_del_hexadecimal = binario_parcial_del_hexadecimal[:-3]

    # Aca puede ser que binario_parcial_del_hexadecimal haya quedado con 1 o 2 digitos, en tal caso se extiendo con ceros a la izquierda y se la ultima conversion
    while len(binario_parcial_del_hexadecimal) > 0 and len(binario_parcial_del_hexadecimal) < 3 and binario_parcial_del_hexadecimal.count("0") != len(binario_parcial_del_hexadecimal):
        binario_parcial_del_hexadecimal = "0" + binario_parcial_del_hexadecimal

        resultado = BINARIO_A_OCTAL[binario_parcial_del_hexadecimal[-3:]] + resultado

    # Si el input fueron solo ceros, el código se ira por este caso
    if not resultado or resultado.count("0") == len(resultado):
        return "0"

    return resultado


"""
Nombre: octal_a_hexa
Entrada: 
- num_octal : str
Descripción:
Se tiene un "binario_parcial_del_octal" que son los ultimos digitos del octal que todavia no se hayan usado, pero convertidos a binario,
en el bucle principal, se mantiene que los bits de este numero siempre sean almenos 4, para transformar 4 bits en su digito hexadecimal equivalente, añadiendo este
al resultado
Al final de la función, si llego a sobrar una cantidad de bits < 4, en "binario_parcial_del_octal", se rellena con 0 para que llegue a 4 bits y se
pasa a hexadecimal

Salida: El string de la representación hexadecimal del octal de entrada
"""


def octal_a_hexa(num_octal: str):
    # fmt: off
    resultado = ""
    binario_parcial_del_octal = ""
    num_octal = num_octal[::-1]
    while len(num_octal) > 0:
        if len(binario_parcial_del_octal) < 4:
            binario_parcial_del_octal = OCTAL_A_BINARIO[num_octal[0]] + binario_parcial_del_octal
            num_octal = num_octal[1:]

        # Por si dentro del anterior if, se alcanza el len() correcto. Si esto fuera un else, el bucle podria terminar sin ver el ultimo byte
        if len(binario_parcial_del_octal) >= 4:
            resultado = BINARIO_A_HEXADECIMAL[binario_parcial_del_octal[-4:]] + resultado # obtengo los 3 ultimos digitos
            binario_parcial_del_octal = binario_parcial_del_octal[:-4]

    # Se agregan 0's para completar el ultimo hexadecimal en caso de que no alcance los 4 bits
    while len(binario_parcial_del_octal) > 0 and len(binario_parcial_del_octal) < 4 and binario_parcial_del_octal.count("0") != len(binario_parcial_del_octal):
        binario_parcial_del_octal = "0" + binario_parcial_del_octal
    if len(binario_parcial_del_octal) == 4:
        resultado = BINARIO_A_HEXADECIMAL[binario_parcial_del_octal[-4:]] + resultado

    # Si el input fueron solo ceros, el código se ira por este caso
    if not resultado or resultado.count("0") == len(resultado):
        return "0"

    return resultado


###### BINARIO ####

"""
Nombre: Hexa a binario
Entrada:
- Num_hexa : str
Descripción:
Lo que hace esta función es ir concatenando la representación de 4-bits de cada uno de los carácteres del
número en hexadecimal y al quita los ceros de la izquierda (Solo por temas estéticos, esto básicamente no afecta
el valor del resultado)

Salida: Transforma el string de un número hexadecimal a un string con su representación en binario.
"""


def Hexa_a_binario(Num_hexa):
    resultado = ""
    for digito in Num_hexa:
        resultado += HEXADECIMAL_A_BINARIO[digito]
    # Quitamos los ceros de sobra que puedan quedar al principio
    while resultado[0] == "0" and len(resultado) > 1:
        resultado = resultado[1:]
    return resultado


"""
Nombre: Octal_a_binario
Entrada: Num_oct (String)
Descripción:
Lo que hace esta función es ir concatenando la representación de 3-bits de cada uno de los carácteres del
número en octal y al quita los ceros de la izquierda (Solo por temas estéticos, esto básicamente no afecta
el valor del resultado)

Salida: Transforma el string de un número octal a un string con su representación en binario.
"""


def Octal_a_binario(Num_oct):
    resultado = ""
    for digito in Num_oct:
        resultado += OCTAL_A_BINARIO[digito]
    while resultado[0] == "0" and len(resultado) > 1:
        resultado = resultado[1:]
    return resultado


"""
Nombre: Decimal_a_binario
Entrada: Num_decimal (String)
Descripción:
Esta función recibe un string (Por temas de coherencia con las otras funciones), pero se trabaja con su valor entero (Por eso se hace el casting).
Lo que se busca es ir dividiendo el número en 2 e ir guardando el resto de cada división, luego se repite este proceso hasta que 
el resultado de la división sea 0. 
En cada una de las iteraciónes se va guardando el respectivo resto de la división, y finalmente se debe dar vuelta el resultado para
conseguir la representación binaria válida.

Salida: Transforma el string de un número decimal a un string con su representación en binario.
"""


def Decimal_a_binario(Num_decimal):
    resultado = ""
    T_res = 1
    Num_decimal = int(Num_decimal)
    while T_res != 0:
        T_res = Num_decimal // 2
        resto = Num_decimal % 2
        Num_decimal = T_res
        resultado += str(resto)
    while resultado[0] == "0" and len(resultado) > 1:
        resultado = resultado[1:]
    return resultado[::-1]


"""
Nombre: desde_binario_a_hexa_o_octal()
Entradas:
- num_original: string
- base_destino: int
Descripción:
Lo que hace esta función es identificar en primera instancia si se está trabajado con octales o con hexadecimales, en base
a esto se asigna una base destino (8 o 16) y se utiliza un conversor (el cual tiene la representaciónes decimales de 3 y 4 bits).
Luego se identifica la cantidad de bits por digito (para agrupar de 3-bits si se requiere octal o de 4-bits si se requiere hexadecimal)
Luego lo que se hace es ir tomando desde el "final" hacia delante los dígitos binarios e irlos agrupando según la base_destino.
Finalmente para el caso donde el ultimo bloque de dígitos binarios no corresponda con el largo, se rellena a la izquierda con 0's.
En el caso de que el último bloque de dígitos binarios corresponda con el largo (ósea que el largo original sea múltiplo de 3 o 4), entonces
simplemente se agrega la representación al resultado retorna el string resultado.

Salida: Toma un número en binario, una base (8 o 16) y entrega un string con el binario representado en la base elegida.
"""


def desde_binario_a_hexa_o_octal(num_original, base_destino):
    # fmt: off
    resultado = ""
    if base_destino == 8 or base_destino == 16:
        conversor_correspondiente = BINARIO_A_OCTAL if base_destino == 8 else BINARIO_A_HEXADECIMAL
        cantidad_de_bits_por_digito = math.ceil(math.sqrt(base_destino))  # 8 -> 3, 16 -> 4
        while len(num_original) >= cantidad_de_bits_por_digito:
            resultado = conversor_correspondiente[num_original[-cantidad_de_bits_por_digito:]] + resultado
            num_original = num_original[:-cantidad_de_bits_por_digito]
        while len(num_original) > 0 and len(num_original) < cantidad_de_bits_por_digito:
            num_original = "0" + num_original
        if len(num_original) == cantidad_de_bits_por_digito:
            resultado = conversor_correspondiente[num_original[-cantidad_de_bits_por_digito:]] + resultado
        return resultado


    """
El profesor en clases dijo que, para pasar de hexadecimal a octal y visceversa se puede representar en binario, ya que el objetivo de aprendizaje
de la tarea es que nosotros sepamos que al tener un número en binario, se puede pasar directamente a base 8 o 16 según cuantos bits se agrupen. Antes de esto ya habiamos
hecho la función hexa_a_octal y octal_a_hexa, asique las seguiremos utilizando.
De todas formas dejaremos escritas las funciones de agrupación de bits para los casos mencionados anteriormente.

Realmente la lógica es bastante simple y similar para ambos casos, lo que se hace es rellenar con 0s el lado izquierdo de forma que, el largo de la representación en binario
para ambos casos sea divisible perfectamente por 4 si se quiere pasar a hexadecimal y por 3 si se quiere pasar a octal. Luego simplemente se van viendo por bloques de 
4 o 3 bits y se va buscando la represetación en el diccionario (tal como se haría con lapiz y papel).

En ambos casos se espera un string como entrada

def hexa_a_octal_abits(Num_hexa):
    resultado = ""
    HexaBits = Hexa_a_binario(Num_hexa)[::-1]
    while len(HexaBits) % 3 != 0:
        HexaBits += "0"
    HexaBits = HexaBits[::-1]
    i = 0
    f = 3
    veces = len(HexaBits)//3
    while veces > 0:
        resultado += BINARIO_A_OCTAL[HexaBits[i:f]]
        i+=3
        f+=3
        veces-=1
    return resultado


def octal_a_hexa_abits(Num_octal):
    resultado = ""
    HexaBits = Octal_a_binario(Num_octal)[::-1]
    while len(HexaBits) % 4 != 0:
        HexaBits += "0"
    HexaBits = HexaBits[::-1]
    i = 0
    f = 4
    veces = len(HexaBits)//4
    while veces > 0:
        resultado += BINARIO_A_HEXADECIMAL[HexaBits[i:f]]
        i+=4
        f+=4
        veces-=1
    return resultado

"""
