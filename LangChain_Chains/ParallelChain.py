from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model1 = ChatOpenAI()
model2 = ChatAnthropic()

prompt1 = PromptTemplate(
    template = "Generate short and simple notes from the following text: \n {topic}.",
    input_variables = ["text"]
)

prompt2 = PromptTemplate(
    template = "Generate 5 short question-answers from the following text: \n {text}",
    input_variables = ["text"]
)

prompt3 = PromptTemplate(
    template = "Merge the provided notes and quiz into a single document: \n notes: {notes} \n quiz: {quiz}",
    input_variable = ["notes", 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """
What are chains in LangChain?
chains are pipelines in langchain which makes our work easier by connecting multiple components.

Different Types of Chains:
1. Simple Chains
Simple Chains are those chains with connect one or two steps. 
2. Sequential Chains
Sequential Chains are simple chains only but connecting three or more than three steps. For example if I want to generate a paragraph on a topic and then want to summarize it in next step then you have to invoke model twice and this process includes multiple steps. 
3. Parallel Chains
Parallel chains are those chains which are used when we have to deal with multiple models. Suppose I want to build a application which takes a pdf and then I can ask model to make notes of certain topics and also generate a small quiz on that topic. For generating the notes I will use Chat gpt and for generating the quiz I will use anthropic and then I will combine this outputs with the help of another model and finally we will get our final result (notes+quiz).
4. Conditional Chains
Conditional chains is used when for different conditions we have different output respectively. For example If I want to build a system in which if I get a positive feedback from user then I will send them a thank you email and if I get a negative feedback then I will send them a detailed feedback form asking them what is the issue behind negative feedback. 
"""
result = chain.invoke({'text': text })

print(result)
 