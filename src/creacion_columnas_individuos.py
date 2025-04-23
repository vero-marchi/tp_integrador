import csv
from pathlib import Path

# ¿¿ Hay que ajustar luego el Path("tp_integrador") cuando se pase a GitLab ??
archivo = Path("tp_integrador") / "files" / "individuos_combinados.csv"

def leerCSV(archivo):
    """
    Lee un archivo CSV delimitado por punto y coma y devuelve su contenido como lista de diccionarios.
    Args:
        archivo (Path): Ruta al archivo CSV a leer.
    Returns:
        list: Lista de diccionarios, donde cada uno representa una fila del CSV.
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
#----------------------------------------------------------------------     3. CH04 : CH04_str                          ----------------------------------------------------------------------------
#----------------------------------------------------------------------                                                 ----------------------------------------------------------------------------

def refactorizacion_datos_CH04(inf):
    """

    """
    if inf == '1':
        return 'Varon'
    elif inf == '2':
        return 'Mujer'
    else:
        return 'Error'

def agregar_columna_refactorizacion_datos_ch4(csv_inicial, csv_final):
    """

    """
    with csv_inicial.open(mode='r', encoding='utf-8') as f_inicial:
        leerDic = csv.DictReader(f_inicial, delimiter = ';')
        filas = []
        
        for fila in leerDic:
            fila['CH04_str'] = refactorizacion_datos_CH04(fila.get('CH04', '')) # funcion GET tiene dos parametros, devuelve '(valor x defecto)' si no se encuentra IX_TOT
            filas.append(fila)

    encabezados = list(filas[0].keys()) # Lista con los encabezados del archivo CSV + nuevo encabezado generado

    with csv_final.open(mode='w', encoding='utf-8', newline='') as f_final:
        escritor = csv.DictWriter(f_final, fieldnames=encabezados, delimiter=';')
        escritor.writeheader()
        escritor.writerows(filas)

    print(f"Archivo guardado con columna 'CH04_str': {csv_final}")

# agregar_columna_refactorizacion_datos_ch4(archivo, archivo)


#----------------------------------------------------------------------                                                 ----------------------------------------------------------------------------
#----------------------------------------------------------------------     4. NIVEL_ED : NIVEL_ED_str                          ----------------------------------------------------------------------------
#----------------------------------------------------------------------                                                 ----------------------------------------------------------------------------

def refactorizacion_datos_NIVEL_ED(inf):
    """

    """
    if inf == '1':
        return 'Primario incompleto'
    elif inf == '2':
        return 'Primario completo'
    elif inf == '3':
        return 'Secundario incompleto'
    elif inf == '4':
        return 'Secundario completo'
    elif inf == '5' or inf == '6':
        return 'Superior o universitario'
    elif inf == '7' or inf == '9':
        return 'Sin informacion'
    else:
        return 'ERROR'

def agregar_columna_refactorizacion_datos_NIVEL_ED(csv_inicial, csv_final):
    """

    """
    with csv_inicial.open(mode='r', encoding='utf-8') as f_inicial:
        leerDic = csv.DictReader(f_inicial, delimiter = ';')
        filas = []
        
        for fila in leerDic:
            fila['NIVEL_ED_str'] = refactorizacion_datos_NIVEL_ED(fila.get('NIVEL_ED', '')) # funcion GET tiene dos parametros, devuelve '(valor x defecto)' si no se encuentra IX_TOT
            filas.append(fila)

    encabezados = list(filas[0].keys()) # Lista con los encabezados del archivo CSV + nuevo encabezado generado

    with csv_final.open(mode='w', encoding='utf-8', newline='') as f_final:
        escritor = csv.DictWriter(f_final, fieldnames=encabezados, delimiter=';')
        escritor.writeheader()
        escritor.writerows(filas)

    print(f"Archivo guardado con columna 'NIVEL_ED_str': {csv_final}")

#agregar_columna_refactorizacion_datos_NIVEL_ED(archivo, archivo)


#----------------------------------------------------------------------                                                 ----------------------------------------------------------------------------
#----------------------------------------------------------------------     5. ESTADO, CAT_OCUP : CONDICION_LABORAL                          ----------------------------------------------------------------------------
#----------------------------------------------------------------------                                                 ----------------------------------------------------------------------------

def clasificar_condicion_laboral(inf, inf2):
    """

    """
    try:
        estado = int(inf)
        cat_ocup = int(inf2)

        if estado == 1:
            # Tipos de Ocupado
            if cat_ocup in (1, 2): 
                return 'Ocupado autonomo'
            elif cat_ocup in (3, 4, 9): 
                return 'Ocupado dependiente'
            else:
                return 'Ocupado no categorizado' # Por si hay algun valor distinto a los indicados en el censo

        elif estado == 2:
            return 'Desocupado'

        elif estado == 3:
            return 'Inactivo'

        elif estado == 4:
            return 'Fuera de categoría/sin informacion'

        else:
            return 'Error de estado'

    except:
        return 'Error de conversion'

def agregar_columna_clasificar_condicion_laboral(csv_inicial, csv_final):
    """

    """
    with csv_inicial.open(mode='r', encoding='utf-8') as f_inicial:
        leerDic = csv.DictReader(f_inicial, delimiter = ';')
        filas = []
        
        for fila in leerDic:
            estado = fila.get('ESTADO')
            cat_ocup = fila.get('CAT_OCUP')
            
            fila['CONDICION_LABORAL'] = clasificar_condicion_laboral(estado, cat_ocup) # funcion GET tiene dos parametros, devuelve '(valor x defecto)' si no se encuentra IX_TOT
            filas.append(fila)

    encabezados = list(filas[0].keys()) # Lista con los encabezados del archivo CSV + nuevo encabezado generado

    with csv_final.open(mode='w', encoding='utf-8', newline='') as f_final:
        escritor = csv.DictWriter(f_final, fieldnames=encabezados, delimiter=';')
        escritor.writeheader()
        escritor.writerows(filas)

    print(f"Archivo guardado con columna 'CONDICION_LABORAL': {csv_final}")

agregar_columna_clasificar_condicion_laboral(archivo, archivo)