print('- Sistema de Cálculo de Precio de Lista -')

precio_sin_iva = float(input('Ingrese el precio del producto sin IVA: $ '))

valor_iva = precio_sin_iva * 0.21

precio_con_iva = precio_sin_iva + valor_iva

print(f'El precio final del producto es: $ {precio_con_iva}')
