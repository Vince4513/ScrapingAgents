# To know more about the Task class, visit: https://docs.crewai.com/concepts/tasks
from crewai import Task
from textwrap import dedent

"""
Creating Tasks Cheat Sheet:
- Begin with the end in mind. Identify the specific outcome your tasks are aiming to achieve.
- Break down the outcome into actionable tasks, assigning each task to the appropriate agent.
- Ensure tashs are descriptive, providing clear instructions and expected deliverables.

Goal:
- Retrieve specific data from a website by avoiding or bypassing anti-scraping techniques.

Key Steps for Task Creation:
1. Identify the Desired Outcome: Define what success looks like for your project.
    - A csv file with the correct data

2. Task Breakdown: Divide the goal into smaller, manageable tasks that agents can execute.
    - Data Formatting: Verify the file is either json or csv and contains the data we asked for.
    - Data Scraping: Analyze the website and retrieve the data we are looking for.
    - Data Regulations: Determine if the data we are scraping is authorized or not and why.

3. Assign Tasks to Agents: Match tasks with agents based on their roles and expertise.

4. Task Description Template:
    - Use this template as a guide to define each task in your CrewAI application.
    - This template helps ensure that each task is clearly defined, actionable, and aligned with the specific goals of ...

    Template:
    ---------
    def [task_name](self, agent, [parameters]):
        return Task(description=dedent(f'''
        **Task**: [Provide a concise name or summary of the task.]
        **Description**: [Detailled description of what the agent is expected to do, including actionable steps and expectations....]

        **Parameters**: 
        - [Parameter 1]: [Description]
        - [Parameter 2]: [Description]
        ... [Add more parameters as needed.]

        **Note**: [Optional section for incentives or encouragement for high-quality work. This can include tips, addit......]

        '''), 
        expected_output="",
        agent=agent)
"""

class ScrapingTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def data_formatting(self, agent, url, interests, output_type):
        return Task(
            description=dedent(
                f"""
            **Task**: Data Formatting
            **Description**: You must ensure that the provided dataset is in the correct file format and structure. 
                It should first verify whether the dataset is in an accepted format such as CSV, JSON, XLSX, or Parquet. 
                If the file is in an unsupported format, you should attempt to convert it or notify the user about the 
                issue. Next, it must check for data integrity by confirming that the dataset is neither empty nor 
                corrupted. If applicable, checksum validation should be performed to detect any file corruption.

            Once the file is confirmed to be intact, you should validate its schema and structure by comparing the 
                dataset's columns against an expected schema. This includes ensuring that required fields are present, 
                data types are correct, and column names are consistent. Any missing, extra, or mislabeled columns should 
                be reported, and you should check that encoding (such as UTF-8) and delimiters are used consistently.

            Beyond structural validation, you must assess the authenticity of the data. It should identify the data source 
                using metadata, headers, or source logs and cross-check sample values against known references to confirm 
                legitimacy. Detecting synthetic or anomalous data is also crucial, and this can be achieved by performing 
                statistical analysis to flag outliers, duplicates, or improbable values.

            Finally, you should generate a validation report summarizing detected issues, suggested fixes, and recommendations. 
                If no issues are found, you should confirm that the dataset is correctly formatted and ready for further 
                processing. 
                
            **Parameters**: 
            - URL: {url}
            - Data : {interests}
            - File extension : {output_type}
            
            **Note**: {self.__tip_section()}

            """
            ),
            expected_output="",
            agent=agent,
        )

    def data_scraping(self, agent, url, interests, output_type):
        return Task(
            description=dedent(
                f'''
            **Task**: Data Scraping
            **Description**: You must extract data from a specified web source or API while ensuring that the 
                process is efficient, structured, and compliant with best practices. The first step is to 
                identify the target data source, determining whether the information is available through the  
                website home page url. If scraping a website, you should extract relevant URLs, identify page 
                structures, and locate the necessary data elements. If using an API, you must check documentation 
                for available endpoints, authentication requirements, and rate limits.

            Once the source is identified, you should establish an appropriate scraping method. For websites, 
                it can use HTML parsing tools such as BeautifulSoup or Selenium to navigate pages and extract 
                structured data. CSS or XPath selectors should be implemented to ensure precise extraction. If 
                the target is an API, you should construct well-formed HTTP requests with the appropriate headers, 
                such as User-Agent and Authorization, to interact with the server efficiently.

            You must then ensure that the scraping process is both efficient and compliant. It should check the 
                site's robots.txt file and terms of service for any scraping restrictions. To avoid getting blocked, 
                you should implement request throttling, retries for failed requests, and, if needed, proxy rotation 
                to distribute the request load. It should also consider caching results to reduce redundant queries 
                and improve efficiency.

            Once the data is extracted, you must process and structure it properly. This involves cleaning and 
                normalizing the data, handling encoding issues, and storing the results in a structured format such 
                as CSV, JSON, or a database. The extracted values should also be validated to ensure they match expected 
                patterns, such as numeric fields for prices, valid date formats, or unique identifiers.

            Finally, you should generate an output report summarizing the results. This should include the structured 
                dataset, logs of any errors encountered, and a list of pages or API calls that could not be processed. 
                Potential challenges include dealing with anti-scraping mechanisms such as CAPTCHAs, dynamically loaded 
                content, or IP bans. Additionally, you must balance data freshness with scraping frequency while ensuring 
                compliance with legal and ethical scraping guidelines.

            **Parameters**: 
            - URL: {url}
            - Data: {interests}
            - File extension : {output_type}

            **Note**: {self.__tip_section()}

            '''), 
            expected_output="",
            agent=agent,
        )

    def gather_legal_info(self, agent, url, interests):
        return Task(
            description=dedent(
                f'''
            **Task**: Gather Legal Information
            **Description**: Before initiating a scraping operation, you must assess whether 
                the targeted data is legally accessible. The first step is to determine data ownership and 
                access restrictions by identifying whether the data is publicly available, hidden behind 
                authentication barriers, or paywalled. you should verify whether the data belongs to 
                an entity that explicitly forbids scraping, either through technical measures or legal policies.
            
            To ensure compliance, you must review the website's legal documents, including its robots.txt 
                file, Terms of Service (ToS), and Privacy Policy. By analyzing these documents, you should 
                identify clauses that prohibit automated data extraction, highlight any intellectual property 
                claims, and determine whether the site imposes restrictions on automated access. If specific 
                limitations exist, you should document them and provide references to the relevant legal 
                sections.
            
            Beyond website-specific policies, you must also consider broader legal frameworks that regulate 
                data scraping. It should check for compliance with laws such as the General Data Protection 
                Regulation (GDPR) in the EU, which governs the handling and consent of user data, the California 
                Consumer Privacy Act (CCPA) in the U.S., which defines user data rights and obligations, and the 
                Digital Millennium Copyright Act (DMCA), which protects against unauthorized use of copyrighted 
                materials. Additionally, in cases where structured databases are being scraped, you should 
                evaluate potential conflicts with database protection laws in various jurisdictions.
            
            After gathering all relevant legal information, you should generate a legal summary report 
                outlining whether scraping is permissible. If the operation is restricted, the report should clearly 
                explain the reasons why, referencing specific regulations or website policies. In such cases, you 
                should also suggest alternative approaches, such as using an official API or obtaining explicit 
                permission from the data provider.

            **Parameters**: 
            - URL: {url}
            - Data: {interests}

            **Note**: {self.__tip_section()}

            '''), 
            expected_output="",
            agent=agent
        )