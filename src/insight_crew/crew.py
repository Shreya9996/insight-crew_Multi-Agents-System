from crewai import Agent, Crew, Process, Task,LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from insight_crew.tools.web_search_tool import web_search_tool



llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
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
    def data_analyst_agent(self) ->Agent:
        return Agent(
            config = self.agents_config["data_analyst_agent"],
            llm = llm ,
            verbose = True
        )
    @agent
    def report_agent(self)-> Agent:
        return Agent(
            config = self.agents_config["report_agent"],
            llm = llm,
            verbose = True
        )

    @task
    def research_task(self)->Task:
        return Task(
            config=self.tasks_config["research_task"],
            agent = self.research_agent()

        )
    @task
    def data_analysis_task(self)->Task:
        return Task(
            config=self.tasks_config["data_analysis_task"],
            agent=self.data_analyst_agent()
        )

    @task
    def report_task(self) -> Task:
        return Task(
            config=self.tasks_config["report_task"],
            agent = self.report_agent(),
            output_file="outpu/output.md"
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
