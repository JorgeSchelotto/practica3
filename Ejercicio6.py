"""Implementar una función que reciba el nombre de un archivo en formato CSV y lo exporte
a formato JSON. Probarla con el archivo del ejercicio anterior"""

import json
import csv

def csvToJson( nombreArchivoCsv ):
	csvreader = csv.reader(open(nombreArchivoCsv, "r"))
	
	dato = []
	for fila in csvreader:
		dato.append(fila)
		
		
	json.dump(dato, open('csvToJson.txt','w'))
		
csvToJson("Todas_las_carreras.csv")

print(json.load(open('csvToJson.txt','r')))
	
