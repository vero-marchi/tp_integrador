import csv
from pathlib import Path

# ¿¿ Hay que ajustar luego el Path("tp_integrador") cuando se pase a GitLab ??
archivo = Path("tp_integrador") / "files" / "hogares_combinados.csv"

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


#----------------------------------------------------------------------                                                 ----------------------------------------------------------------------------
#----------------------------------------------------------------------     7. IX_TOT : CANTIDAD DE PERSONAS EN EL HOGAR   ----------------------------------------------------------------------------
#----------------------------------------------------------------------                                                 ----------------------------------------------------------------------------

def parseo_datos_cant_personas_hogar(inf):
    """
    Clasifica el hogar según la cantidad de personas (columna IX_TOT).
    Args:
        inf (str): Valor de la columna IX_TOT (número de personas en el hogar).
    Returns:
        str: Categoría del hogar: 'Unipersonal', 'Nuclear', 'Extendido' o 'Desconocido'.
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
    """
    Agrega una columna 'TIPO_HOGAR' al archivo CSV, clasificada según la cantidad de personas (IX_TOT).
    Args:
        csv_inicial (Path): Ruta del archivo CSV original.
        csv_final (Path): Ruta del archivo CSV destino (mismo archivo de origen).
    """
    with csv_inicial.open(mode='r', encoding='utf-8') as f_inicial:
        leerDic = csv.DictReader(f_inicial, delimiter = ';')
        filas = []
        
        for fila in leerDic:
            fila['TIPO_HOGAR'] = parseo_datos_cant_personas_hogar(fila.get('IX_TOT', '')) # funcion GET tiene dos parametros, devuelve '(valor x defecto)' si no se encuentra IX_TOT
            filas.append(fila)

    encabezados = list(filas[0].keys()) # Lista con los encabezados del archivo CSV + nuevo encabezado generado

    with csv_final.open(mode='w', encoding='utf-8', newline='') as f_final:
        escritor = csv.DictWriter(f_final, fieldnames=encabezados, delimiter=';')
        escritor.writeheader()
        escritor.writerows(filas)

    print(f"Archivo guardado con columna 'TIPO_HOGAR': {csv_final}")


#----------------------------------------------------------------------                                           ----------------------------------------------------------------------------
#----------------------------------------------------------------------         8. V4 : MATERIAL_TECHUMBRE           ----------------------------------------------------------------------------
#----------------------------------------------------------------------                                           ----------------------------------------------------------------------------

def parseo_datos_material_techo(inf):
    """
    Clasifica el material de la techumbre según el valor de la columna V4.
    Args:
        inf (str): Valor de la columna V4.
    Returns:
        str: 'Material Durable', 'Material Precario', 'No Aplica' o 'Desconocido'.
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
    """
    Agrega la columna 'MATERIAL_TECHUMBRE' al archivo CSV, basada en la clasificación de V4.
    Args:
        csv_inicial (Path): Ruta del archivo CSV original.
        csv_final (Path): Ruta del archivo CSV destino (mismo archivo de origen).
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


#----------------------------------------------------------------------                                           ----------------------------------------------------------------------------
#----------------------------------------------------------------------        9. IX_TOT, II2 : DENSIDAD_HOGAR      ----------------------------------------------------------------------------
#----------------------------------------------------------------------                                           ----------------------------------------------------------------------------

# Densidad de hogar = personas / habitaciones (IX_TOT / II2)

def parseo_datos_densidad(inf, inf2):
    """
    Clasifica la densidad del hogar en base a la cantidad de personas (IX_TOT) y habitaciones (II2).
    Args:
        inf (str): Valor de la columna IX_TOT (personas).
        inf2 (str): Valor de la columna II2 (habitaciones para dormir).
    Returns:
        str: 'Bajo', 'Medio', 'Alto' o 'Sin Dato' (en caso de no tener habitaciones).
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



# ¿ PREGUNTA: Deberia ser 'Bajo' ? ¿o no conviene asumirlo ? ↑



def agregar_columna_densidad_hogar(csv_inicial, csv_final):
    """
    Agrega una columna 'DENSIDAD_HOGAR' al archivo CSV, calculada como IX_TOT / II2.
    Args:
        csv_inicial (Path): Ruta del archivo CSV original.
        csv_final (Path): Ruta del archivo CSV destino (mismo archivo de origen).
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



#----------------------------------------------------------------------                                               ----------------------------------------------------------------------------
#----------------------------------------------------------------------           10. CLASIFICACIONES                   ----------------------------------------------------------------------------
#----------------------------------------------------------------------                                               ----------------------------------------------------------------------------


def clasificar_habitabilidad(fila):
    """
    Clasifica la condición de habitabilidad de una vivienda según múltiples variables (agua, banio, desague, techo, piso, origen de agua, ubicacion de banio.).
    Args:
        fila (dict): Fila del CSV como diccionario, con todas las variables necesarias.
    Returns:
        str: Clasificación de habitabilidad: 'Insuficiente', 'Regular', 'Saludables', 'Buena'.
    """
    try:
        tiene_agua = int(fila.get("IV6", "")) in [1, 2]         # TRUE si tiene agua dentro o en el terreno
        origen_agua = int(fila.get("IV7", ""))                  # 1 = red pública
        tiene_banio = int(fila.get("IV8", "")) == 1             # TRUE si tiene baño
        ubic_banio = int(fila.get("IV9", ""))                   # 1 = dentro, 2 = terreno, 3 = fuera
        tipo_banio = int(fila.get("IV10", ""))                  # 3 = letrina
        desague = int(fila.get("IV11", ""))                     # 4 = hoyo o excavacion de tierra
        piso = int(fila.get("IV3", ""))                         # 1 = bueno, 2 = aceptable, 3 = precario
        techo = fila.get("MATERIAL_TECHO", "")                 # durable o precario (calculado previamente)
    except:
        return "Insuficiente"  # Por si hay algun error en el parseo

    # Insuficiente
    if (
        not tiene_agua or                  # no tiene agua
        not tiene_banio or                 # no tiene baño
        desague == 4 or                    # desagüe a hoyo
        piso == 3 or                       # piso de tierra o ladrillo suelto
        tipo_banio == 3 or                 # letrina
        techo == "Material precario"       # techo deficiente
    ):
        return "Insuficiente"

    # Regular
    if (
        ubic_banio == 3 or                 # baño fuera del terreno
        desague == 3 or                    # pozo ciego sin cámara
        piso == 2 or                       # piso aceptable, pero no bueno
        (techo == "Material durable" and tipo_banio == 2)  # buen techo pero baño sin descarga
    ):
        return "Regular"

    # Saludables: 
    if (
        tiene_agua and tiene_banio and
        techo == "Material durable" and
        ubic_banio in [1, 2] and           # baño dentro o en el terreno
        desague in [1, 2] and              # red o cámara séptica
        piso in [1, 2]                     # piso bueno o aceptable
    ):
        return "Saludables"

    # Buena:
    if (
        tiene_agua and tiene_banio and
        techo == "Material durable" and
        ubic_banio == 1 and                # baño dentro de la vivienda
        desague == 1 and                   # conexión a red
        piso == 1 and                      # piso de alta calidad
        origen_agua == 1 and               # agua de red pública
        tipo_banio == 1                    # inodoro con descarga
    ):
        return "Buena"

    # Valor por defecto por si algún caso no matchea con claridad
    return "Regular"


def agregar_columna_clasificar_habitabilidad(csv_inicial, csv_final):
    """
    Agrega una columna 'CONDICION_DE_HABITABILIDAD' al CSV, usando la función de clasificación definida.
    Args:
        csv_inicial (Path): Ruta del archivo CSV original.
        csv_final (Path): Ruta del archivo CSV destino (mismo archivo de origen).
    """
    with csv_inicial.open(mode='r', encoding='utf-8') as f_inicial:
        leerDic = csv.DictReader(f_inicial, delimiter = ';')
        filas = []

        for fila in leerDic:

            fila['CONDICION_DE_HABITABILIDAD'] = clasificar_habitabilidad(fila)
            filas.append(fila)

    encabezados = list(filas[0].keys())

    with csv_final.open(mode='w', encoding='utf-8', newline='') as f_final:
        escritor = csv.DictWriter(f_final, fieldnames=encabezados, delimiter=';')
        escritor.writeheader()
        escritor.writerows(filas)

    print(f"Archivo guardado con columna 'CONDICION_DE_HABITABILIDAD': {csv_final}")


# 7. 
print('___________________Punto 7___________________')
agregar_columna_tipo_hogar(archivo, archivo)

# 8. 
print('___________________Punto 8___________________')
agregar_columna_material_techumbre(archivo, archivo)

# 9.
print('___________________Punto 9___________________')
agregar_columna_densidad_hogar(archivo, archivo)

# 10.
print('___________________Punto 10___________________')
agregar_columna_clasificar_habitabilidad(archivo, archivo)
