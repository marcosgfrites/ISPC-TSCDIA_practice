Algoritmo ejercicio_clase
	valor_leche <- 1000.00
	descuento_mas_12_menos_24 <- 0.10
	descuento_mas_24 <- 0.15
	descuento_jubilado <- 0.10
	total <- 0.00
	
	Escribir '- Sistema de Cobro de Lácteos en Despensa -'
	Escribir ''
	
	Escribir 'Ingrese la cantidad de leche que desea comprar: '
	Leer cantidad_leches
	
	Escribir 'El cliente es jubilado?'
	Escribir '1- SI'
	Escribir '2- NO'
	Escribir 'Ingrese el número de la respuesta: '
	Leer es_jubilado
	
	Si cantidad_leches < 12 Entonces
		total <- cantidad_leches * valor_leche
	SiNo
		Si cantidad_leches >= 12 Y cantidad_leches <= 24
			total <- cantidad_leches * valor_leche * (1 - descuento_mas_12_menos_24)
		SiNo
			total <- cantidad_leches * valor_leche * (1 - descuento_mas_24)			
		FinSi
	FinSi
	
	Si es_jubilado = 1
		total <- total * (1 - descuento_jubilado)
	FinSi
	
	Escribir 'El total a pagar es: $ ', total
FinAlgoritmo	