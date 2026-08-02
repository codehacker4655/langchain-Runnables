from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableSequence,
    RunnableParallel,
    RunnablePassthrough,
    RunnableLambda,
    RunnableBranch
)
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# -----------------------------
# LLM
# -----------------------------
model = ChatGroq(model="openai/gpt-oss-120b")
parser = StrOutputParser()

# -----------------------------
# Prompts
# -----------------------------
report_prompt = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

summary_prompt = PromptTemplate(
    template="Summarize the following report:\n\n{text}",
    input_variables=["text"]
)

# -----------------------------
# Report Generation Chain
# -----------------------------
report_chain = RunnableSequence(
    report_prompt,
    model,
    parser
)

# -----------------------------
# Word Counter
# -----------------------------
def word_counter(text):
    return len(text.split())

word_counter_runnable = RunnableLambda(word_counter)

# -----------------------------
# Summary Branch
# -----------------------------
summary_branch = RunnableSequence(
    RunnableParallel({
        "report": RunnablePassthrough(),
        "initial_word_count": word_counter_runnable
    }),

    RunnableLambda(lambda x: {
        "text": x["report"],
        "initial_word_count": x["initial_word_count"]
    }),

    RunnableParallel({
        "summary": RunnableSequence(
            summary_prompt,
            model,
            parser
        ),
        "initial_word_count": RunnableLambda(
            lambda x: x["initial_word_count"]
        )
    }),

    RunnableLambda(lambda x: {
        "report": x["summary"],
        "initial_word_count": x["initial_word_count"],
        "changed_word_count": len(x["summary"].split())
    })
)

# -----------------------------
# Branch
# -----------------------------
branch_chain = RunnableBranch(

    (
        lambda x: len(x.split()) > 500,
        summary_branch
    ),

    RunnableParallel({
        "report": RunnablePassthrough(),
        "initial_word_count": word_counter_runnable
    })
)

# -----------------------------
# Final Chain
# -----------------------------
final_chain = RunnableSequence(
    report_chain,
    branch_chain
)

result = final_chain.invoke({
    "topic": "AI in Healthcare"
})

print(result)