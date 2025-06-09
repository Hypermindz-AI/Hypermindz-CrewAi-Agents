from crewai import Agent, Task, Crew, Process, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from hypermindz_tools.crewai import hypermindz_rag_search


@CrewBase
class DatasetFinder():
    """DatasetFinder crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def curator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['curator_agent'],
            tools=[hypermindz_rag_search],
            llm=LLM(model="gpt-4o", temperature=0),
            verbose=True
        )

    @task
    def dataset_query_task(self) -> Task:
        return Task(
            config=self.tasks_config['dataset_query_task'], 
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:

        return Crew(
            agents=self.agents, 
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )

