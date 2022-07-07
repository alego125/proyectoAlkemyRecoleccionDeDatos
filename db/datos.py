import os
import requests
from core.config import settings
from datetime import datetime
from pathlib import Path
import pandas as pd

def obtenerDatos(url, category:str, date:datetime) -> pd.DataFrame:
    """
        Crea directorio, recupera archivo de url, recupera archivo de directorio y devuelve csv
        1) Crea path 
        2) Usa path para crear directorio si no existe
        3) Trae archivo con request
        4) Crea archivo en directorio
        5) Retorna csv
    """
    
    path = Path('.') / f"{category}"/f"{date.day}_{date.strftime('%B')}"

    if not os.path.exists(category):
        os.makedirs(path)    

    file = requests.get(url, allow_redirects=True)

    open(f"{path}/{category}-{date.day}-{date.strftime('%B')}-{date.year}.csv", 'wb').write(file.content)

    return pd.read_csv(f"{path}/{category}-{date.day}-{date.strftime('%B')}-{date.year}.csv")


def crearDataframes(dataFrame, arregloColumnasDataframe) -> pd.DataFrame:
    """
        Crea DataFrame con columnas especificadas y corrige los nombres para que sean el de todos iguales
        1) Crea dataframe con ciertas columnas
        2) Modifica columnas para que sean las mismas en todos los dataframe
    """

    frame = dataFrame[arregloColumnasDataframe]
    frame.columns = ['Cod_Loc','IdProvincia','IdDepartamento','Categoría','Provincia','Localidad','Nombre','Domicilio','CP','Teléfono','Mail','Web','Fuente']

    return frame

def unirDataframes(dataFrames) -> pd.DataFrame:
    """
        Une Varios dataFrames los cuales vengan en forma de lista. Dichos dataFrames tienen que traer en lo posible las mismas columnas
    """
    return pd.concat(dataFrames, ignore_index=True)


def dataFramesToSql(df, engine, tableName:str):

    """
        Funcion encargada de crear en el dataframe una columna nueva con la fecha de actualizacion actual y de enviar a la base de datos el dataframe final
    """

    df['FechaActualizacion'] = datetime.now()
    df.to_sql(tableName, con=engine, if_exists='replace', index=False)