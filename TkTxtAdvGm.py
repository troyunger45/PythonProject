#Imports tkinter.
from tkinter import *
from tkinter import messagebox

class Game:

    def __init__(self, menu):
        #Adds formatting for menu window.
        self.menu = menu
        menu.title("Text Adventure Game!")
        menu.geometry('500x500')
        # Create the PhotoImage here.
        self.bg = PhotoImage(file="images/picture.png")
        #Calls InsertMenuWidgets
        self.InsertMenuWidgets()
        #Defines class attributes.
        self.health = 0
        self.xp = 0
        self.name = ""
        self.turn = 0

    def InsertMenuWidgets(self):
        my_canvas = Canvas(self.menu,width=500,height=500)
        my_canvas.pack(fill="both", expand=True)
        my_canvas.create_image(0,0, image=self.bg, anchor='nw')
        custom_fontLabel =("Helvetica", 25, "bold")
        custom_fontButton =("Helvetica", 10, "bold")
        my_canvas.create_text(250,250, text="Welcome to Our\nText Adventure Game", font=custom_fontLabel, fill="navy")
     
        startButton = Button(self.menu, text="Start Game!",command=self.InsertGameWidgets,padx=50,pady=25,bg="navy",fg="cyan",font=custom_fontButton)
        descriptionButton = Button(self.menu, text="Game Description.",command=self.InsertDescriptionWidgets,padx=32,pady=25,bg="navy",fg="cyan",font=custom_fontButton)
        startButton_window = my_canvas.create_window(250,150, anchor='nw', window=startButton)
    
    def InsertGameWidgets(self):
        #Destroys the menu window.
        self.menu.destroy()
        gameScreen = Tk()
        gameScreen.title("Playing the game...")
        gameScreen.geometry('500x500')
        gameScreen.configure(bg="blue")
        custom_font1 =("Helvetica", 10, "bold")
        backButton = Button(gameScreen,text="Back to menu.",command=lambda: self.BackToMenu(gameScreen),padx=32,pady=25,fg="cyan",bg="navy",font=custom_font1)
        backButton.pack(padx=10, pady=10)
        #Calling the main loop for the menu to run.
        gameScreen.mainloop()

    def InsertDescriptionWidgets(self):
        #Destroys the menu window.
        self.menu.destroy()
        descriptionScreen = Tk()
        descriptionScreen.title("Game Description")
        descriptionScreen.geometry('500x500')
        descriptionScreen.configure(bg="blue")
        custom_fontLabel =("Helvetica", 15, "bold")
        custom_fontButton =("Helvetica", 10, "bold")
        descriptionLabel = Label(descriptionScreen, text="This is an old style\ntext adventure game.", font=custom_fontLabel, bg="cyan", fg="navy", padx= 50, pady= 50)
        descriptionLabel.pack()
        backButton = Button(descriptionScreen,text="Back to menu.",command=lambda: self.BackToMenu(descriptionScreen),padx=32, pady=25,fg="cyan", bg="navy",font=custom_fontButton)
        backButton.pack(padx=10, pady=10)
        #Calling the main loop for the menu to run.
        descriptionScreen.mainloop()
    
    def BackToMenu(self, screen):
        screen.destroy()
        
        self.menu = Tk()
        self.menu.title("Text Adventure Game!")
        self.menu.geometry('500x500')
        self.menu.configure(bg="blue")
        self.InsertMenuWidgets()
        self.menu.deiconify()
        

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
