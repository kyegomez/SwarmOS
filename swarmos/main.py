import os

from dotenv import load_dotenv

# Import the OpenAIChat model and the Agent struct
from swarms import Agent, ChromaDB, OpenAIChat, tool

# Load the environment variables
load_dotenv()


# Memory
memory = ChromaDB()


# Define a tool
@tool
def search_api(query: str, description: str):
    """Search the web for the query

    Args:
        query (str): _description_

    Returns:
        _type_: _description_
    """
    return f"Search results for {query}"


@tool
def terminal_api(
    query: str,
):
    """_summary_

    Args:
        query (str): _description_
    """
    print(f"Getting the weather for {query}")


# Get the API key from the environment
api_key = os.environ.get("OPENAI_API_KEY")

# Initialize the language model
llm = OpenAIChat(
    temperature=0.5,
    openai_api_key=api_key,
)


## Initialize the workflow
agent = Agent(
    agent_name="SwarmOS-Worker",
    agent_description=(
        "A worker agent for SwarmOS, the LLM-based Operating System."
    ),
    llm=llm,
    max_loops="auto",
    dashboard=True,
    tools=[search_api, terminal_api],
    long_term_memory=ChromaDB(),
)

# Run the workflow on a task
out = agent.run("Generate a 10,000 word blog on health and wellness.")
print(out)
