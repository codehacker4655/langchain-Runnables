from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
#RunnableLambda changes the data.
#RunnableLambda is a Runnable that wraps any python function so it can be part of a Langchain workflow.
#RunnablePassthrough is a Runnable that returns the input unchanged.
#RunnablePrimitve - is a special type of runnable whose job is not perform ai tasks, but to organoze,coordinate,and execute other Runnables into a workflow
#Runnable Primitives are orchestration Runnables. They don't perform domain-specific AI tasks; instead, they define and execute how multiple Runnables interact within a workflow, such as sequential execution (RunnableSequence), parallel execution (RunnableParallel), custom transformations (RunnableLambda), or preserving inputs (RunnablePassthrough).

prompt1=PromptTemplate(template="write a joke about {topic}",input_variables=["topic"])
prompt2=PromptTemplate(template="Explain the joke {text}",input_variables=["text"])
parser=StrOutputParser()
model = ChatGroq(model='openai/gpt-oss-120b')
passthrough=RunnablePassthrough()

joke_gen_chain=RunnableSequence(prompt1,model,parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({"topic": "AI in healthcare"})
print(result)