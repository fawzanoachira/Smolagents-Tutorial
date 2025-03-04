from smolagents import CodeAgent, E2BSandbox

agent = CodeAgent(
    tools=[],
    model=model,
    sandbox=E2BSandbox(),
    additional_authorized_imports=["numpy"]
)