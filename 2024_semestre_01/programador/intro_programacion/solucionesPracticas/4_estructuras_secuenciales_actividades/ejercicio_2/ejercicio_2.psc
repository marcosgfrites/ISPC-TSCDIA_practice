Algoritmo ejercicio_2
	largo_pared <- 0.0
	alto_pared <- 0.0
	costo_metro_cuadrado <- 0.0
	
	Escribir '- Sistema de Cálculo de Costos para Pintor -'
	Escribir ''
	
	Escribir 'Ingrese el largo de la pared en metros: '
	Leer largo_pared
	
	Escribir 'Ingrese el alto de la pared en metros: '
	Leer alto_pared
	
	Escribir 'Ingrese el costo por metro cuadrado: $ '
	Leer costo_metro_cuadrado
	
	cantidad_metros_cuadrados <- largo_pared * alto_pared
	costo_total <- cantidad_metros_cuadrados * costo_metro_cuadrado
	
	Escribir 'El costo total de mano de obra para pintar la pared es: $ ', costo_total	
FinAlgoritmo	