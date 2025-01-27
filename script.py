import os
import pandas as pd

# Rutas de los archivos
archivo_entrada = r"C:\Users\DanielZuniga\Downloads\ResultsEntrada.csv"
archivo_salida = r"C:\Users\DanielZuniga\Downloads\ResultsSalida.csv"

# Verificar si el archivo de entrada existe
if not os.path.exists(archivo_entrada):
    print(f"Error: El archivo de entrada '{archivo_entrada}' no existe.")
else:
    # Leer el archivo de entrada
    df = pd.read_csv(archivo_entrada)

    # Eliminar filas duplicadas basadas en las columnas 'Nombre', 'Apellido', 'FechaEntrada' y 'HoraEntrada'
    df = df.drop_duplicates(subset=['Nombre', 'Apellido', 'FechaEntrada', 'HoraEntrada'], keep='first')

    # Crear nuevas columnas constantes
    df['IDNodo'] = 85
    df['IDPadre'] = 2

    # Generar el ID
    if 'ID' in df.columns:
        # Si la columna ID ya existe, continuar desde el último ID
        ultimo_id = df['ID'].max()
        df['ID'] = range(ultimo_id + 1, ultimo_id + 1 + len(df))
    else:
        # Si la columna ID no existe, empezar desde 1
        df['ID'] = range(1, 1 + len(df))

    # Reordenar columnas si es necesario
    columnas_deseadas = ['ID', 'IDNodo', 'IDPadre'] + [col for col in df.columns if col not in ['ID', 'IDNodo', 'IDPadre']]
    df = df[columnas_deseadas]

    # Guardar el archivo de salida
    try:
        # Si ya existe, lo reemplaza; si no existe, lo crea
        df.to_csv(archivo_salida, index=False)
        print(f"Archivo transformado guardado (o reemplazado) en: {archivo_salida}")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
