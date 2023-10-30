import streamlit as st
import semantic_kernel as sk

from sql_connection import AzureSQLDatabaseConnection
from prompts import SQL_GENERATION_TEMPLATE_SK, SQL_QA_TEMPLATE_SK
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

class SemanticQueryEngine:
    def __init__(self):

        self.azure_sql_database_connection = AzureSQLDatabaseConnection(
            sql_server = st.secrets["SQL_SERVER"],
            sql_db = st.secrets["SQL_DB"],
            sql_username = st.secrets["SQL_USERNAME"],
            sql_pwd = st.secrets["SQL_PWD"],
            driver = st.secrets["DRIVER"]
        )

        self.kernel_sql, self.kernel_qa = sk.Kernel(), sk.Kernel()
        self.api_key = st.secrets["OPENAI_API_KEY"]

        # Add the model to the kernel:
        self.kernel_sql.add_chat_service("sql", OpenAIChatCompletion("gpt-3.5-turbo-16k", self.api_key))
        self.kernel_qa.add_chat_service("qa", OpenAIChatCompletion("gpt-3.5-turbo-16k", self.api_key))

        # Create the context for the sql generator and add the description of the database:
        self.context_sql = self.kernel_sql.create_new_context()
        self.context_sql["schema"] = self.azure_sql_database_connection.get_schema()

        # Create the context for the qa model:
        self.context_qa = self.kernel_qa.create_new_context()

        # Create the functions of the sql generator and the qa:
        self.sql_generator = self.kernel_sql.create_semantic_function(SQL_GENERATION_TEMPLATE_SK)
        self.qa_generator = self.kernel_qa.create_semantic_function(SQL_QA_TEMPLATE_SK)

    def execute_query(self, input_text: str) -> str:
        """Creates a sql quer, executes it and returns the response from the LLM"""
        
        print("Generating SQL query...")

        generated_sql_query = self.sql_generator(input_text, context=self.context_sql)["input"]

        print("Generated SQL query:")
        print(generated_sql_query)

        # Execute the query and get the results from the database:
        db_output = self.azure_sql_database_connection.run_query(generated_sql_query)
        # Store the generated Dataframe:
        db_output.to_csv("db_output.csv")

        # Convert the dataframe to an string:
        db_output = str(db_output)

        print("DB output:")
        print(db_output)

        # Add the DB output as context for the QA kernel:
        self.context_qa["db_output"] = db_output

        # Generate the response of the QA:
        response = self.qa_generator(input_text, context=self.context_qa)["input"]

        return response

