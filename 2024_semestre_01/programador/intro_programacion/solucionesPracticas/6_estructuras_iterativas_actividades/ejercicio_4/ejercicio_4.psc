Algoritmo ejercicio_4
	suma_notas <- 0.0
	promedio <- 0.0
	cantidad_alumnos <- 0
	rendimiento <- ''
	control_ciclo <- 0
	
	Escribir '- Sistema de Control de Rendimiento Escolar -'
	Escribir ''
	
	Escribir 'Ingrese la cantidad de alumnos: '
	Leer cantidad_alumnos
	
	Repetir
		Escribir 'Ingrese la nota del alumno ', control_ciclo + 1, ': '
		Leer nota
		suma_notas <- suma_notas + nota
		control_ciclo <- control_ciclo + 1
	Hasta Que control_ciclo = cantidad_alumnos
	
	promedio = suma_notas / cantidad_alumnos
	
	Si promedio > 8 Entonces
		rendimiento <- 'elevado'
	SiNo
		Si promedio >= 6 Entonces
			rendimiento <- 'aceptable'
		SiNo
			rendimiento <- 'bajo'			
		FinSi
	FinSi
	
	Escribir 'El promedio de las notas es: ', promedio, ' lo que marca un rendimiento ', rendimiento, '.'
FinAlgoritmo