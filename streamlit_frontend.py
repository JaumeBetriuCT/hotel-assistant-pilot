import streamlit as st

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
             background: url("https://i.pinimg.com/1200x/94/32/6c/94326cc12d92893263a4d4139aff60de.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    
    # To find simillar images to the one in the background type in google images: "sky transparent background"

    # https://i.pinimg.com/736x/4b/2a/9b/4b2a9bfe892f32fcda6ed95cc6b57f98.jpg
    # https://i.pinimg.com/1200x/94/32/6c/94326cc12d92893263a4d4139aff60de.jpg