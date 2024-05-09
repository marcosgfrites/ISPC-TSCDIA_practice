# # # Ejercicio 3
# Un hincha de fúlbol desea conocer la cantidad de puntos que su equipo lleva acumulados en el campeonato, para ello
# recibe cada semana la información de la cantidad total de partidos, desde el inicio del campeonato, que el equipo
# ha perdido, ha empatado y ha ganado. Por cada partido empatado recibe un punto, por cada partido ganado recibe tres
# puntos y por cada partido perdido recibe cero puntos.

print('Control de puntos de su equipo de fútbol')

partidos_ganados = int(input('Ingrese la cantidad total de partidos ganados por su equipo: '))
partidos_empatados = int(input('Ingrese la cantidad total de partidos empatados por su equipo: '))
partidos_perdidos = int(input('Ingrese la cantidad total de partidos perdidos por su equipo: '))

puntos_ganados = partidos_ganados * 3
puntos_empatados = partidos_empatados

puntos_totales = puntos_ganados + puntos_empatados

print(f'Su equipo lleva acumulados {puntos_totales} puntos en el campeonato.')
