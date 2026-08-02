#RunnableParallel is a runnable primitive that allows executing multiple runnables in parallel and collecting their outputs.
#Each runnable receives the same input and process it independently,producing a dictonary of outputs
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableParallel
from langchain_core.output_parsers import StrOutputParser

prompt1=PromptTemplate(template="Generate a tweet about {topic}",input_variables=["topic"])
prompt2=PromptTemplate(template="Generate a LinkedIn post about {topic}",input_variables=["topic"])
model = ChatGroq(model='openai/gpt-oss-120b')

parallel_chain=RunnableParallel({
    "tweet":RunnableSequence(prompt1,model,StrOutputParser()),
    "linkedin":RunnableSequence(prompt2,model,StrOutputParser())    
})

result=parallel_chain.invoke({"topic":"AI in healthcare"})
print(result)
print('------------------------------')
print(type(result))
print('------------------------------')
print(type(result['tweet']))