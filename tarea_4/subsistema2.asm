.data
#Aqui hay que cambiar los datos para realizar las pruebas (explicado en el readme)
#Dejaré estos valores de prueba
m:.word 3
arreglo:.word 0x00000001, 0xFFFFFFFF, 0x00000007
TODOBIEN:.asciz " -> LLAVE ACEPTADA - PORTAL ABIERTO\n"
ERROR_REGLA1:.asciz " -> RECHAZADA (Fallo de Paridad)\n"
ERROR_REGLA2:.asciz " -> RECHAZADA (Sobrecarga de Patrón)\n"

.text
main:
#Primero cargo datos en registros "s" porque se usan a lo largo de todo el programa
	la s0, arreglo
	lw s1, m
	addi s2, zero, 0
	addi s3, zero, 32
	addi s4, zero, 30
ciclo:
	beq s2, s1, terminar
	lw t0, 0(s0)
#Para imprimir hexadecimales
	add a0, zero, t0
	li a7, 34
	ecall
    add t6, t0,zero
    addi t3,zero,0
    addi t2,zero,0
    regla1:
	beq t3,s3, chao
	andi t1, t6, 1
	add t2, t2, t1
	srli t6, t6, 1
	addi t3,t3,1
	j regla1
	chao:
# Podemos volver a usar los valores temporales de antes porque no volvemos hacia atrás.
	andi t1,t2,1
	    addi t3,zero,1
	    beq t1,t3,regla2
	    j rr1
    regla2:
    # Ahora puedo usar t0 porque da igual, ya que es la ultima regla
    addi t3,zero,0
    addi t5,zero,7
    postcontador:
	    beq t3, s4, aceptar
	    andi t1, t0, 7
	    beq t1,t5,rr2
	    srli t0, t0,1
	    addi t3,t3,1
    	    j postcontador
aceptar:
    la a0, TODOBIEN
    li a7, 4     
    ecall
    j sig_numero
rr1:
    la a0, ERROR_REGLA1
    li a7, 4
    ecall
    j sig_numero
rr2:
    la a0, ERROR_REGLA2
    li a7, 4
    ecall
sig_numero:
    addi s0, s0, 4
    addi s2, s2, 1
    j ciclo
terminar:
    li a7, 10
    ecall
