from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Simple one-line prompt
prompt = PromptTemplate.from_template("{question}")

model = ChatOpenAI()
parser = StrOutputParser()

# Chain: prompt → model → parser
chain = prompt | model | parser

# Run it
result = chain.invoke({"question": "What is the capital of Peru?"})
print(result)


# .env mein langsmith ka api aur baaki env variables batane pe ...woh trace kar lega iss project ko...LangSmith ke UI mein jaakr har ek trace ko jaakr dekh sakte hai ...ki uss instance mein
# input kya tha aur output kya hai
