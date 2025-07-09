# simple coding agent that can respond to simple questions


class ChatAgent:
    def __init__(self, name="GPT"):
        self.name = name

    def respond(self, message):
        # Simplified responses like a mini ChatGPT
        if "hello" in message.lower():
            return "Hi! How can I help you today?"
        elif "weather" in message.lower():
            return "The weather is sunny with a slight chance of rain."
        elif "bye" in message.lower():
            return "Goodbye! Have a nice day."
        else:
            return "I'm not sure how to respond to that."
        
Agent1 = ChatAgent.respond

print(Agent1(ChatAgent(), "Hello, how are you?"))   # one question one answer
print(Agent1(ChatAgent(), "What's the weather like?"))
print(Agent1(ChatAgent(), "Bye!"))
print(Agent1(ChatAgent(), "Tell me a joke!"))