print('- Sistema de Cobro de Lácteos en Despensa -')

valor_leche = 1000
descuento_mas_12_menos_24 = 0.10
descuento_mas_24 = 0.15
descuento_jubilado = 0.10

cantidad_leches = int(input("Ingrese la cantidad de leche que desea comprar: "))
print("El cliente es jubilado?")
print("1- SI")
print("2- NO")
es_jubilado = int(input("Ingrese el número de la respuesta: "))

if cantidad_leches < 12:
    total = cantidad_leches * valor_leche
elif 12 <= cantidad_leches <= 24:
    total = cantidad_leches * valor_leche * (1 - descuento_mas_12_menos_24)
else:
    total = cantidad_leches * valor_leche * (1 - descuento_mas_24)

if es_jubilado == 1:
    total = total * (1 - descuento_jubilado)

print(f"El total a pagar es: $ {total}")
