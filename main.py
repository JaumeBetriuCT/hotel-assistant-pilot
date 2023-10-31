import streamlit as st

from semantic_query_engine import SemanticQueryEngine
from PIL import Image
import base64

from streamlit_frontend import show_chat_history, set_background, set_title

def main():

    hotel_logo = Image.open('images/hotel_logo.png')
    gpt_logo = Image.open("images/Chat_gpt_logo.png")
    icon = Image.open("images/dqs_icon.jpeg")
    sql_logo = Image.open("images/sql_logo.png")

    st.set_page_config(page_icon=icon, page_title="Hotel assistant")
    set_background()
    set_title(hotel_logo)

    # Define the chat history:
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Define if is is the first time the user enters the sessin or not:
    if "first_refresh_session" not in st.session_state:
        st.session_state.first_refresh_session = True
    else:
        st.session_state.first_refresh_session = False

    # Prepare the assitant if it is the first session:
    if st.session_state.first_refresh_session:
        with st.spinner("Preparing the assistant..."):
            st.session_state.semantic_query_engine = SemanticQueryEngine()

    show_chat_history(icon)

    input_text = st.chat_input("Escribe tu mensaje")

    if input_text:
        with st.spinner("Buscando la información en nuestra base de datos..."):
            # Generate the response:
            response = st.session_state.semantic_query_engine.execute_query(input_text)

            # Show the question:
            with st.chat_message("user"):
                st.write(input_text)
            # Show the answer:
            with st.chat_message("user", avatar=icon):
                st.write(response)

            # Store the question and the response to the chat memory of the session:
            st.session_state.chat_history.append({"user": input_text, "avatar": response})

    col3, col4 = st.columns(2)
    with col3:
        st.write("Data hosted in:")
        st.image(sql_logo, width=250)
    with col4:
        st.write("Powered by:")
        st.image(gpt_logo, width=250)

if __name__ == "__main__":
    main()