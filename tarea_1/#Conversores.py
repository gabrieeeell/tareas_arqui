#Conversores

OCTAL = {
    "0": "000",
    "1": "001",
    "2": "010",
    "3": "011",
    "4": "100",
    "5": "101",
    "6": "110",
    "7": "111"
}

HEXADECIMAL = {
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
    "F": "1111"
}

########################################## DECIMAL ######################################
# De cualquier base a decimal
def a_decimal(num_original, base_origen):
    decimal_a_hexadecimal = {10 : "A", 11 : "B", 12 : "C", 13 : "D", 14 : "E", 15 : "F"}
    hexadecimal_a_decimal = {valor : clave for clave,valor in decimal_a_hexadecimal.items()}
    total = 0
    potencia_actual = 0
    # Se convierte el numero a base 10, multiplicando cada digito por la pontencia que le corresponderia en base 10. ademas de considerar el caso
    # de que hubieran caracteres hexadecimales como A,B,C...
    for digit in str(num_original)[::-1]: # asi voltean los string la gente sin atun
        if digit in hexadecimal_a_decimal:
            digit = hexadecimal_a_decimal[digit]
        total += int(digit) * base_origen**potencia_actual
        potencia_actual += 1
    return total


def desde_decimal(Num,base_destino):
    decimal_a_hexadecimal = {10 : "A", 11 : "B", 12 : "C", 13 : "D", 14 : "E", 15 : "F"}
    resultado = ""
    potencia_actual = 0
    # Este bucle se usa para encontrar la potencia mas grande de la respectiva base por la que poder dividir el numero
    while Num >= base_destino ** (potencia_actual + 1):
        potencia_actual += 1

    # El siguiente bucle ve cuantas veces "cabe" la potencia actual de la base destino en el total y agrega el este numero de veces al resultado
    # en su posición respectiva, luego disminuye "potencia actual" y repite el proceso

    # La segunda condición es para el caso de que el numero sea perfectamente divisible por una potencia superior a 0, ya que en este caso se
    # podria terminar el bucle sin haber agregado los ceros correspondientes al final
    while Num > 0 or potencia_actual >= 0:
        next_num = 0
        while Num >= (next_num + 1) * base_destino**potencia_actual:
            next_num += 1
        Num -= next_num * base_destino**potencia_actual
        potencia_actual -= 1
        if next_num >= 10:
            resultado += decimal_a_hexadecimal[next_num]
        else:
            resultado += str(next_num)
    return resultado

#num_dec = str(input("Digita el numero en base\n"))
#base = int(input("De base (2,8,16) a decimal: \n"))
#print(a_decimal(num_dec,base))


#num_dec = int(input("Digita el numero en decimal\n"))
#base = int(input("A que base (2,8,16): \n"))
#print(desde_decimal(num_dec,base))



###### BINARIO ####

#2ED
def Hexa_a_binario(Num_hexa):
    resultado = ""
    for digito in Num_hexa:
        resultado += HEXADECIMAL[digito]
    return resultado

def Octal_a_binario(Num_oct):
    resultado = ""
    for digito in Num_oct:
        resultado += OCTAL[digito]
    return resultado


#81
def Decimal_a_binario(Num_decimal):
    resultado = ""
    T_res = 1
    Num_decimal = int(Num_decimal)
    while T_res != 0:
        T_res = Num_decimal//2
        resto = Num_decimal% 2
        Num_decimal = T_res
        resultado += str(resto)
        # Lo damo welta sin atun
    return resultado[::-1]



        
    


        
        





