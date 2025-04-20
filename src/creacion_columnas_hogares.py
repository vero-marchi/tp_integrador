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

# ________________________________________________
# Enumeracion de columnas para resolver luego enunciados (se puede borrar una vez realizado todo el codigo)
inp = input('Deseas imprimir listado de columnas? | si - no\n')
print('')
if inp == 'si':
    for i, columna in enumerate(header):
        print(i, columna)
# ________________________________________________

#----------------------------------------------------------------------                                                 ----------------------------------------------------------------------------
#----------------------------------------------------------------------     IX_TOT : CANTIDAD DE PERSONAS EN EL HOGAR   ----------------------------------------------------------------------------
#----------------------------------------------------------------------                                                 ----------------------------------------------------------------------------

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

def agregar_columna_tipo_hogar(csv_inicial, csv_final):
    """"

    """
    with csv_inicial.open(mode='r', encoding='utf-8') as f_inicial:
        leerDic = csv.DictReader(f_inicial, delimiter = ';')
        filas = []
        
        for fila in leerDic:
            fila['TIPO_HOGAR'] = parseo_datos_cant_personas_hogar(fila.get('IX_TOT', '')) # funcion GET tiene dos parametros, devuelve 'valor x defecto' si no se encuentra IX_TOT
            filas.append(fila)


    encabezados = list(filas[0].keys())

    with csv_final.open(mode='w', encoding='utf-8', newline='') as f_final:
        escritor = csv.DictWriter(f_final, fieldnames=encabezados, delimiter=';')
        escritor.writeheader()
        escritor.writerows(filas)
        
    print(f"Archivo guardado con columna 'TIPO_HOGAR': {csv_final}")
    
#agregar_columna_tipo_hogar(archivo, archivo) → invocar en hogares.ipynb

#----------------------------------------------------------------------                                           ----------------------------------------------------------------------------
#----------------------------------------------------------------------         V4 : MATERIAL_TECHUMBRE           ----------------------------------------------------------------------------
#----------------------------------------------------------------------                                           ----------------------------------------------------------------------------

def parseo_datos_material_techo(inf):
    """"
    Clasifica la tipo de hogar segun V4:
    5 a 7: "Material precario".
    1 a 4: "Material durable".
    9: “No aplica”.
    """
    try:
        valor = int(inf)
    except:
        print('Valor inválido')
    
    if valor >= 5 and valor <= 7:
        return 'Material Precario'
    elif 1 <= valor <= 4:
        return 'Material Durable'
    elif valor == 9:
        return 'No Aplica'
    else:
        return 'Desconocido'

def agregar_columna_material_techumbre(csv_inicial, csv_final):
    """"

    """
    with csv_inicial.open(mode='r', encoding='utf-8') as f_inicial:
        leerDic = csv.DictReader(f_inicial, delimiter = ';')
        filas = []
        
        for fila in leerDic:
            fila['MATERIAL_TECHUMBRE'] = parseo_datos_material_techo(fila.get('V4', ''))
            filas.append(fila)

    encabezados = list(filas[0].keys())

    with csv_final.open(mode='w', encoding='utf-8', newline='') as f_final:
        escritor = csv.DictWriter(f_final, fieldnames=encabezados, delimiter=';')
        escritor.writeheader()
        escritor.writerows(filas)
        
    print(f"Archivo guardado con columna 'MATERIAL_TECHUMBRE': {csv_final}")

#agregar_columna_material_techumbre(archivo, archivo)

#----------------------------------------------------------------------                                           ----------------------------------------------------------------------------
#----------------------------------------------------------------------         IX_TOT, II2 : DENSIDAD_HOGAR      ----------------------------------------------------------------------------
#----------------------------------------------------------------------                                           ----------------------------------------------------------------------------

# Densidad de hogar = personas / habitaciones (IX_TOT / II2)

def parseo_datos_densidad(inf, inf2):
    """"
    Clasifica la tipo de hogar segun V4:
    5 a 7: "Material precario".
    1 a 4: "Material durable".
    9: “No aplica”.
    """
    try: 
        personas = int(inf) # IX_TOT
        habitaciones = int(inf2) # II2
        if habitaciones == 0:
            return 'Sin Dato'

        densidad = personas / habitaciones
    except:
        print('Valor inválido')
    
    if densidad < 1:
        return 'Bajo'
    elif 1 <= densidad <= 2:
        return 'Medio'
    else:
        return 'Alto'

def agregar_columna_densidad_hogar(csv_inicial, csv_final):
    """"

    """
    with csv_inicial.open(mode='r', encoding='utf-8') as f_inicial:
        leerDic = csv.DictReader(f_inicial, delimiter = ';')
        filas = []
        
        for fila in leerDic:
            # obtengo los valores en la columna ix_tot e ii2 para hacer el calculo y asignarlo a la celda de la columna creeada
            ix_tot = fila.get('IX_TOT', '')
            ii2 = fila.get('II2', '')

            fila['DENSIDAD_HOGAR'] = parseo_datos_densidad(ix_tot, ii2)
            filas.append(fila)

    encabezados = list(filas[0].keys())

    with csv_final.open(mode='w', encoding='utf-8', newline='') as f_final:
        escritor = csv.DictWriter(f_final, fieldnames=encabezados, delimiter=';')
        escritor.writeheader()
        escritor.writerows(filas)
        
    print(f"Archivo guardado con columna 'DENSIDAD_HOGAR': {csv_final}")

# agregar_columna_densidad_hogar(archivo, archivo)




























































