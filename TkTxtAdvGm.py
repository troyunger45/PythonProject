from tkinter import *
import random
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
        self.bg4 = PhotoImage(file="images/picture5.png")
        # Defines class attributes.
        self.health = 75
        self.xp = 0
        self.name = ""
        self.enemyHealth = 50
        self.healthCount=1
        self.attack = False
        self.defend = False
        self.run = False
        self.invalidResponse = False
        self.previousDefend = False
        self.printDefendTwice = False
        self.scenarioCount = 0
        self.defense = 0
        # Three parallel arrays that holds the scenarios, choices, and responses for the game.
        self.scenarios = [
            "Scenario 1: 1choice1 or 1choice2",
            "Scenario 2: 2choice1 or 2choice2",
            "A monster attacks what will you do: fight or run",
            "You found a shield: pick up or leave",
            "Scenario 5: 5choice1 or 5choice2",
            "A cyborg attacks what will you do: fight or run",
            "You found a sword: pick up or leave",
            "Scenario 8: 8choice1 or 8choice2",
            "A centurion-bot attacks what will you do: fight or run",
            "Scenario 10: 10choice1 or 10choice2",
        ]
        self.scenarioResponse =[
            ["1response1", "1response2"],
            ["2response1", "2response2"],
            ["You chose to fight the monster!", "You chose to run!"],
            ["You pick up the shield, increasing the healing you do when defending.", "you left the shield."],
            ["5response1", "5response2"],
            ["You chose to fight the cyborg!", "You chose to run!"],
            ["You pick up the sword, increasing the damage you do to enemies.", "you left the sword."],
            ["8response1", "8response2"],
            ["You chose to fight the centurion-bot!", "You chose to run!"],
            ["10response1", "10response2"]
        ]
        self.scenarioChoice = [
            ["1choice1", "1choice2"],
            ["2choice1", "2choice2"],
            ["fight", "run"],
            ["pick up", "leave"],
            ["5choice1", "5choice2"],
            ["fight", "run"],
            ["pick up", "leave"],
            ["8choice1", "8choice2"],
            ["fight", "run"],
            ["10choice1", "10choice2"]
        ]
        self.enemyName = [
            "Monster",
            "Cyborg",
            "Centurion-bot"
        ]
        self.enemiesHealth = [
            50,
            100,
            150
        ]
        # Calls InsertMenuWidgets
        self.InsertMenuWidgets()
    
    def ResetHealth(self):
        if self.health <= 0:
            self.health = 75
            self.enemyHealth = 50

    def SetDamage(self, enemy1, enemy2, enemy3):
        if enemy1:
            self.enemyDamage = random.randint(13,19)
            self. playerDamage = random.randint(15,21)
        elif enemy2:
            self.enemyDamage = random.randint(21,27)
            self. playerDamage = random.randint(21,27)
        elif enemy3:
            self.enemyDamage = random.randint(26,32)
            self. playerDamage = random.randint(31,37)
        # Apply the swords damage bonus if the player has picked up the sword.
        if self.item2:
            self.enemyDamage += random.randint(1,3)
    
    def SetDefense(self, enemy1, enemy2, enemy3):
        if enemy1:
            self.defense = random.randint(10,15)
        elif enemy2:
            self.defense = random.randint(15,20)
        elif enemy3:
            self.defense = random.randint(25,30)
        # Apply the shield's defense bonus if the player has picked up the shield.
        if self.item1:
            self.defense += random.randint(1,3)

    def on_fight_window_close(self, fight_dialog):
        # Handle any necessary cleanup or actions when the fight window is closed.
        self.response_button.config(state=NORMAL)
        self.closeFight = True
        self.text_box.insert(END, "You closed the fight window.\n")
        fight_dialog.destroy()
    
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
        self.ResetHealth()
        self.scenarioCount = 0
        self.item1 = False
        self.item2 = False
        my_canvas = Canvas(self.menu, width=500, height=500)
        my_canvas.pack(fill="both", expand=True)
        my_canvas.create_image(0, 0, image=self.bg3, anchor='nw')
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
        self.user_input = Entry(self.menu, font=custom_font1, width=50, bg="cyan", fg="navy")
        user_input_window = my_canvas.create_window(80, 90, anchor='nw', window=self.user_input)
        # Creating and placing button to process user input.
        self.response_button = Button(self.menu, text="Display response.", padx=31, pady=25, fg="cyan", bg="navy", font=custom_font1, command=lambda: self.ProcessUserInput(self.user_input.get().lower()))
        response_button_window = my_canvas.create_window(170, 270, anchor='nw', window=self.response_button)

    # Process user input and display a response
    def ProcessUserInput(self, user_input):
        # Sets the text box to enable and clears the previous text.
        self.text_box.config(state=NORMAL)
        self.text_box.delete(1.0, END)
        self.user_input.delete(0, END)
        # Logic to decide if the game cycle has been completed or not.
        if self.scenarioCount < len(self.scenarios):
            # Check if the user input matches either of the choices for the current scenario.
            if user_input == self.scenarioChoice[self.scenarioCount][0]:    # Choice one.
                response_text = self.scenarioResponse[self.scenarioCount][0]
                self.text_box.insert(END, response_text + "\n")
                # Determines when the player will need to fight or they picked up an Item. Fight and Item pick up option will always be in column 0.
                if (self.scenarioCount == 2 and user_input == self.scenarioChoice[2][0]) or (self.scenarioCount == 5 and user_input == self.scenarioChoice[5][0]) or (self.scenarioCount == 8 and user_input == self.scenarioChoice[8][0]): 
                    self.Fight() 
                elif self.scenarioCount == 3 and user_input == self.scenarioChoice[3][0]:
                    self.item1 = True 
                elif self.scenarioCount == 6 and user_input == self.scenarioChoice[6][0]:
                    self.item2 = True
            elif user_input == self.scenarioChoice[self.scenarioCount][1]:    # Choice two.
                response_text = self.scenarioResponse[self.scenarioCount][1]
                self.text_box.insert(END, response_text + "\n") 
            else:   # invalid Option.
                response_text = f"You chose '{user_input}'. This is not a valid response. Please choose again."
                self.text_box.insert(END, response_text + "\n") 
                self.scenarioCount = self.scenarioCount - 1
            # Increment scenarioCount.
            self.scenarioCount = self.scenarioCount + 1
            if self.health > 0:
                # Determines wether to display the next scenario or the conclusion.
                if self.scenarioCount < len(self.scenarios):
                    self.text_box.insert(END, self.scenarios[self.scenarioCount])
                else:
                    self.text_box.insert(END, "This is the conclusion of the game!")
        elif self.scenarioCount >= len(self.scenarios) and self.health > 0:
            self.text_box.insert(END, "All done! Please press exit game to restart!")
        if self.health > 0:
            # Disables text box.
            self.text_box.config(state=DISABLED)
            self.response_button.config(state=NORMAL)

    def Fight(self):
        # Create a new Toplevel window for the fight scenario.
        fight_dialog = Toplevel(self.menu)
        fight_dialog.title("Fight Scenario")
        fight_dialog.geometry('500x275')
        # Bind the closing of the window to a function
        fight_dialog.protocol("WM_DELETE_WINDOW", lambda: self.on_fight_window_close(fight_dialog))
        custom_font1 = ("Helvetica", 10, "bold")
        self.health = 75
        enemy1 = False
        enemy2 = False
        enemy3 = False
        self.response_button.config(state=DISABLED)
        if self.scenarioCount == 2:
            self.enemyHealth = self.enemiesHealth[0]
            enemy1 = True
            enemy_num = 0
        elif self.scenarioCount == 5:
            self.enemyHealth = self.enemiesHealth[1]
            enemy2 = True
            enemy_num = 1
        elif self.scenarioCount == 8:
            self.enemyHealth = self.enemiesHealth[2]
            enemy3 = True
            enemy_num = 2
        my_canvas = Canvas(fight_dialog, width=500, height=250)
        my_canvas.pack(fill="both", expand=True)
        my_canvas.create_image(0, 0, image=self.bg4, anchor='nw')
        # Creating and placing the text box to the screen.
        self.fight_box = Text(fight_dialog, width=50, height=7, wrap=WORD, font=custom_font1, bg="cyan", fg="navy")
        fight_box_window = my_canvas.create_window(70, 80, anchor='nw', window=self.fight_box)
        
        # Creating and placing the entry for user input to the screen.
        self.fight_input = Entry(fight_dialog, font=custom_font1, width=50, bg="cyan", fg="navy")
        fight_input_window = my_canvas.create_window(70, 40, anchor='nw', window=self.fight_input)
        # Button to process the user input and close the window.
        process_button = Button(fight_dialog, text="Process", command=lambda: self.ProcessFight(self.fight_input.get().lower(),enemy1,enemy2,enemy3), padx=25, pady=10, fg="cyan", bg="navy", font=custom_font1)
        process_button_window = my_canvas.create_window(195, 200, anchor='nw', window=process_button)

        self.healthCount = 1
        self.attack = False
        self.defend = False
        self.run = False
        self.invalidResponse = False
        self.previousDefend = False
        self.printDefendTwice = False
        self.closeFight = False
        # Continuously check player's health during the fight
        while self.health > 0 and self.enemyHealth > 0:
            if self.closeFight == False:
                # Update the fight box with current health information
                self.fight_box.delete(1.0, END)
                if self.invalidResponse == True:
                    self.fight_box.insert(END, f"You chose '{self.fight_input.get()}'. This is not a valid response. Please choose again.\n")
                elif self.run == True:
                    if enemy3:
                        self.fight_box.insert(END,"You cannot run from this fight! Defend or attack!\n" )
                    else:
                        self.fight_box.insert(END,"You ran away with you life!\n" )
                        break
                elif self.healthCount == 1:
                    if enemy1 == True:
                        self.fight_box.insert(END, f"The {self.enemyName[enemy_num].lower()} charges! What will you do? attack, defend, or run.\nRemember you may only defend one time before you have to chose attack." + "\n")
                    elif enemy2 == True:
                        self.fight_box.insert(END, f"The {self.enemyName[enemy_num].lower()} charges! What will you do? attack, defend, or run.\nRemember you may only defend one time before you have to chose attack." + "\n")
                    elif enemy3 == True:
                        self.fight_box.insert(END, f"The {self.enemyName[enemy_num].lower()} charges! What will you do? attack, defend, or run.\nRemember you may only defend one time before you have to chose attack." + "\n")
                elif self.attack == True: 
                    if enemy1 == True:
                        self.fight_box.insert(END,f"You attacked! Dealing {self.enemyDamage} damage to the {self.enemyName[enemy_num].lower()}, but you were hit causing {self.playerDamage} damage to you.\n" )
                    elif enemy2 == True:
                        self.fight_box.insert(END,f"You attacked! Dealing {self.enemyDamage} damage to the {self.enemyName[enemy_num].lower()}, but you were hit causing {self.playerDamage} damage to you.\n" )
                    elif enemy3 == True:
                        self.fight_box.insert(END,f"You attacked! Dealing {self.enemyDamage} damage to the {self.enemyName[enemy_num].lower()}, but you were hit causing {self.playerDamage} damage to you.\n" )
                elif self.defend == True:
                    if self.printDefendTwice == False:
                        self.fight_box.insert(END, f"You held your stance, giving you {self.defense} health.\n")
                        self.previousDefend = True  # Update the flag after a successful defend
                    else:
                        self.fight_box.insert(END, "You must attack before you may defend!\n")  
                if enemy1 == True:
                    self.fight_box.insert(END, f"{self.enemyName[enemy_num]}'s health: {self.enemyHealth}.\n")
                elif enemy2 == True:
                    self.fight_box.insert(END, f"{self.enemyName[enemy_num]}'s health: {self.enemyHealth}.\n")
                elif enemy3 == True:
                    self.fight_box.insert(END, f"{self.enemyName[enemy_num]}'s health: {self.enemyHealth}.\n")
                if self.health >= 0:
                    self.fight_box.insert(END, f"Your health: {self.health}.\n")
                fight_dialog.update()
                # Wait for a short time to avoid a tight loop
                fight_dialog.after(100)
            else:
                self.scenarioCount= self.scenarioCount - 1
                break
                
        # Player's health is 0 or below, handle the death
        if self.health <= 0:
            self.fight_box.insert(END, "You died!\n")
            fight_dialog.update()  # Update the fight box
            fight_dialog.after(1000, lambda: fight_dialog.destroy())
            self.menu.after(1000, lambda: self.InsertMenuWidgets())
        if self.enemyHealth <= 0:
            self.fight_box.insert(END, f"You killed the {self.enemyName[enemy_num].lower()}!\n")
            self.fight_box.insert(END, f"Your health: {self.health}.\n")
            fight_dialog.update()  # Update the fight box
            fight_dialog.after(1000, lambda: fight_dialog.destroy())
        if self.run == True:
            fight_dialog.after(1000, lambda: fight_dialog.destroy())
        self.response_button.config(state=NORMAL)
    
    def ProcessFight(self, fight_input, enemy1,enemy2,enemy3):
        self.fight_box.delete(1.0, END)
        self.fight_input.delete(0, END)
        if self.health >= 1 and self.enemyHealth >= 1:
            if fight_input == "attack":
                self.SetDamage(enemy1,enemy2,enemy3)
                self.enemyHealth -= self.enemyDamage
                self.health -= self.playerDamage        
                self.attack = True
                self.defend = False
                self.run = False
                self.invalidResponse = False
                self.previousDefend = False
                self.healthCount += 1
            elif fight_input == "defend":
                self.defend = True
                self.SetDefense(enemy1,enemy2,enemy3)
                if self.previousDefend == False:
                    self.health += self.defense
                    self.previousDefend = True
                    self.printDefendTwice = False
                else:
                    self.printDefendTwice = True
                self.attack = False
                self.run = False
                self.invalidResponse = False
                self.healthCount += 1
            elif fight_input == "run":
                self.invalidResponse = False
                self.run = True
                self.attack = False
                self.defend = False
            else:
                self.invalidResponse = True
                self.run = False
                self.attack = False
                self.defend = False
            # Update the display
            self.menu.update_idletasks()
                 
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
        my_canvas.create_image(0, 0, image=self.bg2, anchor='nw')
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
    game_one = Game(menu)
    # Calling the main loop for the GUI to run.
    menu.mainloop()

# Calling main function.
main()