from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.sqlite import SqliteSaver
# yeh yahan pe hum log InMemorySaver ni use karenge...ek database se connect kar denge
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
import sqlite3

load_dotenv()

llm = ChatOpenAI()

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState):
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages": [response]}

conn = sqlite3.connect(database='chatbot.db', check_same_thread=False)
# agar yeh DB exists ni karta toh ho jayega
#check_same_threads ko False isiliye karna hai kyuki we will be using mul threads
# byt sqllite mein 1 thread ka hi use hota hai...toh woh check karne wala process band kardo


# Checkpointer
checkpointer = SqliteSaver(conn=conn)

graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpointer)

def retrieve_all_threads():
    all_threads = set()
    for checkpoint in checkpointer.list(None): # saare ke saare checkpoints ka list dega
        all_threads.add(checkpoint.config['configurable']['thread_id'])
# thread_id ke base pe db mein store hoga convo
    return list(all_threads)




