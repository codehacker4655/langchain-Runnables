#to create conditional chains 
from cffi import model
from langchain_groq import ChatGroq
from dotenv import load_dotenv, parser
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda,RunnableBranch
from langchain_core.output_parsers import StrOutputParser

prompt=PromptTemplate(template="write a detailed report on {topic}",input_variables=['topic'])

prompt2=PromptTemplate(template="summarize the following \n {text}",input_variables=['text'])

parser=StrOutputParser()

model=ChatGroq(model='openai/gpt-oss-120b')

report_gen_chain=RunnableSequence(prompt,model,parser)

def word_counter(text):
    return len(text.split())

runnable_word_counter=RunnableLambda(word_counter)

#(condition,chain), default branch must and should 
branch_chain = RunnableBranch(
    (lambda x: len(x.split())>500,RunnableParallel({'intial_word_count':runnable_word_counter,'the_final_report':RunnableSequence(prompt2,model,parser,RunnableParallel({'report':RunnablePassthrough(),'changed_word_count':runnable_word_counter}))})),
    RunnableParallel({
        'report':RunnablePassthrough(),
        'word_count':runnable_word_counter
    }))



final_chain=RunnableSequence(report_gen_chain,branch_chain)
result=final_chain.invoke({"topic":"AI in healthcare"})
print(result)

