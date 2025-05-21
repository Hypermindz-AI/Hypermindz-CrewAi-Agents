from crewai import Agent, Task, Crew, Process, LLM
from knowledge.dataset_knowledge_source import DatasetKnowledgeSource
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


dataset_knowledge = DatasetKnowledgeSource(file_path="all-datasets.json")

@CrewBase
class DatasetFinder():
    """DatasetFinder crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def curator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['curator_agent'],
            knowledge_sources=[dataset_knowledge],
            llm=LLM(model="gpt-4", temperature=0),
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
            verbose=True,
            knowledge_sources=[dataset_knowledge]
        )

