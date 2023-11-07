import tkinter as tk
from tkinter import messagebox

class TextAdventureGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Adventure Game")

        self.current_room = None

        self.create_rooms()
        self.create_widgets()

    def create_rooms(self):
        # Define rooms and their connections
        self.rooms = {
            "start": {
                "name": "Start Room",
                "description": "You are in the starting room.",
                "exits": {"east": "kitchen", "west": "living_room"},
                "items": ["key"],
            },
            "kitchen": {
                "name": "Kitchen",
                "description": "You are in the kitchen.",
                "exits": {"west": "start"},
                "items": ["knife"],
            },
            "living_room": {
                "name": "Living Room",
                "description": "You are in the living room.",
                "exits": {"east": "start"},
                "items": [],
            },
        }

    def create_widgets(self):
        self.description_label = tk.Label(
            self.root, text="Welcome to the Text Adventure Game!"
        )
        self.description_label.pack()

        self.input_entry = tk.Entry(self.root)
        self.input_entry.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.process_input)
        self.submit_button.pack()

        self.command_history = tk.Text(self.root, width=40, height=10)
        self.command_history.pack()

        self.move("start")

    def move(self, room_name):
        self.current_room = room_name
        room = self.rooms[room_name]
        description = room["description"]
        items = room["items"]
        self.description_label.config(text=description)
        self.command_history.insert("1.0", f"You are in the {room['name']}.\n")
        self.command_history.insert("1.0", description + "\n")
        if items:
            self.command_history.insert("1.0", "You see: " + ", ".join(items) + "\n")

    def process_input(self):
        command = self.input_entry.get()
        self.command_history.insert("1.0", "> " + command + "\n")
        self.input_entry.delete(0, "end")

        if command.lower() == "quit":
            self.root.destroy()
        elif command.lower() == "help":
            self.command_history.insert("1.0", "Available commands: quit, help, look\n")
        elif command.lower() == "look":
            self.move(self.current_room)
        else:
            self.command_history.insert("1.0", "I don't understand that command.\n")

if __name__ == "__main__":
    root = tk.Tk()
    game = TextAdventureGame(root)
    root.mainloop()