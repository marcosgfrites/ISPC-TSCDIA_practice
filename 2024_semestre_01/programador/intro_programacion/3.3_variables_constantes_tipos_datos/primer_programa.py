# # # Ej. de demostración de la función print
PI = 3.14159265359

print(PI)

radio = 5

area_circunferencia = PI * radio ** 2  # ** es el operador de potencia

print(area_circunferencia)
print("El área de la circungerencia es: ", area_circunferencia)

# # # Ej. de interacción con el usuario - input de texto
nombre = input("¿Cómo te llamas? ")

print(f'Hola {nombre}, ¿cómo estás?')

# # # Ej. de interacción con el usuario - input de números
numero1 = int(input("Dame un primer número: "))  # int() convierte el texto a un número entero
numero2 = int(input("Dame un segundo número: "))  # si no agrego int() el input se toma como texto
numero3 = int(input("Dame un tercer número: "))

suma = numero1 + numero2 + numero3  # si el input es texto, la suma será una concatenación

promedio = suma / 3

print("La suma de los números es: ", suma)
print("El promedio de los números es: ", promedio)

