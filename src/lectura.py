from pathlib import Path
import csv

def leer_archivos(carpeta):
    """"
    Lee los dataset .txt y devuelve sus registros.
    
    Args: 
        carpeta (str): ruta a la carpeta que contiene los dataset.
    Returns:
        list: lista de diccionarios con los registros.
    """
    carpeta = Path(carpeta)
    datos = []
    
    for archivo in carpeta.glob("*.txt"):
        with archivo.open(mode= 'r', encoding= 'utf-8') as f:
            csv_reader = csv.DictReader(f, delimiter = ';')
            for fila in csv_reader:
                datos.append(fila)
    
    return datos


def guardar_dataset(dataset, csv_combinado):
    """"
    guardar un dataset combinado en un csv
    
    Args:
        dataset (list): lista de diccionarios.
        csv_combinado (str): ruta donde se guardó el archivo.
    """
    
    with open(csv_combinado, mode='w', encoding='utf-8', newline='') as f: # NewLine se usa para solventar el salto de linea al guardar el dataset combinado
        writer = csv.DictWriter(f, fieldnames=dataset[0].keys(), delimiter=';') #usa las claves del primer registro como encabezado
        writer.writeheader()
        writer.writerows(dataset)