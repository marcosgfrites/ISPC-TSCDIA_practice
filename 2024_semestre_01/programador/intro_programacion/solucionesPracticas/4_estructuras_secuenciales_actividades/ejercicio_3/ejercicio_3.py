print('- Sistema de Control de Puntos de su Equipo de Fútbol -')

partidos_ganados = int(input('Ingrese la cantidad total de partidos ganados por su equipo: '))
partidos_empatados = int(input('Ingrese la cantidad total de partidos empatados por su equipo: '))
partidos_perdidos = int(input('Ingrese la cantidad total de partidos perdidos por su equipo: '))

puntos_ganados = partidos_ganados * 3
puntos_empatados = partidos_empatados

puntos_totales = puntos_ganados + puntos_empatados

print(f'Su equipo lleva acumulados {puntos_totales} puntos en el campeonato.')
