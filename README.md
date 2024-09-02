# WebChat Ai - A LangChain Chatbot with Streamlit GUI

## Features
- **Website Interaction**: The chatbot uses LangChain to interact with and extract information from various websites.
- **Large Language Model Integration**: Powered by GPT-4.
- **Streamlit GUI**: A clean and intuitive user interface built with Streamlit.
- **Python-based**: Entirely coded in Python.
- **CSS: Used CSS to make the GUI more attractive and user-friendly.

## How Project works
- User Paste's any website link to the input box.
- All the website text is scrapped using BeautifulSoup.
- Text is split into small chunks so that it can be fed to the Embeddings Model.
- Embeddings model performs vectorization and stores it in vector data base.
- The user query is also embeded and top matching text present in the vector data base is found out through semantic search.
- The Top ranked text found from our webpage data and the user query both are feeded to the LLM model.
- LLM model produces the answer to the query and displays it to the user.

## RAG Bot and project flow
- A RAG chatbot is an AI-powered chatbot that uses Retrieval Augmented Generation (RAG) to provide more accurate and relevant responses than traditional chatbots.

![RAG-diagram](https://github.com/user-attachments/assets/8412e9c5-9d02-4b71-a69c-1e6a26247e40)



