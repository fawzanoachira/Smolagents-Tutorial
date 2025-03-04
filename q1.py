# Create a CodeAgent with DuckDuckGo search capability
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],           # Add search tool here
    model=HfApiModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct")        # Add model here
)