Algoritmo desafio_3
	valor_dolar <- 909.500 // valor oficial del d�lar seg�n BNA el 2024-05-25
	monto_pesos <- 0.0
	monto_dolares <- 0.0
	
	Escribir '- Sistema de Conversi�n ARS a USD -'
	Escribir ''
	
	Escribir 'Ingrese el monto en Pesos ARS: $ '
	Leer monto_pesos
	
	monto_dolares <- monto_pesos/valor_dolar
	
	Escribir 'El monto en D�lares USD es: U$S ', monto_dolares
FinAlgoritmo