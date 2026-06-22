Integrantes:
Gabriel Garcés Mimo Rol: 202473555-1 Paralelo 200
Martín Araya Díaz   Rol: 202473646-9 Paralelo 200



Especificaciones de los algoritmos y desarrollo realizado:
- Para el desarrollo de este laboratorio se realizaron 2 desafíos en Asembly mediante RARS 1.6.
- El desarrollo y supuesto está en la explicación de cada desafío presente en este archivo


Explicación desafío 1:




Explicación desafío 2:
- Supuestos:
1. Asumimos que las entradas se deben modificar dentro del código. Para esto, se deben cambiar los datos indicados en el archivo, que serían los valores de "m" y "arreglo"
2. Se asume que los valores hexadecimales válidos.
3. Se asume que el valor de "m" corresponde con la cantidad de números, ya que de otra forma simplemente se harán iteraciones extra.

- Primero lo que se hace es cargar constantes que se usaran a lo largo del programa en registros "s".
- Tanto la comprobación para la regla 1 y 2 están dentro de un "bucle" principal llamado "ciclo".
- En cada iteración general se comprueban ambas reglas para cada número de 32 bits.
- Para comprobar la regla 1 lo que se hace es guardar valores temporales y hacer un bucle, posteriormente se itera 32 veces por cada número, ya que lo que se hace es comparar cada bit con un 1, esto se logra mediante un "andi", debido a que si hacemos un "andi" con un numero y 1 logramos que, en caso de que el último bit sea un 1, el resultado en 1, en caso contrario es 0. Por lo tanto, se va acumulando la suma en un valor temporal. Para comprobar cada bit, se debe hacer un shift a la derecha del número (para comprobar con el bit del lado).
- Luego para comprobar la regla 2 lo que se hace es utilizar una comparación con el número 7 (ya que 7 es 0111, pero debido a que se hace un shift lógico, se rellenan con 0s, entonces de todas formas se detecta el patrón). De forma similar a la regla 1, se utiliza un "andi", para comprobar los últimos 3 bits, en caso de que sean 111 se sale del bucle porque se rechaza la regla 2, en caso contrario se comprueban todos los bits y se acepta directamente el número, debido a que la ejecución es secuencial, por lo tanto si está en la regla 2, ya pasó la regla 1.
- Finalmente se repite el proceso para cada número gracias al contenido del label "sig_numero", donde se incrementa el puntero en 4 bytes.
- Para imprimir por pantalla y finalizar el programa se utilizan los códigos presentes en RARS 1.6 Help (se accede con F1), específicamente en la sección "Syscalls".


Instrucciones de compilación y ejecución en RARS:
1. Abrir RARS
2. Seleccionar el archivo en file -> Open -> subsistema(1 o 2).asm
3. Una vez abierto, seleccionar en las funcionalidades de la barra superior "Assemble the current file and clear breakpoints"
4. Seleccionar "Run the current program"
5. Ver salida en Run I/O
