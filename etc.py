from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableLambda,
    RunnablePassthrough,
    RunnableParallel,
    RunnableSequence
)

# Prompt 1
joke_prompt = PromptTemplate(
    template="Generate a funny joke about {topic}.",
    input_variables=["topic"]
)

# Prompt 2
explain_prompt = PromptTemplate(
    template="""
Explain the following joke in a {mode} manner.

Joke:
{text}
""",
    input_variables=["text", "mode"]
)

parser = StrOutputParser()
model = ChatGroq(model='openai/gpt-oss-120b')


# Chain to generate joke
joke_chain = joke_prompt | model | parser

# Complete Workflow
workflow = RunnableSequence(
    RunnableParallel(
        joke=joke_chain,
        original=RunnablePassthrough()
    )
    , RunnableLambda(
        lambda x: {
            "joke": x["joke"],
            "text": x["joke"],
            "mode": x["original"]["mode"]
        }
    )
    , RunnableParallel(
        joke=RunnableLambda(lambda x: x["joke"]),
        explanation=(
            explain_prompt
            | model
            | parser
        )
    )
)

result = workflow.invoke({
    "topic": "Artificial Intelligence",
    "mode": "beginner"
})

print(result)