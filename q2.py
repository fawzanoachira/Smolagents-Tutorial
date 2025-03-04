from smolagents import ToolCallingAgent, CodeAgent, HfApiModel, DuckDuckGoSearchTool

# Create web agent and manager agent structure
web_agent = ToolCallingAgent(
    tools=[DuckDuckGoSearchTool(), visit_webpage],  # Add required tools
    model=model,  # Add model
    max_steps=10,  # Adjust steps
    name="web",  # Add name
    description="Browses the web to find information",  # Add description
)

manager_agent = CodeAgent(
    model=model,
    tools=[],
    additional_authorized_imports=["numpy", "time", "pandas"],
    managed_agents=[web_agent],
)
