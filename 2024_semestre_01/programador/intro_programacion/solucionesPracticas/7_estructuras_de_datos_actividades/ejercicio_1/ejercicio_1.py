# Consigna 1
# Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo) no repetidas, guardarlos en una lista y mostrarlos.
print('\n'+'- Estructura de Datos - Ejercicio 1 - Consigna 1 -'+'\n')

nombres = []
for i in range(10):
    nombre = input("Ingrese un nombre: ")
    if nombre in nombres:
        print("El nombre ya fue ingresado")
    else:
        nombres.append(nombre)
print(nombres)

# Consigna 2
# Eliminar la tercer y la última persona de la lista del ejercicio 1, luego ordenar la lista y mostrarlo
print('\n'+'- Estructura de Datos - Ejercicio 1 - Consigna 2 -'+'\n')

nombres.pop(2)
nombres.pop()
nombres.sort()
print(nombres)

# Consigna 3
# Guardar en un diccionario los datos de una persona: nombre, apellido, dni, email, fecha de nacimiento.
print('\n'+'- Estructura de Datos - Ejercicio 1 - Consigna 3 -'+'\n')

persona = {
    "nombre": "Marcos",
    "apellido": "Frites",
    "dni": 34440964,
    "email": "marcosgfrites@gmail.com",
    "fecha_nacimiento": "27/05/1989",
}
print(persona)

# Consigna 4
# En un nuevo diccionario llamado familia guardar 4 personas, cada una de ellas con los mismos 5 datos (nombre, apellido, dni, email, fecha de nacimiento)
print('\n'+'- Estructura de Datos - Ejercicio 1 - Consigna 4 -'+'\n')

familia = {
    "persona_1": {
        "nombre": "Marcos",
        "apellido": "Frites",
        "dni": 34440964,
        "email": "marcosgfrites@gmail.com",
        "fecha_nacimiento": "27/05/1989",
    },
    "persona_2": {
        "nombre": "Makarena",
        "apellido": "Carmona",
        "dni": 37093873,
        "email": "makacarmona15@gmail.com",
        "fecha_nacimiento": "18/06/1993",
    },
    "persona_3": {
        "nombre": "Elizabeth",
        "apellido": "Debenedetti",
        "dni": 17177759,
        "email": "ely.lou2015@gmail.com",
        "fecha_nacimiento": "19/03/1965",
    },
    "persona_4": {
        "nombre": "Estebans",
        "apellido": "Frites",
        "dni": 13533412,
        "email": "ef.multiservice@gmail.com",
        "fecha_nacimiento": "29/11/1959",
    }
}
print(familia)

# Consigna 5 - Tuplas
# Guardar en una tupla los primeros n números pares. El valor de n que lo ingrese el usuario (input). Luego mostrar los datos de la tupla.
print('\n'+'- Estructura de Datos - Ejercicio 1 - Consigna 5: Tuplas -'+'\n')

n = int(input("Ingrese un número: "))
pares = tuple([i for i in range(1, n*2) if i % 2 == 0])
print(pares)

# Consigna 5 - Listas
# Guardar en una lista los primeros n números pares. El valor de n que lo ingrese el usuario (input). Luego mostrar los datos de la lista.
print('\n'+'- Estructura de Datos - Ejercicio 1 - Consigna 5: Listas -'+'\n')

n = int(input("Ingrese un número: "))
pares = [i for i in range(1, n*2) if i % 2 == 0]
print(pares)
