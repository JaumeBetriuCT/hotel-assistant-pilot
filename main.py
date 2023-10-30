import streamlit as st

from semantic_query_engine import SemanticQueryEngine
from PIL import Image

def show_chat_history(avatar_icon) -> None:
    # Get the history:
    chat_history = st.session_state.chat_history

    # If there is no chat history;
    if len(chat_history) == 0:
        pass

    else:
        # Iterate trough the history chat
        for question_answer_dict in chat_history:
            with st.chat_message("user"):
                st.write(question_answer_dict["user"])
            with st.chat_message("assistant", avatar=avatar_icon):
                st.write(question_answer_dict["avatar"])

def main():

    dqs_logo = Image.open('images/dqs_logo.png')
    gpt_logo = Image.open("images/Chat_gpt_logo.png")
    icon = Image.open("images/dqs_icon.jpeg")
    sql_logo = Image.open("images/sql_logo.png")

    st.set_page_config(page_icon=icon, page_title="DQS chatbot")

    # Define the chat history:
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Define if is is the first time the user enters the sessin or not:
    if "first_refresh_session" not in st.session_state:
        st.session_state.first_refresh_session = True
    else:
        st.session_state.first_refresh_session = False

    st.title("Asistente de reservas Hotel Playa Golf")

    st.image(dqs_logo)

    # Prepare the assitant if it is the first session:
    if st.session_state.first_refresh_session:
        with st.spinner("Preparing the assistant..."):
            st.session_state.semantic_query_engine = SemanticQueryEngine()


    show_chat_history(icon)

    input_text = st.chat_input("Escribe tu mensaje")

    if input_text:
        with st.spinner("Generando respuesta ..."):
            # Generate the response:
            response = st.session_state.semantic_query_engine.execute_query(input_text)

            # Show the question:
            with st.chat_message("user"):
                st.write(input_text)
            # Show the answer:
            with st.chat_message("assistant", avatar=icon):
                st.write(response)

            # Store the question and the response to the chat memory of the session:
            st.session_state.chat_history.append({"user": input_text, "avatar": response})

    col1, col2 = st.columns(2)
    with col1:
        st.write("Data hosted in:")
        st.image(sql_logo, width=250)
    with col2:
        st.write("Powered by:")
        st.image(gpt_logo, width=250)

if __name__ == "__main__":
    main()