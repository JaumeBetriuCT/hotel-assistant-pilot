# Hotel assistant pilot
This repo contains the implementation of a virtual assistant that allows you to interact with a SQL database to get information from a hotel

## Data
The data used is fake

## Run the streamlit app
The project uses the library semantic-kernel for finetunning the GPT model to your own data and Streamlit for creating a user-friendly interface.

To run the virtual assistant run:

```
streamlit run main.py
```

## Cloud deploy
The repo can be deployed on streamlit cloud following the instructions in the page: https://streamlit.io/cloud

Once deployed the app will be accessible from any device using a navigator.

## Open AI api-keys management
To add the Open AI key create a folder in the repo with the name .streamlit and inside crate a file named secrets.toml and add the key with the format:

OPENAI_API_KEY="sk-..."p