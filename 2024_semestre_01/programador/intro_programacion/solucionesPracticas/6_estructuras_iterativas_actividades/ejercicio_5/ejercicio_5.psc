Funcion Estructura_Iterativa_Mientras
	numero_ingresado <- 0
	control_ciclo <- 1
	Escribir ''
	Escribir '- Sistema de Tablas de Multiplicar | Estructura Iterativa Mientras -'
	Escribir ''
	Escribir 'Ingrese un número entre 1 y 10: '
	Leer numero_ingresado
	
	Si numero_ingresado < 1 O numero_ingresado > 10
		Escribir 'El número ingresado no es válido. Reintente nuevamente.'
	SiNo
		Mientras  control_ciclo <= 10
			producto <- numero_ingresado * control_ciclo
			Escribir numero_ingresado, 'x', control_ciclo, '=', producto
			control_ciclo <- control_ciclo + 1
		FinMientras
	FinSi
FinFuncion

Funcion Estructura_Iterativa_Para
	numero_ingresado <- 0
	Escribir ''
	Escribir '- Sistema de Tablas de Multiplicar | Estructura Iterativa Para -'
	Escribir ''
	Escribir 'Ingrese un número entre 1 y 10: '
	Leer numero_ingresado
	
	Si numero_ingresado < 1 O numero_ingresado > 10
		Escribir 'El número ingresado no es válido. Reintente nuevamente.'
	SiNo
		Para control_ciclo = 1 Hasta 10
			producto <- numero_ingresado * control_ciclo
			Escribir numero_ingresado, 'x', control_ciclo, '=', producto			
		FinPara
	FinSi
FinFuncion

Algoritmo ejercicio_5
	
	Estructura_Iterativa_Mientras()
	
	Estructura_Iterativa_Para()

FinAlgoritmo	