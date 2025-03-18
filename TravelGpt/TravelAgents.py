from crewai import agent
from travelTools import search_web_tool
from crewai import LLM
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

chatgpt_llm - ChatOpenAI(temperature=0.5, model="gpt-4o" , api_key=
OPENAI_API_KEY)

openai_llm = LLM(provider=chatgpt_llm)

guide_expert = Agent(
    role = "City Local Guide Expert",
    goal ="Providers information about the city,its attractions and the best places to visit",
    backstory = "A local expert Passionate about the city and its culture",
    tools=[search_web_tool],
    verbose=True,
    max_iter = 5,
    llm = openai_llm,
    allow_delegation = False,
)


location_expert = Agent(
    role = "Travel Trip Expert",
    goal ="Provide Travel logistics and essential for a trip",
    backstory = "A seasoned traveler with a knacks for planning trips",
    tools=[search_web_tool],
    verbose=True,
    max_iter = 5,
    llm = openai_llm,
    allow_delegation = False,
)



Planner_expert = Agent(
    role = "Travel Planning Expert ",
    goal ="Compiles a;; gathered information and Creates a detailed travel plan",
    backstory = "An Expert in planning trips and creating detailed itineraries",
    tools=[search_web_tool],
    verbose=True,
    max_iter = 5,
    llm = openai_llm,
    allow_delegation = False,
)
