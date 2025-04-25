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


#----------------------------------------------------------------------                                          ----------------------------------------------------------------------------
#----------------------------------------------------------------------         3. CH04 : CH04_str               ----------------------------------------------------------------------------
#----------------------------------------------------------------------                                          ----------------------------------------------------------------------------

def refactorizacion_datos_CH04(inf):
    """
    Convierte el código numérico del sexo (CH04) a un categoria legible.
    Args:
        inf (str): Valor de CH04 (1 para varón, 2 para mujer).
    Returns:
        str: 'Varon', 'Mujer' o 'Error' si el valor no es válido.
    """
    if inf == '1':
        return 'Varon'
    elif inf == '2':
        return 'Mujer'
    else:
        return 'Error'

def agregar_columna_refactorizacion_datos_CH04(csv_inicial, csv_final):
    """
    Agrega al CSV una nueva columna 'CH04_str' con el sexo en formato texto.
    Args:
        csv_inicial (Path): Ruta del archivo CSV original.
        csv_final (Path): Ruta del archivo CSV destino (mismo archivo de origen).
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




#----------------------------------------------------------------------                                                 ----------------------------------------------------------------------------
#----------------------------------------------------------------------     4. NIVEL_ED : NIVEL_ED_str                          ----------------------------------------------------------------------------
#----------------------------------------------------------------------                                                 ----------------------------------------------------------------------------

def refactorizacion_datos_NIVEL_ED(inf):
    """
    Traduce el código de nivel educativo (NIVEL_ED) a su descripción textual.
    Args:
        inf (str): Código del nivel educativo.
    Returns:
        str: Descripción del nivel o 'ERROR' si el valor no es válido.
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
        return 'Error'

def agregar_columna_refactorizacion_datos_NIVEL_ED(csv_inicial, csv_final):
    """
    Agrega una columna 'NIVEL_ED_str' al CSV con el nivel educativo en texto.
    Args:
        csv_inicial (Path): Ruta del archivo CSV original.
        csv_final (Path): Ruta del archivo CSV destino (mismo archivo de origen).
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




#----------------------------------------------------------------------                                                 ----------------------------------------------------------------------------
#----------------------------------------------------------------------     5. ESTADO, CAT_OCUP : CONDICION_LABORAL                          ----------------------------------------------------------------------------
#----------------------------------------------------------------------                                                 ----------------------------------------------------------------------------

def clasificar_CONDICION_LABORAL(inf, inf2):
    """
    Clasifica la condición laboral de una persona en función de ESTADO y CAT_OCUP.
    Args:
        inf (str): Valor de la variable ESTADO.
        inf2 (str): Valor de la variable CAT_OCUP.
    Returns:
        str: Categoría laboral como texto legible o error en caso de valores inválidos.
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

def agregar_columna_clasificar_CONDICION_LABORAL(csv_inicial, csv_final):
    """
    Agrega una columna 'CONDICION_LABORAL' con la clasificación laboral de cada individuo.
    Args:
        csv_inicial (Path): Ruta del archivo CSV original.
        csv_final (Path): Ruta del archivo CSV destino (mismo archivo de origen).
    """
    with csv_inicial.open(mode='r', encoding='utf-8') as f_inicial:
        leerDic = csv.DictReader(f_inicial, delimiter = ';')
        filas = []
        
        for fila in leerDic:
            estado = fila.get('ESTADO')
            cat_ocup = fila.get('CAT_OCUP')
            
            fila['CONDICION_LABORAL'] = clasificar_CONDICION_LABORAL(estado, cat_ocup) # funcion GET tiene dos parametros, devuelve '(valor x defecto)' si no se encuentra IX_TOT
            filas.append(fila)

    encabezados = list(filas[0].keys()) # Lista con los encabezados del archivo CSV + nuevo encabezado generado

    with csv_final.open(mode='w', encoding='utf-8', newline='') as f_final:
        escritor = csv.DictWriter(f_final, fieldnames=encabezados, delimiter=';')
        escritor.writeheader()
        escritor.writerows(filas)

    print(f"Archivo guardado con columna 'CONDICION_LABORAL': {csv_final}")




#----------------------------------------------------------------------                                                 ----------------------------------------------------------------------------
#----------------------------------------------------------------------     6. UNIVERSITARIO : CH06, NIVEL_ED_str                          ----------------------------------------------------------------------------
#----------------------------------------------------------------------                                                 ----------------------------------------------------------------------------

def clasificar_UNIVERSITARIO(inf, inf2):
    """
    Determina si una persona mayor de 18 años tiene formación universitaria.
    Args:
        inf (str): Edad (CH06).
        inf2 (str): Nivel educativo como texto (NIVEL_ED_str).
    Returns:
        str: 'Si', 'No' o 'No Aplica', según la condición.
    """
    try:
        edad = int(inf)
        nivel_educativo = inf2

        if edad >= 18 and nivel_educativo == 'Superior o universitario':
            return 'Si'
        elif edad >= 18 and nivel_educativo in [
            'Primario incompleto', 'Primario completo', 'Secundario incompleto', 'Secundario completo'
            ]:
            return 'No'
        else:
            return 'No Aplica'
    except:
        return 'Error de conversion, var: edad'

def agregar_columna_clasificar_UNIVERSITARIO(csv_inicial, csv_final):
    """
    Agrega una columna 'UNIVERSITARIO' con la clasificación según edad y educación.
    Args:
        csv_inicial (Path): Ruta del archivo CSV original.
        csv_final (Path): Ruta del archivo CSV destino (mismo archivo de origen).
    """
    with csv_inicial.open(mode='r', encoding='utf-8') as f_inicial:
        leerDic = csv.DictReader(f_inicial, delimiter = ';')
        filas = []
        
        for fila in leerDic:
            edad = fila.get('CH06')
            nivel_educativo = fila.get('NIVEL_ED_str')
            
            fila['UNIVERSITARIO'] = clasificar_UNIVERSITARIO(edad, nivel_educativo) # funcion GET tiene dos parametros, devuelve '(valor x defecto)' si no se encuentra IX_TOT
            filas.append(fila)

    encabezados = list(filas[0].keys()) # Lista con los encabezados del archivo CSV + nuevo encabezado generado

    with csv_final.open(mode='w', encoding='utf-8', newline='') as f_final:
        escritor = csv.DictWriter(f_final, fieldnames=encabezados, delimiter=';')
        escritor.writeheader()
        escritor.writerows(filas)

    print(f"Archivo guardado con columna 'UNIVERSITARIO': {csv_final}")


# 3. 
print('___________________Punto 3___________________')
agregar_columna_refactorizacion_datos_CH04(archivo, archivo)

# 4. 
print('___________________Punto 4___________________')
agregar_columna_refactorizacion_datos_NIVEL_ED(archivo, archivo)

# 5.
print('___________________Punto 5___________________')
agregar_columna_clasificar_CONDICION_LABORAL(archivo, archivo)

# 6.
print('___________________Punto 6___________________')
agregar_columna_clasificar_UNIVERSITARIO(archivo, archivo)