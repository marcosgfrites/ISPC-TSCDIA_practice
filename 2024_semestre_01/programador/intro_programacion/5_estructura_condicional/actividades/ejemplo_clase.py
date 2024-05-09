# # # Ejemplo Comentado en Clases
# Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos la unidad.
# Si el cliente compra más de 12 unidades (y hasta 24 unidades), el costo tiene un descuento del 10%.
# Si compra más de 24 unidades, el descuento es del 15%.
# Además posee la promoción a los jubilados.
# La promoción de jubilados es sumarle un 10% de descuento (si posee otros descuentos, se suma los descuentos).
# Desarrolle una solución algorítmica para saber cuento debe pagar el cliente.

valor_leche = 1000
descuento_mas_12_menos_24 = 0.10
descuento_mas_24 = 0.15
descuento_jubilados = 0.10

cantidad_leche = int(input("Ingrese la cantidad de leche que desea comprar: "))
es_jubilado = input("El cliente es jubilado? (si/no): ")

if cantidad_leche < 12:
    total = cantidad_leche * valor_leche
elif 12 <= cantidad_leche <= 24:
    total = cantidad_leche * valor_leche * (1 - descuento_mas_12_menos_24)
else:
    total = cantidad_leche * valor_leche * (1 - descuento_mas_24)

if es_jubilado == "si":
    total = total * (1 - descuento_jubilados)

print(f"El total a pagar es: $ {total}")
