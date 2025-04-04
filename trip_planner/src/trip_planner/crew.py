from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from trip_planner.tools.browser_tools import fetch_html
from trip_planner.tools.calculator_tools import calculate_travel_cost


@CrewBase
class TripPlanner():
	"""TripPlanner crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	search_tool = SerperDevTool()
	browser_tool = fetch_html
	calculator_tool = calculate_travel_cost


	@agent
	def city_selection_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['city_selector'],
			tools=[self.search_tool,self.browser_tool],
			verbose=True
		)

	@agent
	def local_expert(self) -> Agent:
		return Agent(
			config=self.agents_config['local_expert'],
			tools=[self.search_tool, self.browser_tool],
			verbose=True
		)
	
	@agent
	def travel_concierge(self) -> Agent:
		return Agent(
			config=self.agents_config['travel_concierge'],
			tools=[self.search_tool, self.browser_tool, self.calculator_tool],
			verbose=True
		)


	@task
	def identify_task(self) -> Task:
		return Task(
			config=self.tasks_config['identify_task'],
			agent=self.city_selection_agent(),
		)
	
	@task
	def gather_task(self) -> Task:
		return Task(
			config=self.tasks_config['gather_task'],
			agent=self.local_expert(),
		)

	@task
	def plan_task(self) -> Task:
		return Task(
			config=self.tasks_config['plan_task'],
			agent=self.travel_concierge(),
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the TripPlanner crew"""


		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
