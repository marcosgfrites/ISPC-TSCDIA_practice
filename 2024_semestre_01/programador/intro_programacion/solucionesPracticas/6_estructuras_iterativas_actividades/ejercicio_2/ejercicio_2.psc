Algoritmo ejercicio_2
	valor_ingresado <- 0
	contador_ciclo <- 0
	
	Escribir '- Sistema de Muestra de Números Pares -'
	Escribir ''
	
	Escribir 'Ingrese un número:'
	Leer valor_ingresado
	
	Repetir
		Si contador_ciclo % 2 = 0 Entonces
			Escribir contador_ciclo
		FinSi
		contador_ciclo <- contador_ciclo + 1
	Hasta Que contador_ciclo > valor_ingresado
FinAlgoritmo	