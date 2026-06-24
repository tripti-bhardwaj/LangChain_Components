import random

class FakeLLM:
    def __init__(self):
        print('LLM created.')
    
    def predict(self, prompt):
        response_list = [
            "Delhi is the capital of India.",
            "IPL is a cricket league.",
            "AI stands for Artificial Intelligence.",
            "Generative AI is an emerging field.",
            "Langchain is a beautiful framework.", 
            "Diffrent prompts gives different outputs."
        ]

        return {"response": random.choice(response_list)}
    
class FakePromptTemplate:
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def format(self, input_dict):
        return self.template.format(**input_dict)

class FakeLLMChain:
    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt
    
    def run(self, input_dict):
        final_prompt = self.prompt.format(input_dict)
        result = self.llm.predict(final_prompt)

        return result["response"]

template = FakePromptTemplate(
    template = "Tell me a random fact about {topic}.",
    input_variables = ["topic"]
)

llm = FakeLLM()

chain = FakeLLMChain(llm, template)

result = chain.run({"topic": "AI"})
    
print(result)