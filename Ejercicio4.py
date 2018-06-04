"""Leer un texto desde un archivo y generar uno nuevo (denominado verbos.json) que
contenga una estructura con todos los verbos convertidos a infinitivo junto con la cantidad
de apariciones de cada uno."""

from collections import Counter
from pattern.es import tag
from pattern.es import conjugate, INFINITIVE
import json

def cuentapVerbos(str):
    verbos = []
    for word, pos in tag(str):  # tag devuelve una lista de tuplas formadas por (palabra, tipo de palabra)
        if pos == "VB":
            verbos.append(conjugate(word, tense=INFINITIVE))

    count = Counter(verbos).most_common()
    print(count)
    
    json.dump(count, open('verbos.txt', 'w'))
    
    print(json.load(open('verbos.txt', 'r')))


frase = (' ').join(list(map(lambda str: str.replace('\n', ''), open('textoE4.txt', 'r').readlines())))

cuentapVerbos(frase)


