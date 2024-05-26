Algoritmo desafio_3
	valor_dolar <- 909.500 // valor oficial del dólar según BNA el 2024-05-25
	monto_pesos <- 0.0
	monto_dolares <- 0.0
	
	Escribir '- Sistema de Conversión ARS a USD -'
	Escribir ''
	
	Escribir 'Ingrese el monto en Pesos ARS: $ '
	Leer monto_pesos
	
	monto_dolares <- monto_pesos/valor_dolar
	
	Escribir 'El monto en Dólares USD es: U$S ', monto_dolares
FinAlgoritmo