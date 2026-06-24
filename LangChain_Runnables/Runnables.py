import random, warnings
from abc import ABC, abstractmethod

class Runnable(ABC):
    def invoke(input_data):
        pass

class FakeLLM(Runnable):
    def __init__(self):
        print('LLM created.')

    def invoke(self, prompt):
        response_list = [
            "Delhi is the capital of India.",
            "IPL is a cricket league.",
            "AI stands for Artificial Intelligence.",
            "Generative AI is an emerging field.",
            "Langchain is a beautiful framework.", 
            "Diffrent prompts gives different outputs."
        ]

        return {"response": random.choice(response_list)}

    def predict(self, prompt):
        warnings.warn(
            "The 'predict()' method is deprecated and will be removed in a future release. "
            "Use 'invoke()' instead.",
            DeprecationWarning,
            stacklevel=2
        )

        response_list = [
            "Delhi is the capital of India.",
            "IPL is a cricket league.",
            "AI stands for Artificial Intelligence.",
            "Generative AI is an emerging field.",
            "LangChain is a beautiful framework.",
            "Different prompts give different outputs."
        ]
        return {"response": random.choice(response_list)}

class FakePromptTemplate(Runnable):
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def invoke(self, input_dict):
        return self.template.format(**input_dict)   

    def format(self, input_dict):
        warnings.warn(
            "The 'formatt()' method is deprecated and will be removed in a future release. "
            "Use 'invoke()' instead.",
            DeprecationWarning,
            stacklevel=2
        )
        return self.template.format(**input_dict)

class FakeStrOutputParser(Runnable):
    def __init__(self):
        pass
    def invoke(self, input_data):
        return input_data["response"]

class RunnableConnector(Runnable):
    def __init__(self, runnable_list):
        self.runnable_list = runnable_list
    
    def invoke(self, input_data):
        for runnable in self.runnable_list:
            input_data = runnable.invoke(input_data)
        return input_data

# template = FakePromptTemplate(
#     template = "Tell me a random fact about {topic}.",
#     input_variables = ["topic"]
# )

# llm = FakeLLM()
# parser = FakeStrOutputParser()
# chain = RunnableConnector([template, llm, parser])
# result = chain.invoke({"topic": "AI"})
# print(result)

template1 = FakePromptTemplate(
    template = "Write a joke about {topic}.",
    input_variables = ["topic"]
)

template2 = FakePromptTemplate(
    template = "Explain the following joke {response}.",
    input_variables = ["response"]
)

llm = FakeLLM()
parser = FakeStrOutputParser()
chain1 = RunnableConnector([template1, llm])
chain2 = RunnableConnector([template2, llm, parser])
final_chain = RunnableConnector([chain1, chain2])
result = final_chain.invoke({"topic": "AI"})
print(result)