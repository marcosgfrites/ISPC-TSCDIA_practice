print('- Sistema de Cálculo de Precio de Lista (Versión 2.0) -')

precio_sin_iva = float(input('Ingrese el precio del producto sin IVA: $ '))

porcentaje_iva = float(input('Ingrese el porcentaje de IVA: % ')) / 100

valor_iva = precio_sin_iva * porcentaje_iva

precio_con_iva = precio_sin_iva + valor_iva

print(f'El precio final del producto es: $ {precio_con_iva}')
