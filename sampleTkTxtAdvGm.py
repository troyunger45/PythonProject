import tkinter as tk
from tkinter import Menu

class TextAdventureGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Adventure Game")
        self.story_text = tk.Text(root, wrap=tk.WORD, width=40, height=10)
        self.story_text.pack()
        self.current_story = 0
        self.initialize_story()

        menu = Menu(root)
        root.config(menu=menu)
        file_menu = Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Game", command=self.initialize_story)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)

    def initialize_story(self):
        self.current_story = 0
        self.story_text.delete("1.0", tk.END)
        self.show_story_text(self.current_story)

    def show_story_text(self, story_number):
        story = self.stories[story_number]
        self.story_text.insert(tk.END, story['text'] + '\n\n')

        for i, choice in enumerate(story['choices'], 1):
            self.story_text.insert(tk.END, f"{i}. {choice}\n")

        self.story_text.insert(tk.END, "\n")
        self.story_text.bind("<KeyPress-Return>", self.handle_choice)

    def handle_choice(self, event):
        user_input = event.widget.get("end-2c", tk.END)
        try:
            choice = int(user_input)
            if choice > 0 and choice <= len(self.stories[self.current_story]['choices']):
                self.story_text.delete("1.0", tk.END)
                self.current_story = self.stories[self.current_story]['next'][choice - 1]
                self.show_story_text(self.current_story)
        except ValueError:
            pass

    stories = [
        {
            'text': "You are in a dark room. What do you do?",
            'choices': ["Turn on the light", "Open the door"],
            'next': [1, 2]
        },
        {
            'text': "You turned on the light. It's a small room with a table and a chair. What do you do?",
            'choices': ["Examine the table", "Sit on the chair"],
            'next': [3, 4]
        },
        {
            'text': "You opened the door and found yourself in a garden. What do you do?",
            'choices': ["Explore the garden", "Go back inside"],
            'next': [5, 0]
        },
        {
            'text': "You examine the table and find a key. What do you do?",
            'choices': ["Take the key", "Leave it and sit on the chair"],
            'next': [6, 4]
        },
        {
            'text': "You sit on the chair, but nothing interesting happens.",
            'choices': ["Go back to the dark room"],
            'next': [0]
        },
        {
            'text': "You explore the garden and find a treasure chest. What do you do?",
            'choices': ["Open the chest", "Leave the garden"],
            'next': [7, 8]
        },
        {
            'text': "You take the key from the table. What do you do?",
            'choices': ["Use the key to open the door", "Go back to the garden"],
            'next': [2, 5]
        },
        {
            'text': "You open the chest and find a pile of gold. You win!",
            'choices': [],
            'next': []
        },
        {
            'text': "You leave the garden and go back inside.",
            'choices': ["Go back to the dark room"],
            'next': [0]
        },
    ]

if __name__ == "__main__":
    root = tk.Tk()
    game = TextAdventureGame(root)
    root.mainloop()
