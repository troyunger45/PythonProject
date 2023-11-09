from tkinter import *

class Game:

    def __init__(self, menu):
        # Adds formatting for the menu window.
        self.menu = menu
        menu.title("Text Adventure Game!")
        menu.geometry('500x500')
        # Create the PhotoImage here.
        self.bg = PhotoImage(file="images/picture.png")
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
        my_canvas.create_text(250, 250, text="Welcome to Our\nText Adventure Game", font=custom_fontLabel, fill="navy")

        startButton = Button(self.menu, text="Start Game!", command=self.InsertGameWidgets, padx=50, pady=25, bg="navy", fg="cyan", font=custom_fontButton)
        descriptionButton = Button(self.menu, text="Game Description.", command=self.InsertDescriptionWidgets, padx=32, pady=25, bg="navy", fg="cyan", font=custom_fontButton)
        startButton_window = my_canvas.create_window(250, 150, anchor='nw', window=startButton)

    def InsertGameWidgets(self):
        # Clear the menu window if it's not empty
        for widget in self.menu.winfo_children():
            widget.destroy()

        my_canvas = Canvas(self.menu, width=500, height=500)
        my_canvas.pack(fill="both", expand=True)
        my_canvas.create_image(0, 0, image=self.bg, anchor='nw')
        custom_font1 = ("Helvetica", 10, "bold")
        backButton = Button(self.menu, text="Back to menu.", command=self.InsertMenuWidgets, padx=32, pady=25, fg="cyan", bg="navy", font=custom_font1)
        backButton_window = my_canvas.create_window(250, 150, anchor='nw', window=backButton)

    def InsertDescriptionWidgets(self):
        # Clear the menu window if it's not empty
        for widget in self.menu.winfo_children():
            widget.destroy()

        custom_fontLabel = ("Helvetica", 15, "bold")
        custom_fontButton = ("Helvetica", 10, "bold")
        descriptionLabel = Label(self.menu, text="This is an old style\ntext adventure game.", font=custom_fontLabel, bg="cyan", fg="navy", padx=50, pady=50)
        descriptionLabel.pack()
        backButton = Button(self.menu, text="Back to menu.", command=self.InsertMenuWidgets, padx=32, pady=25, fg="cyan", bg="navy", font=custom_fontButton)
        backButton.pack(padx=10, pady=10)

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