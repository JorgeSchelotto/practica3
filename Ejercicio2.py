import random

"""Realice una función que lea de teclado las coordenadas del ejercicio anterior, las guarde en el
archivo correspondiente y asocie la misma a un color aleatorio del archivo de colores. ¿Cómo
haría para almacenar la estructura completa en un archivo de texto plano? Implementarlo
teniendo en cuenta la separación de las coordenadas y los colores"""

def coordenada():
    #Creo el archivo y guardo las coordenadas.
    file = open('coordenadas2.txt', 'w')
    for i in range(5):
        coorX= input('Ingrese coordenada X')
        coorY = input('Ingrese coordenada Y')
        file.write(coorX + ', ' + coorY + '\n')
    file.close()

    #Abro los archivos y los guardo en listas
    colores = list(map(lambda str: str.replace('\n', ''), open('colores.txt', 'r').readlines()))
    coordenadas = list(map(lambda str: str.replace('\n', ''), open('coordenadas2.txt', 'r').readlines()))

    #cargo los colores como claves de un diccionario
    coloresCoordenadas = {}
    for color in colores:
        coloresCoordenadas[color] = coordenadas[random.randrange(len(coordenadas))]

    #Control
    print(coloresCoordenadas)
    print()

    #guardo la estructura en archivoColoresCoordenas.
    file2 = open('archivoColoresCoordenas.txt','w')
    for key, value in coloresCoordenadas.items():
        file2.write(key + ' : ' + value + '\n')
    file2.close()


#
coordenada()

f = open('archivoColoresCoordenas.txt','r')

for linea in f:
    print(linea)

f.close()








