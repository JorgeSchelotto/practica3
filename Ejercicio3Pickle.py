import pickle
"""Registrar los jugadores del Ejercicio 7 de la Práctica 1 en un archivo utilizando cualquiera de
las librerías dadas en la teoría (Pickle, JSON, CSV). Implementar una función denominada
modificoDatos, la cual solicita por teclado los datos de un jugador, si este existe en el
archivo, modifica dichos datos en el mismo. Si no existe el jugador, lo agrega."""

jugadores = {}
stats = {}

jugador = input('Ingrese Nombre del jugador. Ingrese cancelar para cortar la carga: ')

while(jugador != 'cancelar'):
    nivel = input('Ingrese Nivel del jugador: ')
    puntaje = int(input('Ingrese puntaje del jugador: '))
    horasJuego = input('Ingrese horas de juego del jugador: ')

    stats['nivel'] = nivel
    stats['puntaje'] = puntaje
    stats['horas'] = horasJuego
    jugadores[jugador] = stats

    jugador = input('Ingrese Nombre del jugador: ')



pickle.dump(jugadores,open('pickle.p', 'wb'))


file2 = pickle.load(open('pickle.p', 'rb'))

print(file2)
