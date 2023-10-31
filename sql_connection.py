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

    def run_query(self, query: str) -> str:
        """Query the SQL database"""

        with self.db_engine.connect() as conn:
            # Transform to dataframe:
            db_output = pd.read_sql(query, conn)
            # Save the extracted data for debugging purposes:
            db_output.to_csv("db_output.csv")

        # Convert the dataframe to an string:
        db_output_a = ', '.join(db_output.apply(lambda row: ', '.join([f'{col}: {row[col]}' for col in db_output.columns]), axis=1))
        if db_output_a not in [None, "", " "]:
            db_output = db_output_a
        else:
            db_output = ""
            
        return db_output

    def get_schema(self) -> str:

        """Get the schema of the data base"""
        # TODO: Extract the schema of the database so the model knows how to generate queries:

        description = """
            La tabla informacion_general contiene las columnas: 'ID', 'Descripcion', 'Direccion', 'Contacto' 
            La tabla habitaciones contiene las columnas: 'ID_Habitacion', 'Tipo_Habitacion', 'Descripcion', 'Link'.
            La tabla disponibilidad contiene las habitaciones disponibles, con las columnas 'ID_Habitacion', 'Tipo_Habitacion', 'Fecha_Entrada, 'Fecha_Salida' y 'Precio'. 
            La tabla instalaciones contiene las instalaciones del hotel, con las columnas: 'ID_Instalacion', 'Nombre_Instalacion', 'Descripcion'
            La tabla servicios contiene los servicios del hotel con las columnas: 'ID_Servicio', 'Nombre_Servicio'
            La tabla servicios_por_habitacion contiene los servicios de cada habitación, con las columnas: 'ID_Habitacion', 'ID_Servicio'
            Relaciones entre tablas:
            - La tabla disponibilidad se relaciona con la tabla habitaciones con la columna ID_Habitacion
            - La tabla servicios_por_habitacion se relaciona con la tabla habitaciones ("ID_Habitacion") y servicios ("ID_Servicio")
        """

        return description


