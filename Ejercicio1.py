"""Generar la misma estructura del Ejercicio 1 de la Práctica 2 pero ahora teniendo en cuenta
que las coordenadas y los colores se encuentran en 2 archivos diferentes de texto plano donde
cada elemento se encuentra en una línea. Luego imprima los elementos de la estructura
alineados a la derecha de la pantalla."""

colores = list(map(lambda str: str.replace('\n', ''), open('colores.txt', 'r').readlines()))
coordenadas = list(map(lambda str: str.replace('\n', ''), open('coordenadas.txt', 'r').readlines()))

estructura = {}

for key in coordenadas:
    estructura[key] = []
i = 0
for key in estructura:
    estructura[key] = colores[i]
    i += 1

print(estructura)
