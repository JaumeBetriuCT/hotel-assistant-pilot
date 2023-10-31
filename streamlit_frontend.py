import streamlit as st

def set_title(hotel_logo):
    col1, col2 = st.columns([3,1])
    with col1:
        st.title("Asistente Hotel Playa Golf")
        st.subheader("Tu asistente personal para consultas y reservas de hotel")

    with col2:
        # Add padding so the picture goes down:
        st.write("   ")
        st.write("   ")
        st.image(hotel_logo, width=250)

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
            with st.chat_message("user", avatar=avatar_icon):
                st.write(question_answer_dict["avatar"])

def set_background():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://img.freepik.com/free-photo/elegant-white-background-with-blue-wave-lines_1017-32741.jpg");
             background-size: 100% 113%
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    
    # To find simillar images to the one in the background type in google images: "sky transparent background"

    # https://img.freepik.com/premium-vector/abstract-grunge-background_660067-262.jpg?size=626&ext=jpg
    # 