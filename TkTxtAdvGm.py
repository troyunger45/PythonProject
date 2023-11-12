from tkinter import *

class Game:

    def __init__(self, menu):
        # Adds formatting for the menu window.
        self.menu = menu
        menu.title("Text Adventure Game!")
        menu.geometry('890x500')
        # Create the PhotoImage here.
        self.bg = PhotoImage(file="images/picture2.png")
        self.bg2 = PhotoImage(file="images/picture3.png")
        self.bg3 = PhotoImage(file="images/picture4.png")
        # Calls InsertMenuWidgets
        self.InsertMenuWidgets()
        # Defines class attributes.
        self.health = 0
        self.xp = 0
        self.name = ""
        self.turn = 0

    def InsertMenuWidgets(self):
        # Clear the menu window if it's not empty
        for widget in self.menu.winfo_children():
            widget.destroy()

        my_canvas = Canvas(self.menu, width=500, height=500)
        my_canvas.pack(fill="both", expand=True)
        my_canvas.create_image(0, 0, image=self.bg, anchor='nw')
        custom_fontLabel = ("Helvetica", 25, "bold")
        custom_fontButton = ("Helvetica", 10, "bold")
        my_canvas.create_text(250, 100, text="Welcome to Our\nText Adventure Game!", font=custom_fontLabel, fill="cyan", anchor="center")

        startButton = Button(self.menu, text="Start Game!", command=self.InsertGameWidgets, padx=53, pady=25, bg="navy", fg="cyan", font=custom_fontButton)
        descriptionButton = Button(self.menu, text="Game Description.", command=self.InsertDescriptionWidgets, padx=32, pady=25, bg="navy", fg="cyan", font=custom_fontButton)
        startButton_window = my_canvas.create_window(160, 250, anchor='nw', window=startButton)
        descriptionButton_window = my_canvas.create_window(160, 350, anchor='nw', window=descriptionButton)

    def InsertGameWidgets(self):
        # Clear the menu window if it's not empty
        for widget in self.menu.winfo_children():
            widget.destroy()

        my_canvas = Canvas(self.menu, width=500, height=500)
        my_canvas.pack(fill="both", expand=True)
        my_canvas.create_image(0, 0, image=self.bg2, anchor='nw')
        custom_font1 = ("Helvetica", 10, "bold")
        custom_font2 = ("Helvetica", 15, "bold")
        backButton = Button(self.menu, text="Exit game.", command=self.InsertMenuWidgets, padx=51.5, pady=25, fg="cyan", bg="navy", font=custom_font1)
        backButton_window = my_canvas.create_window(170, 370, anchor='nw', window=backButton)
        my_canvas.create_text(250, 70, text="Enter response here:", font=custom_font2, fill="navy", anchor="center")
        
        # Entry for user input
        user_input = Entry(self.menu, font=custom_font1, width=50,bg="cyan",fg="navy")
        user_input_window = my_canvas.create_window(80, 90, anchor='nw', window=user_input)

        # Button to display response
        response_button = Button(self.menu, text="Display response.", command=lambda: self.handle_response(user_input.get()), padx=31, pady=25, fg="cyan", bg="navy", font=custom_font1)
        response_button_window = my_canvas.create_window(170, 270, anchor='nw', window=response_button)

        # Text box
        self.text_box = Text(self.menu, width=50, height=7, wrap=WORD, font=custom_font1,bg="cyan",fg="navy")
        text_box_window = my_canvas.create_window(80, 130, anchor='nw', window=self.text_box)

        # Display initial scenario
        self.display_scenario("Welcome to the Text Adventure Game! What will you do next? explore or fight?")

    def display_scenario(self, scenario):
        # Clear existing content in the text box
        self.text_box.delete(1.0, END)
        # Display the scenario in the text box
        self.text_box.insert(END, f"{scenario}\n")

    def handle_response(self, user_input):
        # Handle different user responses
        if "explore" in user_input.lower():
            self.display_scenario("You decide to explore the mysterious cave.")
        elif "fight" in user_input.lower():
            self.display_scenario("A fierce dragon appears! Get ready for battle.")
        else:
            self.display_scenario("I'm sorry, I didn't understand that. Please try again.")

    def InsertDescriptionWidgets(self):
        # Clear the menu window if it's not empty
        for widget in self.menu.winfo_children():
            widget.destroy()

        custom_fontLabel = ("Helvetica", 15, "bold")
        custom_fontButton = ("Helvetica", 10, "bold")
        my_canvas = Canvas(self.menu, width=500, height=500)
        my_canvas.pack(fill="both", expand=True)
        my_canvas.create_image(0, 0, image=self.bg3, anchor='nw')
        my_canvas.create_text(250, 100, text="This is an old style text adventure game! Currently\nupon starting the game you are given a scenario in\nwhich you are given two options to choose from.", font=custom_fontLabel, fill="navy", anchor="center")
        backButton = Button(self.menu, text="Back to menu.", command=self.InsertMenuWidgets, padx=32, pady=25, fg="cyan", bg="navy", font=custom_fontButton)
        backButton_window = my_canvas.create_window(170, 250, anchor='nw', window=backButton)

# Main function.
def main():
    # Creates the menu window.
    menu = Tk()
    # Creates Game object to run the first instance of the game.
    gameOne = Game(menu)
    # Calling the main loop for the menu to run.
    menu.mainloop()

# Calling main function.
main()
