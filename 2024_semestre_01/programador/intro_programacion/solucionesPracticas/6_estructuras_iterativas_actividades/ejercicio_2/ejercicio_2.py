print('- Sistema de Muestra de Números Pares -')

numero = int(input("Ingrese un número: "))

for i in range(numero + 1):
    if i % 2 == 0:
        print(i)
