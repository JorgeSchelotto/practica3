"""Dado el archivo que detalla la cantidad de mujeres que estudian carreras tecnológicas,
recorrerlo e imprimir la cantidad total por universidad."""

import csv

csvreader = csv.reader(open("Todas_las_carreras.csv", "r"))
dic_unis = {}

for fila in csvreader:
	if fila[2] != 'Institución' and fila[10] != '':
		dic_unis[fila[2]] = 0
		#dic_unis[fila[2]] += int(fila[12])

		
	
csvreader2 = csv.reader(open("Todas_las_carreras.csv", "r"))
for fila in csvreader2:
	if fila[2] != 'Institución' and fila[10] != '':
		dic_unis[fila[2]] = int(dic_unis[fila[2]]) + int(fila[10])
#print(dic_unis[fila[12]])

for key , value in dic_unis.items():
	print('{} -- Estudiantas: {}'.format(key, value))
	print()
	
#print('\nTotal egresadas de la UNLP: {}'.format(cont))

#print(dic_unis)
