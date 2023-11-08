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
        menuLabel.pack()
        startButton = Button(self.menu, text="Start Game!", command=self.InsertGameWidgets, padx=50, pady=25)
        startButton.pack()
        descriptionButton = Button(self.menu, text="Game Description." , padx=32, pady=25)
        descriptionButton.pack()
    
    def InsertGameWidgets(self):
        #Destroys the menu window.
        self.menu.destroy()
        gameScreen = Tk()
        gameScreen.title("Playing the game...")
        gameScreen.geometry('500x500')
        gameScreen.configure(bg="blue")

        #Calling the main loop for the menu to run.
        gameScreen.mainloop()

    def InsertDescriptionWidgets():

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
