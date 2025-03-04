from smolagents import ToolCallingAgent

agent = ToolCallingAgent(
    tools=[custom_tool],
    model=model,
    max_steps=5,
    name="tool_agent",
    description="Executes specific tools based on input"
)