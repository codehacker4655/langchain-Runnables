# 🚀 LangChain Runnable Primitives

A hands-on learning repository demonstrating the core **Runnable Primitives** in **LangChain**. This project contains practical examples of how to build sequential, parallel, conditional, and custom workflows using LangChain's Runnable interface.

The repository is designed for beginners who want to understand how LangChain workflows are orchestrated using Runnable Primitives.

---

## 📌 What are Runnable Primitives?

Runnable Primitives are **orchestration Runnables**. They do not perform AI tasks themselves. Instead, they organize and control how multiple Runnables work together within a workflow.

This repository covers:

- ✅ RunnableSequence
- ✅ RunnableParallel
- ✅ RunnableLambda
- ✅ RunnablePassthrough
- ✅ RunnableBranch

---

# 📂 Project Structure

```
LANGCHAIN_RUNNABLES/
│
├── RunnableSequence.py
├── RunnableParallel.py
├── RunnableLambda.py
├── RunnableLambda_chain.py
├── RunnablePassthrough.py
├── RunnableBranch.py
├── clean_RunnableBranch.py
│
├── Requirements.txt
├── .env.example
└── README.md
```

---

# ✨ Examples Included

## 1️⃣ RunnableSequence

Demonstrates sequential execution of multiple Runnables.

Workflow:

```
User Input
    │
    ▼
Prompt
    │
    ▼
LLM
    │
    ▼
Output Parser
    │
    ▼
Prompt
    │
    ▼
LLM
    │
    ▼
Output Parser
```

Example:
- Generate a joke.
- Rewrite it sarcastically.
- Explain the joke.

---

## 2️⃣ RunnableParallel

Demonstrates parallel execution of independent Runnable pipelines.

Workflow:

```
            User Input
                 │
      ┌──────────┴──────────┐
      ▼                     ▼
Generate Tweet      Generate LinkedIn Post
      │                     │
      └──────────┬──────────┘
                 ▼
         Combined Dictionary
```

Example Output:

```python
{
    "tweet": "...",
    "linkedin": "..."
}
```

---

## 3️⃣ RunnableLambda

Demonstrates how to convert a normal Python function into a Runnable.

Example:

- Word Counter
- Custom data transformation

Example:

```python
def word_counter(text):
    return len(text.split())
```

Converted into:

```python
RunnableLambda(word_counter)
```

---

## 4️⃣ RunnableLambda Chain

Combines:

- RunnableSequence
- RunnableParallel
- RunnableLambda
- RunnablePassthrough

Workflow:

```
Generate Joke

       │

       ▼

RunnableParallel

 ┌─────────────┐
 │             │

 ▼             ▼

Joke      Count Words

 └──────┬──────┘

        ▼

Dictionary Output
```

---

## 5️⃣ RunnablePassthrough

Demonstrates preserving the original input while simultaneously processing it.

Workflow:

```
Generated Joke

       │

RunnableParallel

 ┌──────────────┐
 │              │

 ▼              ▼

Joke       Explain Joke

 └──────┬───────┘

        ▼

{
    joke,
    explanation
}
```

---

## 6️⃣ RunnableBranch

Demonstrates conditional workflows.

Workflow:

```
Generate Report

       │

Count Words

       │

Is Word Count > 500 ?

      / \

    Yes  No

    │      │

Summarize Keep Original

     │      │

     └──┬───┘

        ▼

Final Output
```

The repository includes:

- Basic implementation
- Cleaner implementation (`clean_RunnableBranch.py`)

---

# 🛠️ Technologies Used

- Python
- LangChain
- LangChain Core
- Groq API
- dotenv

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
```

Navigate into the project

```bash
cd LANGCHAIN_RUNNABLES
```

Install dependencies

```bash
pip install -r Requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Running Examples

Run any file individually.

Example:

```bash
python RunnableSequence.py
```

or

```bash
python RunnableParallel.py
```

---

# 📚 Concepts Covered

- Runnable Interface
- invoke()
- RunnableSequence
- RunnableParallel
- RunnableLambda
- RunnablePassthrough
- RunnableBranch
- Sequential Workflows
- Parallel Workflows
- Conditional Workflows
- Data Transformation
- Workflow Orchestration

---

# 🎯 Learning Outcomes

After completing these examples, you'll understand:

- How LangChain executes sequential workflows.
- How to run multiple Runnable pipelines in parallel.
- How to integrate custom Python functions using RunnableLambda.
- How RunnablePassthrough preserves original inputs.
- How RunnableBranch enables conditional execution.
- How Runnable Primitives orchestrate complex LangChain workflows.

---

# ⭐ If you found this repository helpful

Consider giving it a ⭐ on GitHub!
