from crewai import Agent, Crew, Process, Task,LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from insight_crew.tools.web_search_tool import web_search_tool
import os
from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY missing. Check the .env file."
    )

llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=api_key,
    temperature=0.2,
)



@CrewBase
class Researh_and_Insight_agent():

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    agents : list[BaseAgent]
    tasks : list[Task]

    @agent
    def research_agent(self)->Agent:
        return Agent(
            config = self.agents_config["research_agent"],
            tools = [web_search_tool],
            llm = llm ,
            verbose = True
        )
    
    @agent
    def competitor_agent(self) -> Agent:
        return Agent(
            config = self.agents_config["competitor_agent"],
            tools = [web_search_tool],
            llm = llm,
            verbose = True
        )


    @agent
    def data_analyst_agent(self) ->Agent:
        return Agent(
            config = self.agents_config["data_analyst_agent"],
            llm = llm ,
            verbose = True
        )

    @agent
    def fact_checker_agent(self) -> Agent:
        return Agent(
            config = self.agents_config["fact_checker_agent"],
            tools = [web_search_tool],
            llm = llm,
            verbose = True
        )

    @agent
    def decision_agent(self) -> Agent:
        return Agent(
            config = self.agents_config["decision_agent"],
            llm = llm,
            verbose = True
        )
    
    
    @agent
    def report_agent(self)-> Agent:
        return Agent(
            config = self.agents_config["report_agent"],
            llm = llm,
            verbose = True
        )


# =================================TASK======================================================



    @task
    def research_task(self)->Task:
        return Task(
            config=self.tasks_config["research_task"],
            agent = self.research_agent()

        )

    @task
    def competitor_analysis_task(self) -> Task:
        return Task(
            config = self.tasks_config["competitor_analysis_task"],
            agent = self.competitor_agent(),
            context=[self.research_task()]
        )


    @task
    def data_analysis_task(self)->Task:
        return Task(
            config=self.tasks_config["data_analysis_task"],
            agent=self.data_analyst_agent(),
            context=[self.research_task(),self.competitor_analysis_task()]
        )

    @task
    def fact_checking_task(self) -> Task:
        return Task(
            config = self.tasks_config["fact_checking_task"],
            agent = self.fact_checker_agent(),
            context=[self.research_task(),self.competitor_analysis_task(),self.data_analysis_task()]
        )

    @task
    def decision_task(self) -> Task:
        return Task(
            config = self.tasks_config["decision_task"],
            agent = self.decision_agent(),
            context=[self.research_task(),self.competitor_analysis_task(),self.data_analysis_task(),self.fact_checking_task()]
        )

    

    @task
    def report_task(self) -> Task:
        return Task(
            config=self.tasks_config["report_task"],
            agent = self.report_agent(),
            context=[self.research_task(),self.competitor_analysis_task(),
                     self.data_analysis_task(),self.fact_checking_task(),self.decision_task()],

            output_file="output/output.md"
        )


    @crew
    def crew(self) -> Crew:
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process=Process.sequential,
            llm = llm,
            verbose=True
        )
