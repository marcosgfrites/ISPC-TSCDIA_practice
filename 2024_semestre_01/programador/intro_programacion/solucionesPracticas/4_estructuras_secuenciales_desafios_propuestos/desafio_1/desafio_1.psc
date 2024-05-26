Algoritmo desafio_1
	precio_sin_iva <- 0.0
	valor_iva <- 0.0
	precio_con_iva <- 0.0
	
	Escribir '- Sistema de Cálculo de Precio de Lista -'
	Escribir ''
	
	Escribir 'Ingrese el precio del producto sin IVA: $ '
	Leer precio_sin_iva
	
	valor_iva <- precio_sin_iva * 0.21
	precio_con_iva <- precio_sin_iva + valor_iva		
	
	Escribir 'El precio final del producto es: $ ', precio_con_iva
FinAlgoritmo