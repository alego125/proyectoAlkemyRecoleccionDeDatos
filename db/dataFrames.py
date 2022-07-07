import pandas as pd
from core.config import settings
from datetime import datetime
from db.datos import crearDataframes, dataFramesToSql, obtenerDatos, unirDataframes

def armadoDataFrameCine(urlMuseo, urlCine, urlBiblioteca):

    """
        Funcion que recibe las url de los dataframe con esto trae y devuelve los dataframe completos de:
        * Cine
        * Museo
        * Biblioteca
        * Datos Cantidades de cine
    """

    # Se obtienen los dataframe completos
    dfMuseo = obtenerDatos(urlMuseo,'museo',datetime.now())
    dfCine = obtenerDatos(urlCine,'cine',datetime.now())
    dfBiblioteca = obtenerDatos(urlBiblioteca,'biblioteca',datetime.now())

    cantidadesCine = dfCine[['Provincia','Pantallas', 'Butacas', 'espacio_INCAA']]

    return dfBiblioteca, dfCine, dfMuseo, cantidadesCine

def recorteDataframes(dfMuseo, dfCine, dfBiblioteca, columnsMuseo, columnsCine, columnsBiblioteca):

    """
        Recorta el dataframe con las columnas indicadas y devuelve una tupla de:
        * DataFrame Museo
        * DataFrame Cine
        * DataFrame Biblioteca
    """

    # Se extraen las columnas indicadas del dataframe
    dfMuseo = crearDataframes(dfMuseo,columnsMuseo)
    dfCine = crearDataframes(dfCine,columnsCine)
    dfBiblioteca = crearDataframes(dfBiblioteca,columnsBiblioteca)

    return dfBiblioteca, dfCine, dfMuseo

def unionCreacionDataFramesAlternativos(dfMuseo,dfBiblioteca,dfCine):

    """
        Funcion que a partir del los dataframe unidos Crea tablas alternativas
        Devuelve:
        * DataFrame De la union de los 3 indicados como parametros
        * DataFrame De cantidades totales de categorias, fuentes y PRovincias con Categorias
    """

    dfUnidos = unirDataframes([dfMuseo,dfBiblioteca,dfCine])

    regTotalCateg = dfUnidos[['Categoría']].count()
    regTotalCateg = regTotalCateg['Categoría']
    regTotalFuente = dfUnidos[['Fuente']].count()
    regTotalFuente = regTotalFuente['Fuente']
    regTotalRegCateg = dfUnidos.groupby(['Provincia','Categoría'])['Cod_Loc'].count()
    regTotalRegCateg = regTotalRegCateg.count()

    dfDatosUnidos = pd.DataFrame({"Categorias":regTotalCateg,"Fuentes":regTotalFuente,"ProvinciasCategorias":regTotalRegCateg}, index=[1])

    return dfUnidos, dfDatosUnidos

def guardarEnBaseDatos(dfUnidos,dfDatosUnidos,cantidadesCine,engine):

    """
        Funcion que llama a la funcion que plasma los dataFrame en la base de datos
    """

    dataFramesToSql(dfUnidos, engine, "GlobalData")
    dataFramesToSql(dfDatosUnidos, engine,"SegmentsGlobalData")
    dataFramesToSql(cantidadesCine, engine,"CinesData")

    