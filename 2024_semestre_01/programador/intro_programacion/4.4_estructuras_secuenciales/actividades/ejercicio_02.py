# # # Ejercicio 2
# Un puntor de casas debe hacer un presupuesto para un cliente.
# Lo que cobra se calcula de acuerdo a los metros cuadrados que debe pintar.
# El cliente le indica que necesita conocer el costo de mano de obra para pintar una pared rectangular de un galpón.
# El pintor cobra un monto fijo por cada metro cuadrado.
# Puedes hacer un algoritmo para calcular el costo de mano de obra para pintar la pared.

largo_pared = float(input('Ingrese el largo de la pared en metros: '))
alto_pared = float(input('Ingrese el alto de la pared en metros: '))
costo_metro_cuadrado = float(input('Ingrese el costo por metro cuadrado: $ '))

metros_cuadrados = largo_pared * alto_pared
costo_total = metros_cuadrados * costo_metro_cuadrado

print(f'El costo total de mano de obra para pintar la pared es: $ {costo_total}')
