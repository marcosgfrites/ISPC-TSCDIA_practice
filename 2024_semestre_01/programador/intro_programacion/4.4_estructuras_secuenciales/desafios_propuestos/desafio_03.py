# # # Desafío 03 - Casa de Cambio
# Desarrollar un programa completo (pseudocódigo, diagrama de flujo y código en Python) que permita ingresar un monto en
# Pesos ARS y devuelva como resultado el equivalente en Dólares USD.

valor_dolar = 900.500  # valor oficial del dólar según BNA el 2024-05-08

monto_pesos = float(input('Ingrese el monto en Pesos ARS: $ '))

monto_dolares = monto_pesos / valor_dolar

print(f'El monto en Dólares USD es: U$S {monto_dolares}')
