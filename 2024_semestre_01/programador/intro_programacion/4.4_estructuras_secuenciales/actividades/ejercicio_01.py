# # # Ejercicio 1
# Un estudiante está cursando 5 materias, tiene la nota de cada materia y quiere saber cuál es su promedio.

nota_materia_1 = float(input('Ingrese la nota de la materia 1: '))
nota_materia_2 = float(input('Ingrese la nota de la materia 2: '))
nota_materia_3 = float(input('Ingrese la nota de la materia 3: '))
nota_materia_4 = float(input('Ingrese la nota de la materia 4: '))
nota_materia_5 = float(input('Ingrese la nota de la materia 5: '))

promedio = (nota_materia_1 + nota_materia_2 + nota_materia_3 + nota_materia_4 + nota_materia_5) / 5

print(f'El promedio de las 5 materias es: {promedio}')
