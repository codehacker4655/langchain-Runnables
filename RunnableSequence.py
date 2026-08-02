#RunnableSequence is a sequential chain of runnables in langchain that executes each step one after another,passing the output of one step as the input to the next.
#It is useful for creating complex workflows that require multiple steps to be executed in a specific order.
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser

prompt1=PromptTemplate(template="Write a joke about {person}?",input_variables=["person"])
prompt2=PromptTemplate(template='Now, rewrite the joke {text} in a sarcastic tone and also explain it.',input_variables=["text"])
model = ChatGroq(model='openai/gpt-oss-120b')
parser=StrOutputParser()
chain=RunnableSequence(prompt1,model,parser,prompt2,model,parser)
result=chain.invoke({"person":"Donald Trump"})
print(result)