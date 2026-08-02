#RunnableLambda changes the data.
#RunnableLambda is a Runnable that wraps any python function so it can be part of a Langchain workflow.
#RunnablePassthrough is a Runnable that returns the input unchanged.
#RunnablePrimitve - is a special type of runnable whose job is not perform ai tasks, but to organoze,coordinate,and execute other Runnables into a workflow
#Runnable Primitives are orchestration Runnables. They don't perform domain-specific AI tasks; instead, they define and execute how multiple Runnables interact within a workflow, such as sequential execution (RunnableSequence), parallel execution (RunnableParallel), custom transformations (RunnableLambda), or preserving inputs (RunnablePassthrough).
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda
from langchain_core.output_parsers import StrOutputParser

def word_counter(text):
    return len(text.split())

runnable_word_counter=RunnableLambda(word_counter)

print(runnable_word_counter.invoke("This is a test sentence to count words."))
