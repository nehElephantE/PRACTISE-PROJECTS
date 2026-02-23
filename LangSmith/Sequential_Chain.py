from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic': 'Unemployment in India'})

print(result)


# .env mein LangSmith related variables define karo
#OPEN_API_KEY
#LANGSMITH_API
#LANGSMITH_TRACING_V2 = TRUE...this enables the tracing
#LANGSMITH_ENDPOINT = "url___jaahan___pr___test karna ho"
#LANGSMITH_PROJECT = 'new_project' ...har new project ka new name define karna
