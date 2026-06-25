from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

prompt1 = PromptTemplate(
    template = "Generate a fact about {topic}.",
    input_variables = ["topic"]
)

prompt2 = PromptTemplate(
    template = "Explain the following text: \n {text}",
    input_variables = ["text"]
)

model = ChatOpenAI()

parser = StrOutputParser()

fact_generation_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    "fact": RunnablePassthrough(),
    "explanation": RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(fact_generation_chain, parallel_chain)

result = final_chain.invoke({"topic": "AI"})

print(result)