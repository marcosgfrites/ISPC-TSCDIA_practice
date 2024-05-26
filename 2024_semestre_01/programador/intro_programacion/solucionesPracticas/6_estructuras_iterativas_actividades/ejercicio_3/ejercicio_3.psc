Algoritmo ejercicio_3
	nombre_ingresado <- ''
	
	Escribir '- Sistema de Repetición de Nombres -'
	Escribir ''
	
	Escribir 'Ingrese un nombre: '
	Leer nombre_ingresado
	
	Mientras nombre_ingresado <> 'fin' Y nombre_ingresado <> 'FIN' Y nombre_ingresado <> 'Fin'
		Escribir 'El nombre ingresado es: ', nombre_ingresado
		Escribir 'Ingrese un nombre: '
		Leer nombre_ingresado
	FinMientras
FinAlgoritmo