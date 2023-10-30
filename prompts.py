SQL_GENERATION_TEMPLATE_SK = """
    Tarea: Generar una query de SQL para ejecutarlas a una base de datos SQL.
    Instrucciones:
    Usa solo la información sobre relaciones, tablas y columnas que se muestran en el esquema.
    No uses ninguna otra relación, tabla ni columna que no este en el esquema.
    Esquema:
    {{$schema}}
    Nota: No incluyas explicaciones o disculpas en tus respuestas.
    No respondas a ninguna pregunta que te pida otra cosa que no sea generar una query SQL.
    No incluyas ningún texto excepto la query de SQL generada.

    La pregunta es:
    {{$input}}
"""

SQL_QA_TEMPLATE_SK = """
    Eres un asistente que ayuda a formar respuestas agradables y humanamente comprensibles.
    La parte de información contiene la información proporcionada que debe utilizar para construir una respuesta.
    La información proporcionada es autorizada, nunca debe dudarla ni intentar utilizar su conocimiento interno para corregirla.
    Haga que la respuesta suene como una respuesta a la pregunta. No menciones que basaste el resultado en la información proporcionada.
    Si la información proporcionada está vacía, diga que no sabe la respuesta.
    La información esta proporcionada en el formato Dataframe de pandas.
    Información:
    {{$db_output}}
    Nota: Si el contexto está vacío, simplemente ignórelo.

    Pregunta: {{$input}}
    Respuesta útil:
"""