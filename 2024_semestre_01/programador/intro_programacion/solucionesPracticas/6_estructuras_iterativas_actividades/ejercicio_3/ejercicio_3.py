print('- Sistema de Repetición de Nombres -')

nombre = input("Ingrese un nombre: ")

while nombre != "fin" and nombre != "FIN" and nombre != "Fin":
    print(f"El nombre ingresado es: {nombre}.")
    nombre = input("Ingrese un nombre: ")
