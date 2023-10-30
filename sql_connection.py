from sqlalchemy import create_engine
import pandas as pd

class AzureSQLDatabaseConnection:

    def __init__(self, sql_server: str, sql_db: str, sql_username: str, sql_pwd: str, driver: str):

        obdc_str = 'mssql+pyodbc:///?odbc_connect=' \
            'Driver='+driver+ \
            ';Server=tcp:' + sql_server+'.database.windows.net;PORT=1433' + \
            ';DATABASE=' + sql_db + \
            ';Uid=' + sql_username+ \
            ';Pwd=' + sql_pwd + \
            ';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

        self.db_engine = create_engine(obdc_str)

    def run_query(self, query: str) -> pd.DataFrame:
        """Query SQL database"""

        with self.db_engine.connect() as conn:
            # Transform to dataframe:
            df = pd.read_sql(query, conn)

        return df

    def get_schema(self) -> str:

        """Get the schema of the data base"""
        # TODO: Extract the schema of the database so the model knows how to generate queries:
        
        description = """
            La tabla informacion_general contiene las columnas: 'ID', 'Descripcion', 'Direccion', 'Contacto' 
            La tabla habitaciones contiene las columnas: 'ID_Habitacion', 'Tipo_Habitacion', 'Descripcion', 'Link'
            La tabla disponibilidad contiene la disponibilidad de cada tipo de habitación. Una habitación estará disponible para los días que están entre la fecha de entrada y la de salida. Esta tabla tiene las columns: 'ID_Habitacion', 'Tipo_Habitacion', 'Fecha_Entrada', 'Fecha_Salida', 'Precio'
            La tabla instalaciones contiene el nombre de las instalaciones del hotel con una descripción con las columnas: 'ID_Instalacion', 'Nombre_Instalacion', 'Descripcion'
            La tabla servicios contiene el nombre de los servicios que ofrece el hotel con las columnas: 'ID_Servicio', 'Nombre_Servicio'
            La tabla servicios_por_habitacion contiene los servicios que tiene cada habitación del hotel con las columnas: 'ID_Habitacion', 'ID_Servicio'
            Relaciones entre tablas:
            - La tabla disponibilidad se relaciona con la tabla habitaciones con la columna ID_Habitacion
            - La tabla servicios_por_habitacion contiene relaciones con las tablas de habitaciones y servicios. Puede obtener información sobre los servicios disponibles en cada tipo de habitación.
        """

        return description


