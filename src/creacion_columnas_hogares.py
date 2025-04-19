import csv
from pathlib import Path

# Hay que ajustar luego Path("tp_integrador") cuando se pase a GitLab
archivo = Path("tp_integrador") / "files" / "hogares_combinados.csv"

def leerCSV(archivo):
    """"

    """
    datos = []
    
    with archivo.open(mode='r', encoding='utf-8') as f:
        csv_reader = csv.DictReader(f, delimiter=';')
        for fila in csv_reader:
            datos.append(fila)
    return datos


dataset = leerCSV(archivo)

header = dataset[0].keys()

# ---------------------------------------------------
# Enumeracion de columnas para resolver luego enunciados (se puede borrar una vez realizado todo el codigo)
inp = input('Deseas imprimir listado de columnas? | si - no\n')
print('')
if inp == 'si':
    for i, columna in enumerate(header):
        print(i, columna)
# ---------------------------------------------------

for fila in dataset: #imprime una columna
    print(fila['PONDIH'])
