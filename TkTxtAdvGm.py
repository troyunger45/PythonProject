from tkinter import *

class Game:

    def __init__(self, menu):
        # Adds formatting for the menu window.
        self.menu = menu
        self.title = menu.title("")
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
        # Three parallel arrays that holds the scenarios, choices, and responses for the game.
        self.scenarios = [
            "Scenario 1: 1choice1 or 2choice2",
            "Scenario 2: 2choice1 or 2choice2",
            "A monster attacks what will you do: fight or run",
            "Scenario 4: 4choice1 or 4choice2",
            "Scenario 5: 5choice1 or 5choice2", 
        ]
        self.scenarioResponse = [
            ["1response1", "1response2"],
            ["2response1", "2response2"],
            ["You chose to fight!", "You Chose to run!"],
            ["4response1", "4response2"],
            ["5response1", "5response2"],
        ]
        self.scenarioChoice = [
            ["1choice1", "1choice2"],
            ["2choice1", "2choice2"],
            ["fight", "run"],
            ["4choice1", "4choice2"],
            ["5choice1", "5choice2"],
        ]
        self.scenarioCount = 0
    
    # Sets screen for the menu to be displayed.
    def InsertMenuWidgets(self):
        # Clear the menu window if it's not empty and set the counter back to the start.
        for widget in self.menu.winfo_children():
            widget.destroy()
        self.scenarioCount = 0
        # Setting the format of the window along with creating the canvas with the background image.
        self.title = self.menu.title("Text Adventure Game!")
        custom_fontLabel = ("Helvetica", 25, "bold")
        custom_fontButton = ("Helvetica", 10, "bold")
        my_canvas = Canvas(self.menu, width=500, height=500)
        my_canvas.pack(fill="both", expand=True)
        my_canvas.create_image(0, 0, image=self.bg, anchor='nw')
        # Creating and placing the menu title text to screen.
        my_canvas.create_text(250, 100, text="Welcome to Our\nText Adventure Game!", font=custom_fontLabel, fill="cyan", anchor="center")
        # Creating and placing the start and the description buttons to the screen.
        startButton = Button(self.menu, text="Start Game!", command=self.InsertGameWidgets, padx=53, pady=25, bg="navy", fg="cyan", font=custom_fontButton)
        descriptionButton = Button(self.menu, text="Game Description.", command=self.InsertDescriptionWidgets, padx=32, pady=25, bg="navy", fg="cyan", font=custom_fontButton)
        startButton_window = my_canvas.create_window(160, 250, anchor='nw', window=startButton)
        descriptionButton_window = my_canvas.create_window(160, 350, anchor='nw', window=descriptionButton)

    # Sets screen for the game to be played.
    def InsertGameWidgets(self):
        # Clear the menu window if it's not empty.
        for widget in self.menu.winfo_children():
            widget.destroy()
        # Setting the format of the window along with creating the canvas with the background image.
        self.title = self.menu.title("Playing The Game!")
        custom_font1 = ("Helvetica", 10, "bold")
        custom_font2 = ("Helvetica", 15, "bold")
        my_canvas = Canvas(self.menu, width=500, height=500)
        my_canvas.pack(fill="both", expand=True)
        my_canvas.create_image(0, 0, image=self.bg2, anchor='nw')
        # Creating and placing the back button to the screen.
        backButton = Button(self.menu, text="Exit game.", command=self.InsertMenuWidgets, padx=51.5, pady=25, fg="cyan", bg="navy", font=custom_font1)
        backButton_window = my_canvas.create_window(170, 370, anchor='nw', window=backButton)
        # Creating text instructions for entering input.
        my_canvas.create_text(250, 70, text="Enter choice here:", font=custom_font2, fill="navy", anchor="center")
        # Creating and placing the text box to the screen.
        self.text_box = Text(self.menu, width=50, height=7, wrap=WORD, font=custom_font1, bg="cyan", fg="navy")
        text_box_window = my_canvas.create_window(80, 130, anchor='nw', window=self.text_box)
        #Insert first scenario to the text box.
        self.text_box.insert(END, self.scenarios[0] )
        # Disable text box.
        self.text_box.config(state=DISABLED)
        # Creating and placing the entry for user input to the screen.
        user_input = Entry(self.menu, font=custom_font1, width=50, bg="cyan", fg="navy")
        user_input_window = my_canvas.create_window(80, 90, anchor='nw', window=user_input)
        # Creating and placing button to process user input.
        response_button = Button(self.menu, text="Display response.", padx=31, pady=25, fg="cyan", bg="navy", font=custom_font1, command=lambda: self.ProcessUserInput(user_input.get()))
        response_button_window = my_canvas.create_window(170, 270, anchor='nw', window=response_button)

    # Process user input and display a response
    def ProcessUserInput(self, user_input):
        # Sets the text box to enable and clears the previous text.
        self.text_box.config(state=NORMAL)
        self.text_box.delete(1.0, END)
        # Logic to decide if the game cycle has been completed or not.
        if self.scenarioCount < len(self.scenarios):
            # Check if the user input matches either of the choices for the current scenario.
            if user_input == self.scenarioChoice[self.scenarioCount][0]:    # Choice one.
                response_text = self.scenarioResponse[self.scenarioCount][0]
                # Determines when the player will need to fight. Fight option will always be in column 0.
                if self.scenarioCount == 2 and user_input == self.scenarioChoice[2][0]:
                    self.text_box.insert(END, "you are fighting the monster!" + "\n")
            elif user_input == self.scenarioChoice[self.scenarioCount][1]:    # Choice two.
                response_text = self.scenarioResponse[self.scenarioCount][1]
            else:   # invalid Option.
                response_text = f"You chose '{user_input}'. This is not a valid response. Please chose again."
                self.scenarioCount = self.scenarioCount - 1
            # Insert the response text and increment scenarioCount.
            self.text_box.insert(END, response_text + "\n")
            self.scenarioCount = self.scenarioCount + 1
            # Determines wether to display the next scenario or the conclusion.
            if self.scenarioCount < len(self.scenarios):
                self.text_box.insert(END, self.scenarios[self.scenarioCount])
            else:
                self.text_box.insert(END, "This is the conclusion of the game!")
        elif self.scenarioCount >= len(self.scenarios):
            self.text_box.insert(END, "All done! Please press exit game to restart!")
        # Disables text box.
        self.text_box.config(state=DISABLED)

    # Sets screen for the description to be displayed.
    def InsertDescriptionWidgets(self):
        # Clear the menu window if it's not empty.
        for widget in self.menu.winfo_children():
            widget.destroy()
        # Setting the format of the window along with creating the canvas with the background image.
        self.title = self.menu.title("Describing The Game!")
        custom_fontLabel = ("Helvetica", 15, "bold")
        custom_fontButton = ("Helvetica", 10, "bold")
        my_canvas = Canvas(self.menu, width=500, height=500)
        my_canvas.pack(fill="both", expand=True)
        my_canvas.create_image(0, 0, image=self.bg3, anchor='nw')
        # Creating and placing the description text to screen.
        my_canvas.create_text(250, 100, text="This is an old style text adventure game! Currently\nupon starting the game you are given a scenario in\nwhich you are given two options to choose from.", font=custom_fontLabel, fill="navy", anchor="center")
        # Creating and placing the back button to the screen.
        backButton = Button(self.menu, text="Back to menu.", command=self.InsertMenuWidgets, padx=32, pady=25, fg="cyan", bg="navy", font=custom_fontButton)
        backButton_window = my_canvas.create_window(170, 250, anchor='nw', window=backButton)

# Main function.
def main():
    # Creates the menu window.
    menu = Tk()
    # Creates Game object to run the first instance of the game.
    gameOne = Game(menu)
    # Calling the main loop for the GUI to run.
    menu.mainloop()

# Calling main function.
main()
