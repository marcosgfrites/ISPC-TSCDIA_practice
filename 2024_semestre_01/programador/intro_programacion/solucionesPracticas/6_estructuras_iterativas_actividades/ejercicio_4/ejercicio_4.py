print('- Sistema de Control de Rendimiento Escolar -')

suma_notas = 0.0
promedio = 0.0
rendimiento = ""

cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))

for i in range(cantidad_alumnos):
    nota = float(input(f"Ingrese la nota del alumno {i + 1}: "))
    suma_notas += nota

promedio = suma_notas / cantidad_alumnos

if promedio > 8:
    rendimiento = "elevado"
elif promedio >= 6:
    rendimiento = "aceptable"
else:
    rendimiento = "bajo"

print(f"El promedio de las notas es: {promedio} lo que marca un rendimiento {rendimiento}.")
