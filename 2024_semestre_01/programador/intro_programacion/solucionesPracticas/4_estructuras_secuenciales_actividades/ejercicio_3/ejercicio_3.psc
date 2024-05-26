Algoritmo ejercicio_3
	partidos_ganados <- 0
	partidos_empatados <- 0
	partidos_perdidos <- 0
	puntos_ganados <- 0
	puntos_empatados <- 0
	puntos_totales <- 0
	
	Escribir '- Sistema de Control de Puntos de su Equipo de Fútbol -'
	Escribir ''
	
	Escribir 'Ingrese la cantidad total de partidos ganados por su quipo: '
	Leer partidos_ganados
	
	Escribir 'Ingrese la cantidad total de partidos empatados por su equipo: '
	Leer partidos_empatados
	
	Escribir 'Ingrese la cantidad total de partidos perdidos por si equipo: '
	Leer partidos_perdidos
	
	puntos_ganados <- partidos_ganados * 3
	puntos_empatados <- partidos_empatados
	puntos_totales <- puntos_ganados + puntos_empatados
	
	Escribir 'Su equipo lleva acumulados ', puntos_totales,' puntos en el campeonato.'
FinAlgoritmo