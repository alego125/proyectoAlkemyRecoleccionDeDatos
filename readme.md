# Extractor Datos Cines, Museos y Bibliotecas Argentina

### Quick start Guide

1) Primero crear y abrir una base de datos postgresql
2) Luego para iniciar, ir al archivo .env y modificar los datos de conexion a la base de datos
3) Seguidamente verificar los links en el mismo archivo .env de los csv para extraer la informacion
4) Instalar un entorno virtual en caso de no tenerlo y luego ejecutarlo (si asi lo desea) para no tener que instalar las librerias en su ordenador
5) Ejecutar pip install -r requirements.txt para instalar las librerias necesarias
6) Ejecutar el comando en consola python main.py

Estos pasos anteriores arrancaran la aplicacion lo cual generara 3 carpetas una para museo, otra para cines y otra para bibliotecas dentro de las cuales contendran sus respectivos archivos csv, seguido a esto el programa extraera la informacion que se necesita de estos archivos y luego la introducira en la base de datos a partir de la informacion suministrada de conexion en el .env.
___
**Nota:** No es necesario borrar las carpetas creadas ya que cada vez que se vuelva a ejecutar el programa reemplazara los archivos por los viejos por los nuevos, al igual que la informacion de la base de datos sera reemplazada por la nueva informacion con su respectiva fecha de modificacion
___
