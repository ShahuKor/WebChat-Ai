# WebChat Ai - A LangChain Chatbot with Streamlit GUI

## Features
- **Website Interaction**: The chatbot uses LangChain to interact with and extract information from various websites.
- **Large Language Model Integration**: Powered by GPT-4.
- **Streamlit GUI**: A clean and intuitive user interface built with Streamlit.
- **Python-based**: Entirely coded in Python.
- **CSS**: Used CSS to make the GUI more attractive and user-friendly.

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

## Project Screenshots and Demo
- For the Demo we are using Wikipedia Page of "INDIA IN OLYMPICS 2024".
<img width="1470" alt="Screenshot 2024-09-02 at 4 19 33 PM" src="https://github.com/user-attachments/assets/4666d627-2c1b-4a56-8753-38af380d947f">

- Paste the link of Wikipedia website in the input box.
<img width="1470" alt="Screenshot 2024-09-02 at 4 19 43 PM" src="https://github.com/user-attachments/assets/827b4c85-b30e-4b51-8c9f-befd93f743e9">

- After the link is pasted, the bot automatically start.
<img width="1470" alt="Screenshot 2024-09-02 at 4 19 50 PM" src="https://github.com/user-attachments/assets/8806cff9-51ea-4ae4-be45-c11bf2b5e83b">

- Question 1
<br>
<img width="1470" alt="Screenshot 2024-09-02 at 4 20 22 PM" src="https://github.com/user-attachments/assets/99dfd458-8fc7-4a52-a933-e10e8c03d820">

- Question 2
<img width="1470" alt="Screenshot 2024-09-02 at 4 20 51 PM" src="https://github.com/user-attachments/assets/f4b8c196-c8ea-4699-8412-3348db94def6">

- Question 3. The bot also remembers the chat history and answers accordingly.
<img width="1470" alt="Screenshot 2024-09-02 at 4 22 16 PM" src="https://github.com/user-attachments/assets/1f28e62f-241f-4e1c-af1e-8154ddf0bb9e">

- Question 4. It also summarizes the webpage information.
<img width="1470" alt="Screenshot 2024-09-02 at 4 25 34 PM" src="https://github.com/user-attachments/assets/ef44199b-e7d0-4ca4-acf0-41c327a5be77">

  





