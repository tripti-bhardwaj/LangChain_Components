from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableBranch

load_dotenv()

prompt1 = PromptTemplate(
    template = "Generate a detailed report on {topic}.",
    input_variables = ["topic"]
)

prompt2 = PromptTemplate(
    template = "Summarize the following text: \n {text}",
    input_variables = ["text"]
)
model = ChatOpenAI()

parser = StrOutputParser()

report_generation_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch({
    (lambda x: len(x.split() > 500), RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
    })

final_chain = RunnableSequence(report_generation_chain, branch_chain)

result = final_chain.invoke({"topic": "AI"})

print(result)