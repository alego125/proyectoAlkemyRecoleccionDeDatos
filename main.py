


from db.datos import *
from db.database import engine
from core.config import settings
from db.dataFrames import *

COLUMNS_CINE = ['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'Categoría', 'Provincia',
       'Localidad', 'Nombre', 'Dirección', 'CP', 'Teléfono', 'Mail', 'Web',
       'Fuente']
COLUMNS_MUSEO = ['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'Categoría', 'Provincia',
       'Localidad', 'Nombre', 'Domicilio', 'CP', 'Teléfono', 'Mail', 'Web',
       'Fuente']
COLUMNS_BIBLIOTECA = ['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'categoria', 'provincia',
       'localidad', 'nombre', 'direccion', 'CP', 'telefono', 'Mail', 'Web',
       'fuente']

def initMigrations():
       """ 
       Funcion encargada de orquestar la ejecucion de las tareas de migracion de la informacion a la base de datos
       """
       
       dfMuseo,dfCine,dfBiblioteca,cantidadesCine = armadoDataFrameCine(settings.URL_MUSEO,
                                                                      settings.URL_CINE,
                                                                      settings.URL_BIBLIOTECA)       

       dfMuseo,dfCine,dfBiblioteca = recorteDataframes(dfMuseo,
                                                        dfCine,
                                                        dfBiblioteca,
                                                        COLUMNS_MUSEO, 
                                                        COLUMNS_CINE, 
                                                        COLUMNS_BIBLIOTECA)

       dfUnidos, dfDatosUnidos = unionCreacionDataFramesAlternativos(dfMuseo,
                                                                      dfCine,
                                                                      dfBiblioteca)

       guardarEnBaseDatos(dfUnidos, 
                            dfDatosUnidos, 
                            cantidadesCine,
                            engine)


if __name__ == '__main__':
       
       initMigrations()