# # # Consigna 03
# Pedir que el usuario ingrese (input) nombre de personas y mostrarlos hasta que el valor de lo que ingresa sea fin.

nombre = input("Ingrese un nombre: ")

while nombre != "fin" and nombre != "FIN" and nombre != "Fin":
    print(f"El nombre ingresado es: {nombre}.")
    nombre = input("Ingrese un nombre: ")
