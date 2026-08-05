import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage
import uuid

def generate_thread_id():
    thread_id=uuid.uuid4()
    st.session_state['thread_id']=thread_id
    return thread_id

def reset_chat():
    thread_id=generate_thread_id()
    st.session_state['thread_id']=thread_id
    add_thread(thread_id)
    st.session_state['history_message']=[]

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_thread']:
        st.session_state['chat_thread'].append(thread_id)

def load_conversations(thread_id):
    state=chatbot.get_state(config={'configurable':{'thread_id':thread_id}})
    return state.values.get('messages',[])

if 'history_message' not in st.session_state:
    st.session_state['history_message']=[]
if 'thread_id' not in st.session_state:
    st.session_state['thread_id']=generate_thread_id()
if 'chat_thread' not in st.session_state:
    st.session_state['chat_thread']=[]

st.sidebar.title('LangGraph ChatBot')
if st.sidebar.button('New Chat'):
    reset_chat()

st.sidebar.header('Conversations')
for thread in st.session_state['chat_thread']:
    messages=load_conversations(thread)
    title = "New Chat"
    for message in messages:
        if isinstance(message, HumanMessage):
            title = message.content[:10]
            if len(message.content) > 10:
                title += "..."
            break
    if st.sidebar.button(title,key=str(thread)):
        st.session_state['thread_id']=thread
        temp_messages=[]
        for message in messages:
            if isinstance(message,HumanMessage):
                role='user'
            else:
                role='assistant'
            temp_messages.append({'role':role,'content':message.content})
        st.session_state['history_message']=temp_messages
        st.rerun()

for message in st.session_state['history_message']:
    with st.chat_message(message['role']):
        st.write(message['content'])

user_input=st.chat_input("Enter Message Here...")

config={'configurable':{'thread_id':st.session_state['thread_id']}}
add_thread(st.session_state['thread_id'])

if user_input:
    st.session_state['history_message'].append({'role':'user','content':user_input})
    with st.chat_message('user'):
        st.write(user_input)
    response=chatbot.invoke({'messages':[HumanMessage(content=user_input)]},config=config)
    ai_message=response['messages'][-1].content
    with st.chat_message('assistant'):
        st.write(ai_message)
    st.session_state['history_message'].append({'role':'assistant','content':ai_message})
    




