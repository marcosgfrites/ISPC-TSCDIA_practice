print ('- Sistema de Conversión ARS a USD -')

valor_dolar = 909.500  # valor oficial del dólar según BNA el 2024-05-25

monto_pesos = float(input('Ingrese el monto en Pesos ARS: $ '))

monto_dolares = monto_pesos / valor_dolar

print(f'El monto en Dólares USD es: U$S {monto_dolares}')
