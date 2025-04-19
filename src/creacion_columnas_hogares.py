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

columna_ix_tot = [fila["IX_TOT"] for fila in dataset] #list comprehension - IX TOT indica la cantidad de personas en el hogar

def parseo_datos_cant_personas_hogar(inf):
    """"
    Clasifica la cantidad de personas en un hogar según IX_TOT:
    1  → 'Unipersonal'
    2-4 → 'Nuclear'
    5+ → 'Extendido'
    """
    try:
        valor = int(inf)
    except:
        print('Valor inválido')
    
    if valor == 1:
        return 'Unipersonal'
    elif 2 <= valor <= 4:
        return 'Nuclear'
    elif valor >= 5:
        return 'Extendido'
    else:
        return 'Desconocido'

def agregar_columna(csv_inicial, csv_final):
    with csv_inicial.open(mode='r', encoding='utf-8') as f_inicial:
        leerDic = csv.DictReader(f_inicial, delimiter = ';')
        filas = []
        
        for fila in leerDic:
            fila['TIPO_HOGAR'] = parseo_datos_cant_personas_hogar(fila.get('IX_TOT', ''))
            filas.append(fila)


    encabezados = list(filas[0].keys())

    with csv_final.open(mode='w', encoding='utf-8', newline='') as f_final:
        escritor = csv.DictWriter(f_final, fieldnames=encabezados, delimiter=';')
        escritor.writeheader()
        escritor.writerows(filas)
        
    print(f"Archivo guardado con columna 'TIPO_HOGAR': {csv_final}")
    
agregar_columna(archivo, archivo)
