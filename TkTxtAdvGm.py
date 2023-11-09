#Imports tkinter.
from tkinter import *

class Game:

    def __init__(self, menu):
        #Adds formatting for menu window.
        self.menu = menu
        menu.title("Text Adventure Game!")
        menu.geometry('500x500')
        menu.configure(bg="blue")
        #Calls InsertMenuWidgets
        self.InsertMenuWidgets()
        #Defines class attributes.
        self.health = 0
        self.xp = 0
        self.name = ""
        self.turn = 0

    def InsertMenuWidgets(self):
        custom_font =("Helvetica", 25, "bold")
        menuLabel = Label(self.menu, text="Welcome to Our\nText Adventure Game", font=custom_font, bg="cyan", fg="navy", padx= 50, pady= 50)
        menuLabel.pack(padx=20,pady=20)
        startButton = Button(self.menu, text="Start Game!", command=self.InsertGameWidgets, padx=50, pady=25)
        startButton.pack(padx=10,pady=10)
        descriptionButton = Button(self.menu, text="Game Description.", command=self.InsertDescriptionWidgets, padx=32, pady=25)
        descriptionButton.pack(padx=10,pady=10)
    
    def InsertGameWidgets(self):
        #Destroys the menu window.
        self.menu.destroy()
        gameScreen = Tk()
        gameScreen.title("Playing the game...")
        gameScreen.geometry('500x500')
        gameScreen.configure(bg="blue")
        #Calling the main loop for the menu to run.
        gameScreen.mainloop()

    def InsertDescriptionWidgets(self):
        #Destroys the menu window.
        self.menu.destroy()
        descriptionScreen = Tk()
        descriptionScreen.title("Game Description")
        descriptionScreen.geometry('500x500')
        descriptionScreen.configure(bg="blue")
        custom_font =("Helvetica", 15, "bold")
        descriptionLabel = Label(descriptionScreen, text="This is an old style\ntext adventure game.", font=custom_font, bg="cyan", fg="navy", padx= 50, pady= 50)
        descriptionLabel.pack()
        backButton = Button(descriptionScreen,text="Back to menu.",command=lambda: self.BackToMenuFromDescription(descriptionScreen) , padx=32, pady=25)
        backButton.pack(padx=10, pady=10)
        #Calling the main loop for the menu to run.
        descriptionScreen.mainloop()
    
    def BackToMenuFromDescription(self, descriptionScreen):
        self.menu = Tk()
        self.menu.title("Text Adventure Game!")
        self.menu.geometry('500x500')
        self.menu.configure(bg="blue")
        self.InsertMenuWidgets()
        descriptionScreen.destroy()

#Main function.
def main():
    #Creates the menu window.
    menu = Tk()
    #Creates Game object to run the first instance of the game.
    gameOne = Game(menu)
    #Calling the main loop for the menu to run.
    menu.mainloop()

#Calling main function.    
main()
