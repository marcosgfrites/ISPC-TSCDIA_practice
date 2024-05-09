# # # Desafío 02 - Calcular el I.V.A (Versión 2.0)
# Desarrollar un programa secuencial, planteando su Pseudocódigo y Diagrama de Flujo, que permita ingresar un precio,
# ingresar el porcentaje de I.V.A., calcular el I.V.A. según el porcentaje ingresado y mostrar el precio final de
# lista de un producto.

precio_sin_iva = float(input('Ingrese el precio del producto: $ '))

porcentaje_iva = float(input('Ingrese el porcentaje de I.V.A.: % ')) / 100

iva = precio_sin_iva * porcentaje_iva

precio_con_iva = precio_sin_iva + iva

print(f'El precio final del producto es: $ {precio_con_iva}')
