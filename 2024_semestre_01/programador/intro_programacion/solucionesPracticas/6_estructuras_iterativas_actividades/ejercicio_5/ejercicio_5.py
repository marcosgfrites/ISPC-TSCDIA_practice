# # # Resolución 5.1: utilizando un 'while'
print('\n' + '- Sistema de Tablas de Multiplicar | Estructura Iterativa While -' + '\n')
numero_ingresado_while = int(input("Ingrese un número entre 1 y 10: "))
if numero_ingresado_while < 1 or numero_ingresado_while > 10:
    print("El número ingresado no es válido. Reintente nuevamente.")
else:
    i = 1
    while i <= 10:
        print(f"{numero_ingresado_while}x{i}={numero_ingresado_while * i}")
        i += 1

# # # Resolución 5.2: utilizando un 'for'
print('\n' + '- Sistema de Tablas de Multiplicar | Estructura Iterativa For -' + '\n')
numero_ingresado_for = int(input("Ingrese un número entre 1 y 10: "))
if numero_ingresado_for < 1 or numero_ingresado_for > 10:
    print("El número ingresado no es válido. Reintente nuevamente")
else:
    for i in range(1, 11):
        print(f"{numero_ingresado_for}x{i}={numero_ingresado_for * i}")
