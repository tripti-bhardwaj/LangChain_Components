from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()

prompt = PromptTemplate(
    template = "Generate a fact about {topic}.",
    input_variables = ["topic"]
)

model = ChatOpenAI()

parser = StrOutputParser()

fact_generator_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    "fact": RunnablePassthrough(),
    "word_count": RunnableLambda(lambda x: len(x.split()))
})

final_chain = RunnableSequence(fact_generator_chain, parallel_chain)

result = final_chain.invoke({"topic": "AI"})

print(result)