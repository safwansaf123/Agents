class Agent:
    def __init__(self, name, default_behavior):
        self.name = name
        self.default_behavior = default_behavior

    def run(self, task, override_behavior=None):
        # Use the override if provided, else use the default
        behavior = override_behavior if override_behavior else self.default_behavior
        print(f"[{self.name}] ({behavior}) → Task: {task}")

# Create an agent with a default formal behavior
my_agent = Agent(name="HelperBot", default_behavior="formal")

# Run task 1 — uses default behavior
my_agent.run("Summarize this article.")

# Run task 2 — temporarily override behavior for a single run
my_agent.run("Tell me a joke about AI.", override_behavior="funny")

print(my_agent.default_behavior)
# Check the agent's behavior after running tasks