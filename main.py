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
    def __init__(self, url, interests):
        self.url = url
        self.interests = interests

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = ScrapingAgents()
        tasks = ScrapingTasks()

        # Define your custom agents and tasks here
        expert_data_manager = agents.expert_data_manager()
        data_engineer_expert = agents.data_engineer_expert()
        data_governance_expert = agents.data_governance_expert()

        # Custom tasks include agent name and variables as input
        check_conformity = tasks.check_conformity(
            expert_data_manager,
            self.interests
        )

        scrape_website = tasks.scrape_website(
            data_engineer_expert,
            self.url,
            self.interests
        )

        gather_legal_info = tasks.gather_legal_info(
            data_governance_expert,
            self.url,
            self.interests
        )

        # Define your custom crew here
        crew = Crew(
            agents=[
                expert_data_manager, 
                data_engineer_expert, 
                data_governance_expert
            ],
            tasks=[
                check_conformity, 
                scrape_website, 
                gather_legal_info
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
    scraping_crew = ScrapingCrew(url, interests)
    result = scraping_crew.run()
    print("\n\n########################")
    print("## Here is you scraped data crew run result:")
    print("########################\n")
    print(result)
