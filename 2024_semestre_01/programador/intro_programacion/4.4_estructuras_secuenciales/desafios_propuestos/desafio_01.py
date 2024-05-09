# # # Desafío 01 - Calcular el I.V.A
# Desarrollar un programa secuencial, planteando su Pseudocódigo y Diagrama de Flujo, que permita ingresar un precio,
# calcular el I.V.A. (21%) y mostrar el precio final de lista de un producto.

precio_sin_iva = float(input('Ingrese el precio del producto: $ '))

iva = precio_sin_iva * 0.21

precio_con_iva = precio_sin_iva + iva

print(f'El precio final del producto es: $ {precio_con_iva}')
