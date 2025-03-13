from crewai import Agent
from textwrap import dedent
from langchain_community.llms import OpenAI
from langchain_ollama import OllamaLLM
from langchain_openai import ChatOpenAI

from langchain_apify import ApifyActorsTool
from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools

'''
Creating Agents Cheat Sheet:
- Think like a boss. Work backwards from the goal and think which employee
    you need to hire to get the job done.
- Define the Captain of the crew who orient the other agents towards the goal.
- Define which experts the captain needs to communicate with and delegate tasks to.
    Build a top down structure of the crew.

Goal:
- Scrape data from a specific website and give us a csv or json file aggregating 
    all this data.

Captain/Manager/Boss:
- Expert Data Manager (Manage web scraping process)

Employee/Experts to hire:
- Data Engineer Expert (How to scrape)
- Data Governance Expert (What to scrape)

Notes:
- Agents should be results driven and have a clear goal in mind
- Role is their job title
- Goals should be actionable
- Backstory should be their resume
'''

# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class ScrapingAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(name="gpt-4", temperature=0.7)
        # self.Ollama = OllamaLLM(model="openhermes")

    def expert_data_manager(self):  
        return Agent(
            role="Expert Data Manager",
            backstory=dedent(f"""Expert in computer science projects.
                             I have decades of experience making IT projects successful."""),
            goal=dedent(f"""
                        Create a structured csv or json file with the data extracted from the website. 
                        We should not have duplicates or empty rows. 
                        """),
            tools=[
                SearchTools.search_the_internet
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def data_engineer_expert(self):
        return Agent(
            role="Data Engineer Expert",
            backstory=dedent(f"""Expert at scraping data ovr the web"""),
            goal=dedent(f"""Parse the web page based on client interests"""),
            tools=[
                SearchTools.search_the_internet,
                ApifyActorsTool("apify/rag-web-browser")
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
    
    def data_governance_expert(self):
        return Agent(
            role="Data Governance Expert",
            backstory=dedent(f"""Knowledgeable data governance expert with extensive information 
                             about the rules about laws like GDPR"""),
            goal=dedent(f"""Provide the BEST insights about the data the client is interested in."""),
            tools=[
                SearchTools.search_the_internet
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
