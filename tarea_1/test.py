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


a = "1005"

print(convertor_general(a, 10, 2))
