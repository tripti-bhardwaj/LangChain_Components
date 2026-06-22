from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field
load_dotenv()

model = ChatOpenAI()

class Review(BaseModel):
    I
    key_themes: list[str] = Field(description = "Write down all the key themes discussed in the review in a list")
    summary: Annotated[str, "A brief summary of the review."]
    sentiment: Annotated[Literal["pos", "neg"], "Return sentiment of the review either negative or positive."]
    pros: Optional[list[str]] = Field(default = None, description = "Write down all the pros inside a list.")
    cons: Optional[list[str]] = Field(default = None, description = "Write down all the cons inside a list.")

structured_model = model.with_structured_output(Review)

result = model.invoke("""The hardware is great, but the software feels bloated. There are
too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to 
other brands. Hoping for a software update to fix this.""")

print(result.sentiment)