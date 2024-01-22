import google.generativeai as genai
from gemini_api import gemini_api_key
from vertexai.preview.generative_models import (Content, FunctionDeclaration, GenerativeModel, Part, Tool)
import vertexai

vertexai.init(project="buildforbharat")

genai.configure(api_key=gemini_api_key)

# Documentation code
model = GenerativeModel("gemini-pro")

def get_current_weather(location):
    print("Location: ", location)
    
get_current_weather_func = FunctionDeclaration(
    name="get_current_weather",
    description="Get the current weather in a given location",
    parameters={
        "type": "object",
        "properties": {"location": {"type": "string", "description": "Location"}},
    },
)

weather_tool = Tool(
    function_declarations=[get_current_weather_func],
)

prompt = "What is the weather like in Boston?"

response = model.generate_content(
    prompt,
    generation_config={"temperature": 0},
    tools=[weather_tool],
)
print(response)

""" Functions for our use case
# Review product function
def review_product(order_id, rating, feedback):
    print("Order id: ", order_id)
    print("Rating: ", rating)
    print("Feedback: ", feedback)

tools = Tool(
    function_declarations=[
        FunctionDeclaration(name = "review_product",
                            description="Review product with given order id",
                            parameters={
                                "type": "object",
                                "properties": {
                                    "order_id": {"type": "string", "description": "Order id of the product"},
                                    "rating": {"type": "number", "description": "Rating of the product"},
                                    "feedback": {"type": "string", "description": "Feedback of the product"}
                                }
                            })])

model = GenerativeModel("gemini-pro", tools=[tools])
chat = model.start_chat()
response = chat.send_message("I liked the last order with order id 1234 and rate it 3.7 stars and the product met my expectations")
print(response.text) """


""" Basic Gemini api implementation
# Configuration
from gemini_api import gemini_api_key
genai.configure(api_key=gemini_api_key)
generation_config = {"temperature":0.9, "top_p": 1, "top_k": 1, "max_output_tokens": 2048}

# Initialization of the model
model = genai.GenerativeModel("gemini-pro", generation_config=generation_config)

# Generate content
response = model.generate_content(["Write a poem about gemini ai"])

print(response.text) """

"""Straming
response = model.generate_content(["Write a poem about gemini ai"], stream=True)

for part in response:
    print(part.text, end="", flush=True)"""
