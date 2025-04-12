# Proyecto: TRABAJO PRÁCTICO INTEGRADOR

## Descripción


---

## Estructura del Proyecto

- **`files/`**: contiene las carpetas con los datasets.
  - `hogares/`: contiene los datasets de hogares.
  - `individuos/`: contiene los datasets de individuos.
- **`notebooks/`**: contiene las notebooks con los programas principales.
  - `main_individuos.ipynb`: programa principal para procesar datasets de individuos.
  - `main_hogares.ipynb`: programa principal para procesar datasets de hogares.
- **`src/`**: Contiene las funciones Python necesarias para procesar los archivos.
  - `lectura.py`: Funciones de lectura y guardado.
  - `__init__.py`: Archivo que convierte el directorio en un paquete Python.
- **`venv/`**: Contiene el entorno virtual.
  - `.gitignore`
  - `LICENSE`: Detalles de la licencia del proyecto.
  - `requirements.txt`: Lista de dependencias necesarias.
  - `README.md`: Documentación principal.

---

## Instalación

Realiza los pasos detallados a continuación para instalar y ejecutar el proyecto:

### 1. Obtener el repositorio



### 2. Activar entorno virtual

Crear y activar un entorno virtual
Ejecuta los siguientes comandos:
```bash
python -m venv venv
```
En Windows:
```bash
venv\Scripts\activate
```

En Mac/Linux:
```bash
source venv/bin/activate
```
Una vez activado el entorno, deberías ver (venv) al inicio de tu terminal, indicando que estás trabajando dentro del entorno virtual.

### 3. Instalar dependencias
Con el entorno virtual activado, instala las dependencias necesarias usando el archivo requirements.txt:
```bash
pip install -r requirements.txt
```

### Ejecución del Programa
Abre el notebook principal en Jupyter Notebook:
```bash
jupyter notebook notebooks/main_hogares.ipynb
```
```bash
jupyter notebook notebooks/main_individuos.ipynb
```

Ejecuta las celdas del notebook. 
Asegúrate de seguir las instrucciones iniciales para realizar los imports necesarios.

### Observaciones
- Este proyecto fue desarrollado y probado con **Python 3.12.9**, pero debería ser compatible con Python 3.8 o superior. Verifica tu versión ejecutando:
```bash
python --version
```
### Datos alumnos
GRUPO 14

Nombre completo:
Legajo:

Nombre completo:
Legajo:

Nombre completo:
Legajo:

Nombre completo:
Legajo:

Nombre completo:
Legajo:




