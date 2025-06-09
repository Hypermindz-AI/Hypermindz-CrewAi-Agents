# Knowledge Example using Hypermindz Tool

Welcome to the Knowledge Example (using hypermindz tool) Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Getting Started with AgenticRegistry.ai

Before running this project, you need to obtain the required credentials and dataset configuration from AgenticRegistry.ai:

### Step 1: Visit AgenticRegistry.ai

Go to [agenticregistry.ai](https://agenticregistry.ai) and create an account if you don't have one.

### Step 2: Choose Your Dataset Option

You have two options:

#### Option A: Submit Your Own Dataset
1. Navigate to the dataset submission section
2. Upload your dataset files (CSV, JSON, or other supported formats)
3. Provide dataset metadata and description
4. Wait for processing and vectorization
5. Once processed, you'll receive your dataset credentials

#### Option B: Choose an Existing Dataset
1. Browse the available public datasets
2. Select a dataset that matches your use case
3. Subscribe or request access to the dataset
4. Obtain the dataset credentials

### Step 3: Get Your Credentials

After submitting or selecting a dataset, you'll receive:
- `HYPERMINDZ_RAG_API_KEY`: Your API authentication key
- `HYPERMINDZ_BASE_URL`: The base API endpoint URL
- `HYPERMINDZ_DATASET_ID`: Your specific dataset identifier

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```

## Configuration

### Step 1: Add Your API Keys to `.env` file

Create or modify the `.env` file in your project root and add the following:

```bash
# OpenAI API Key
OPENAI_API_KEY=your_openai_api_key_here

# Hypermindz RAG Configuration (from agenticregistry.ai)
HYPERMINDZ_RAG_API_KEY=your_rag_api_key_here
HYPERMINDZ_BASE_URL=https://api.agenticregistry.ai
HYPERMINDZ_DATASET_ID=your_dataset_id_here
```

### Step 2: Customize Your Crew

- Modify `src/dataset_finder/config/agents.yaml` to define your agents
- Modify `src/dataset_finder/config/tasks.yaml` to define your tasks
- Modify `src/dataset_finder/crew.py` to add your own logic, tools and specific args
- Modify `src/dataset_finder/main.py` to add custom inputs for your agents and tasks

## How the Hypermindz Tool Works

The Hypermindz RAG Search Tool performs semantic similarity searches over your vectorized dataset. When you make a query:

1. Your natural language query is sent to the AgenticRegistry.ai API
2. The API performs vector similarity matching within your specified dataset
3. The most contextually relevant entries are returned
4. Your CrewAI agents can then use this information for their tasks

### Example API Request Format:
```
GET https://api.agenticregistry.ai/search?query=your_search_query&id=your_dataset_id
Authorization: Bearer your_api_key
```

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the dataset_finder Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder, enhanced with data from your selected dataset via the Hypermindz RAG search tool.

## Understanding Your Crew

The dataset_finder Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

### Key Features:
- **Semantic Search**: Agents can search through your vectorized dataset using natural language queries
- **Contextual Retrieval**: Get the most relevant information based on semantic similarity
- **Multi-Agent Collaboration**: Agents work together, sharing insights from the dataset
- **Flexible Dataset Integration**: Works with any dataset uploaded to AgenticRegistry.ai

## Example Usage

Here's how your agents might use the Hypermindz tool:

```python
# In your agent's task
from hypermindz_tools.crewai import hypermindz_rag_search

# Agent searches for relevant information
result = hypermindz_rag_search("Find research papers about machine learning optimization")

# Agent uses the results for further analysis
# The results will be contextually relevant to your specific dataset
```

## Troubleshooting

### Common Issues:

1. **API Key Issues**: Ensure your `HYPERMINDZ_RAG_API_KEY` is correctly set in the `.env` file
2. **Dataset Not Found**: Verify your `HYPERMINDZ_DATASET_ID` matches the ID from AgenticRegistry.ai
3. **Network Issues**: Check that `HYPERMINDZ_BASE_URL` is accessible from your network

### Getting Help:

If you encounter issues with your dataset or API credentials:
1. Check your AgenticRegistry.ai dashboard
2. Verify your dataset is fully processed and vectorized
3. Ensure your API key has the correct permissions

## Support

For support, questions, or feedback regarding the Knowledge Example Crew or crewAI:
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

For AgenticRegistry.ai related issues:
- Visit [agenticregistry.ai](https://agenticregistry.ai) support section
- Check the platform documentation for dataset management

Let's create wonders together with the power and simplicity of crewAI enhanced by intelligent dataset search capabilities!