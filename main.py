# Source du tutoriel
# https://www.youtube.com/watch?v=sPzc6hMg7So&list=PLpkzjZ2JCjKLCwoAs6i2AsX69Y5vc-g20&index=4

from crewai import Crew
from textwrap import dedent
from agents import ScrapingAgents
from tasks import ScrapingTasks

from dotenv import load_dotenv
load_dotenv(override=True) # Load environment variables

# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class ScrapingCrew:
    def __init__(self, url, interests, output_type):
        self.url = url
        self.interests = interests
        self.output_type = output_type

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = ScrapingAgents()
        tasks = ScrapingTasks()

        # Define your custom agents and tasks here
        data_governance_expert = agents.data_governance_expert()
        data_engineer_expert = agents.data_engineer_expert()
        expert_data_manager = agents.expert_data_manager()

        # Custom tasks include agent name and variables as input
        gather_legal_info = tasks.gather_legal_info(
            data_governance_expert,
            self.url,
            self.interests
        )

        data_scraping = tasks.data_scraping(
            data_engineer_expert,
            self.url,
            self.interests,
            self.output_type
        )

        data_formatting = tasks.data_formatting(
            expert_data_manager,
            self.url,
            self.interests,
            self.output_type
        )

        # Define your custom crew here
        crew = Crew(
            agents=[
                data_governance_expert, 
                data_engineer_expert, 
                expert_data_manager
            ],
            tasks=[
                gather_legal_info, 
                data_scraping, 
                data_formatting
            ],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    
    print("## Welcome to Scraping Crew")
    print("-------------------------------")
    url = input(
        dedent("""
        What is the url of the web page to scrape data from?
        """))
    interests = input(
        dedent("""
        What do you wanna scrape on the web page?
        """))
    output_type = input(
        dedent("""
        Do you prefer a CSV or a JSON file?
        """))
    scraping_crew = ScrapingCrew(url, interests, output_type)
    result = scraping_crew.run()
    print("\n\n########################")
    print("## Here is you scraped data crew run result:")
    print("########################\n")
    print(result)
