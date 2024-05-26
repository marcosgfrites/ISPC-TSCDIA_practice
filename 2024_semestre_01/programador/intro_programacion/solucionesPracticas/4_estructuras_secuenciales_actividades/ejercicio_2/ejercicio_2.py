print('- Sistema de Cálculo de Costos para Pintor -')

largo_pared = float(input('Ingrese el largo de la pared en metros: '))
alto_pared = float(input('Ingrese el alto de la pared en metros: '))
costo_metro_cuadrado = float(input('Ingrese el costo por metro cuadrado: $ '))

cantidad_metros_cuadrados = largo_pared * alto_pared
costo_total = cantidad_metros_cuadrados * costo_metro_cuadrado

print(f'El costo total de mano de obra para pintar la pared es: $ {costo_total}')
