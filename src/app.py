import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage 
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain

load_dotenv()



def get_vector_store(url):
    #Get the text in document form
    loader = WebBaseLoader(url)
    document = loader.load()

    #Split the document into sub-parts
    text_splitter = RecursiveCharacterTextSplitter()
    document_chunks = text_splitter.split_documents(document)
    
    # Chroma Vector Store
    vector_store = Chroma.from_documents(document_chunks, OpenAIEmbeddings())
    return vector_store
    

def get_context_retriever_chain(vector_store):
    llm = ChatOpenAI()

    retriever = vector_store.as_retriever()
 
    prompt = ChatPromptTemplate.from_messages(
        [
            MessagesPlaceholder(variable_name="chat_history"),
            ("user","{input}"),
            ("user","Given the above conversation, generate a search query to look up in order to get information relevant to the conversation")
        ]
    )

    retriever_chain = create_history_aware_retriever(llm,retriever,prompt)
    return retriever_chain

def conversational_rag_chain(retriever_chain):
    
    llm = ChatOpenAI()
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system","Answer the below questions based on the below context:\n\n{context}"),
            MessagesPlaceholder(variable_name="chat_history"),
             ("user","{input}")  
        ]
    )
    stuff_documents = create_stuff_documents_chain(llm,prompt)

    return create_retrieval_chain(retriever_chain,stuff_documents)

def get_response(user_query):
    #create conversation chain
    retriever_chain = get_context_retriever_chain(st.session_state.vector_store)
    conversation_rag_chain = conversational_rag_chain(retriever_chain)
    
    #response = get_response(user_query )
    response = conversation_rag_chain.invoke({
        "chat_history": st.session_state.chat_history,
        "input": user_query
    })

    return response['answer']




#Page Config
st.set_page_config(page_title="WebChat-AI", page_icon="🤖")
st.title("WebChat Ai ✨")


with open("assets/style.css") as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

#SideBar
with st.sidebar:
    st.header("About the website")
    st.write("<span class='webinfo'>This website helps you to interact with any website and get a better understanding and information about the content of that website.</span>", unsafe_allow_html=True)
    website_url = st.text_input("Paste any website URL    👇")
    

if website_url is None or website_url == "":
    st.info("Please Enter any Website URL to start a conversation 😴")

else:
    #Session State
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            AIMessage(content="Hello, I am an Ai bot! How can I help you?")]

    if "vector_store" not in st.session_state:
        st.session_state.vector_store =  get_vector_store(website_url)

    #User Input 
    user_query = st.chat_input("Type you text here...")
    if user_query is not None and user_query != " ":
        response = get_response(user_query)
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        st.session_state.chat_history.append(AIMessage(content=response))



    #conversation 
    for message in st.session_state.chat_history:
        if isinstance(message,AIMessage):
            with st.chat_message("ai"):
                st.write(message.content)
        elif isinstance(message,HumanMessage):
            with st.chat_message("human"):
                st.write(message.content)


