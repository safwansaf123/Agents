# agent_vacuum.py
# Your robot vacuum moves room by room. If it sees dirt, it cleans. If not, it moves to the next room.

class VacuumAgent:
    def __init__(self):
        self.position = 0  # start at room 0

    def sense(self, room):
        return room[self.position]

    def act(self, room):
        if self.sense(room) == "dirty":
            room[self.position] = "clean"
            print(f"Cleaned room {self.position}")
        else:
            print(f"Room {self.position} already clean.")
            if self.position < len(room) - 1:
                self.position += 1

# Simulated 1D world: ["dirty", "clean", "dirty"]
rooms = ["dirty", "clean", "dirty"]
agent = VacuumAgent()

for _ in range(5):
    agent.act(rooms)
    print("Current room states:", rooms)
