## Integrantes ##
- Gabriel Garcés Rol: 202473555-1
- Martín Araya Rol: 202473646-9
Paralelo: 200 

## Especifiación de algoritmos y desarrollo realizado ##
- Cada una de las funciones está comentada debidamente en el apartado donde fue escrita, creemos que es mas ordenado de esta forma ya que se puede ir viendo al mismo tiempo el código.
- Una especificación importante es respecto a la conversión de hexadecimal a octal y visceversa, ya que el profesor dijo que se podía pasar a binario y luego de eso hacer la conversión correspondiente.
Debido a que, ya teníamos funciones hechas para los casos comentados, decidimos agregar al final las funciones con la lógica de agrupación de bits al tener la representación completa del número en binario.
Al final de archivo se explica mas detalladamente la situación, pero en resumen, hicimos 2 funciones extra.
- El método que estabamos utilizando anteriormente, era un derivado de la agrupación de bits, solo que un poco mas rebuscado, ya que en vez de tener el número convertido completamente en hexadecimal o en
octal, ibamos tomando "bloques" de números y luego de esto ibamos haciendo la conversión correspondiente.


## Supuesto utilizados ##
1. Asumimos que los valores que el usuario ingerará a la base solo pueden ser numeros enteros, se maneja si elige una base diferente a las opciones dadas, pero daría error si ingerasa otro tipo de dato.


## Aclaración ##
- Inciamos la libreria "math" pero solamente para usar "ceil" y "sqrt".


## Entorno ## 
Entorno de ejecución:
- Se utilizó python 3.13.6 y se desarrolló en Windows 11 Pro version 24H2 y Windows 10.
- El código fue desarrollado con Visual Studio Code.
