# learning_mouse.py
import random

directions = ["left", "right"]
rewards = {"left": -1, "right": 1}  # left is a trap, right is cheese

class LearningMouse:
    def __init__(self):
        self.knowledge = {"left": 0, "right": 0}  # mouse knowledge about directions

    def choose_direction(self):
        return max(self.knowledge, key=self.knowledge.get)  # choose direction with highest knowledge

    def explore(self):
        return random.choice(directions) # randomly choose a direction

    def learn(self, direction, reward):
        self.knowledge[direction] += reward # update knowledge based on reward

mouse = LearningMouse()

# Simulate learning over 10 tries
for i in range(10):
    if random.random() < 0.3:
        choice = mouse.explore()
    else:
        choice = mouse.choose_direction()

    reward = rewards[choice]
    mouse.learn(choice, reward)
    print(f"Try {i+1}: Mouse went {choice}, got reward {reward}")
    print(f"Knowledge: {mouse.knowledge}")
