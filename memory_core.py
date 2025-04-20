import json

class MemoryCore:
    def __init__(self, memory_file="memory.json"):
        self.memory_file = memory_file
        self.load_memory()

    def load_memory(self):
        try:
            with open(self.memory_file, "r") as file:
                self.memory = json.load(file)
        except FileNotFoundError:
            self.memory = {}

    def save_memory(self):
        with open(self.memory_file, "w") as file:
            json.dump(self.memory, file)

    def remember(self, key, value):
        self.memory[key] = value
        self.save_memory()

    def recall(self, key):
        return self.memory.get(key, None)
