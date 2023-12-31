from tkinter import *
import random
class Game:

    def __init__(self, menu):
        # Adds formatting for the menu window.
        self.menu = menu
        self.title = menu.title("")
        menu.geometry('890x500')
        menu.resizable(False, False)
        # Defines class attributes.
        self.health = 75
        self.enemyHealth = 50
        self.healthCount= 1
        self.attack = False
        self.defend = False
        self.run = False
        self.invalidResponse = False
        self.previousDefend = False
        self.printDefendTwice = False
        self.scenarioCount = 0
        self.defense = 0
        self.itemValue = [
            [2,2],
            [3,3],
            [5,5]  
        ]
        self.enemyName = [
            "Hyperion guard",
            "Hyperion elite trooper",
            "The President's giant mech"
        ]
        self.enemiesHealth = [
            50,
            100,
            150
        ]
        # Three parallel arrays that holds the scenarios, choices, and responses for the game.
        self.scenarios = [
            "You are an AI engineer who is tasked with monitoring the AI that is now ruling over earth. The AI's leadership has been benevolent, wise and caring, until now. Something has been corrupting the AI, and you have been trying to stop it. One night, you find out what it is. A  mega-corporation, known as Hyperion Macro, has been tampering with the AI government, trying to bend it to their will and control the world. That same night, you are nearly killed by a rogue assassin, but you get away at the last second. In your haste, you snag two crucial items: your laser pistol, and something in your safe. Do you grab a 'first-aid kit' (+2 healing) or a 'light plate carrier' from your policing days (+2 armor)?",
            "After trekking through the dry, dusty fields of Galactican Plains, you find a farm and a Hyperion supply depot. Out of desperation, you try to find a spot to rest. However, a Hyperion guard sees you and tries to subdue you. Do you 'fight', or try to 'escape'?",
            "You come back to the supply depot later, rummaging for supplies. While scavenging, you find a holo-note next to some guards that shows a hidden underground bullet train that leads directly to Hyperion's headquarters. That explains why they'd have a supply depot out here in the middle of nowhere. You pocket the note and now begin searching for the entrance to this train. Do you look around 'quickly' or 'carefully'?",
            "You find the entrance to this advanced train station, but before you enter, something catches your eye from a nearby dumpster. Going to investigate it, you find two items. You can only grab one, though, as you hear the bullet train begin to take off. Do you grab an old 'adaptive armor set' (+3 armor) or a 'plasma rifle' (+3 damage)?",
            "Once on the train, you breathe a sigh of relief. A Hyperion elite trooper on the train has spotted you, however, and grabs his communicator. You quickly decide if you should engage the enemy or simply try to hide. Do you 'fight', or try to 'escape'?",
            "Emerging from the bullet train, you find you've finally made it to Hyperion HQ. The large, sleek walls rise up seemingly forever into the sky. The building itself intimidates you. What horrible things could be going on inside that would lead to world domination? Would you like to 'keep moving' or 'take a moment' to collect yourself? ",
            "You make it outside Hyperion HQ, and see two options before you. You could stroll through Hyperion's front entrance with a platoon of soldiers you see marching in, or you could duck off to the side and enter through a construction site. Do you enter through the 'front' or the 'side'?",
            "Rummaging through the storage room, you find some top-of-the-line gear. Would you like to grab the 'cryogenic stim shot' (+5 healing) or the 'prototype railgun' (+5 damage)?",
            "You find an old service elevator and scan the buttons inside. One button is simply labeled, “Access Point.” Fair enough. You push the button and descend deep underground. Once the doors open, you see a room filled with servers, monitors, and flashing lights. To the side, you see a room with some state-of-the-art equipment. You kick open the glass door, shattering it. Walking through the broken glass, you ready your weapon, only to stop and stare at the technological monstrosity towering above you. Hyperion's president controls a mech staring you down. You know it's him, you've seen his face before. Without a word, he readies his weapon. Do you try to 'negotiate' with him or 'distract' him?",
            "The president's giant mech looms before you, spinning up its gatling laser. You know you're in the right place, but you have to move quickly. The mech begins to unload lasers on the place you stood mere moments ago. Will you stand and 'fight' or will you try to 'escape'?",
            "Having successfully defeated the President in his Hyperion mech, a voice crackles over an intercom in the room. It's the board of directors, and they see how much you care about the world. They offer you a position of power in Hyperion, to become its new leader. You do know what's best for the world, after all. Do you accept 'yes' or 'no'?"
        ]
        self.scenarioResponse =[
            ["You grab your first aid kit and escape. Now with one mission, you find your way to Hyperion's headquarters.", "You grab your plate carrier and escape. Now with one mission, you find your way to Hyperion's headquarters."],
            ["You give the guard an elbow to the jaw as he grabs you, initiating combat.", "You break away and sprint for the exit, successfully escaping."],
            ["You decide to look quickly, scanning the area for any obvious signs or entrances to the hidden underground bullet train. Time is of the essence, and you hope that a fast search will reveal the entrance without drawing too much attention to yourself.", "Opting for a careful approach, you take your time to meticulously inspect the surroundings. You pay attention to details, looking for subtle clues or hidden mechanisms that might indicate the entrance to the underground bullet train. While this method is slower, you believe it reduces the risk of overlooking important details that could lead you astray."],
            ["You quickly grab the adaptive armor set and run to the futuristic train, slipping the suit on as you go. You feel more powerful as you duck into the train's closing doors.", "You quickly grab the plasma rifle and run to the futuristic train, turning off the safety as you go. You feel more powerful as you duck into the train's closing doors."],
            ["You rip the communicator out of the guard's hand and begin combat.", "You sprint into a cargo storage area and escape onto the train's roof. However, trying to stay on the train at these incredible speeds saps your strength substantially"],
            ["You snap yourself out of your thoughts. The here and now is what matters. You proceed onward.", "Overwhelmed by the sheer magnitude of Hyperion HQ, you decide to take a moment to collect yourself. You lean against a nearby wall, taking deep breaths to calm your nerves. As you gather your thoughts, you can't help but wonder about the mysteries hidden within those imposing walls. After a brief pause, you contemplate your next move."],
            ["You enter through the front with the platoon of soldiers. You blend in surprisingly well, even though your armor is a bit dirtier and outdated. After marching with them for a minute, you see a storage room and slink away to see what you can find", "You sneak into the construction site undetected. However, just as you find an entrance into Hyperion, a worker alerts his superiors to your presence. You jump in through the opening in the wall but have to sprint away from any potential items you may have been able to pick up."],
            ["You grab the cryo stim, admiring the technology needed to produce such incredible medicine. After putting it in your backpack, you head out, looking for a way down to Hyperion's server room.", "You grab the railgun. It's heavy, but it packs a SERIOUS punch. You look at all the wires and exposed parts, but it seems safe enough. You pick it up and head out, looking for a way down to Hyperion's server room."],
            ["You decide to attempt negotiation, raising your hands in a gesture of peace. 'We don't have to do this,' you say, trying to appeal to reason. You inquire about Hyperion's motives and whether there's room for a resolution without further bloodshed. However, the president remains stoic, refusing to engage in dialogue. With a cold glare, he readies his weapon, signaling that words won't stop the imminent confrontation.", "In a quick change of strategy, you decide to distract the president and buy yourself some time. You scan the room for any nearby control panels or exposed wiring. Spotting a console, you dash towards it, initiating a series of random commands to confuse the mech's systems. As alarms blare and lights flash, you hope the chaos will create an opening for your next move."],
            ["You ready your weapon and begin to fire back, initiating combat for the final time.", "You've come so far, you will not run away now."],
            ["Hyperion's board of directors calms you down and tells you that you would make an incredible leader. The former president didn't have the resolve to do a fraction of what you can. You know what's best for the world, you've already shown them. Hyperion is offering you a place of power, where your efforts can be fully recognized. You deserve more. You can make a difference. And after a long pause, you accept.", "You ignore the intercom and take one final shot with your weapon, obliterating the server that kept Hyperion in control of the AI. The calm messages quickly turn into frantic yells as alarms begin blaring throughout the entire building. You manage to escape the HQ though, by a worker who had also been fed up with Hyperion. You and the worker escape into the world, with a beautiful sunset adorning the sky. You're sure Hyperion will find you eventually, but they can never take away your achievements. You've beaten them, forever."]
        ]
        self.scenarioChoice = [
            ["first-aid kit", "light plate carrier"],       # Intro/Item1:      0
            ["fight", "escape"],                            # Enemy1:           1
            ["quickly", "carefully"],                       # Story2:           2
            ["adaptive armor set", "plasma rifle"],         # Item2:            3
            ["fight", "escape"],                            # Enemy2:           4
            ["keep moving", "take a moment"],               # Story3:           5
            ["front", "side"],                              # Shortcut/Trap:    6
            ["cryogenic stim shot", "prototype railgun"],   # Item3:            7
            ["negotiate", "distract"],                      # Story4:           8
            ["fight", "escape"],                            # Enemy3            9
            ["yes", "no"]                                   # Conclusion:       10
        ]
        self.SetImages()
        # Calls InsertMenuWidgets
        self.InsertMenuWidgets()
    
    # Resets the charater and enemy health back to the start of the game if they have died.
    def ResetHealth(self):
        if self.health <= 0:
            self.health = 75
            self.enemyHealth = 50

    def SetImages(self):
        # Creating the PhotoImages.
        self.menuPath = "images/menu.png"
        self.gamePath = "images/start.png"
        self.combatPath = "images/combat.png"
        self.descriptionPath = "images/description.png"
        
        if self.scenarioCount == 1 or self.scenarioCount == 2:
            self.gamePath = "images/combat1.png"
            self.bgGame = PhotoImage(file=self.gamePath)
            self.my_canvas.itemconfig(self.image_item, image=self.bgGame)
        elif self.scenarioCount == 3 or self.scenarioCount == 4:
            self.gamePath = "images/description.png"
            self.bgGame = PhotoImage(file=self.gamePath)
            self.my_canvas.itemconfig(self.image_item, image=self.bgGame)
        elif self.scenarioCount == 5 or self.scenarioCount == 6 or self.scenarioCount == 7:
            self.gamePath = "images/story3.png"
            self.bgGame = PhotoImage(file=self.gamePath)
            self.my_canvas.itemconfig(self.image_item, image=self.bgGame)
        elif self.scenarioCount == 8 or self.scenarioCount == 9 or self.scenarioCount == 10:
            self.gamePath = "images/story4.png"
            self.bgGame = PhotoImage(file=self.gamePath)
            self.my_canvas.itemconfig(self.image_item, image=self.bgGame)
        elif self.scenarioCount > 0:
            self.gamePath = "images/conclusion.png"
            self.bgGame = PhotoImage(file=self.gamePath)
            self.my_canvas.itemconfig(self.image_item, image=self.bgGame)
        else:
            self.bgGame = PhotoImage(file=self.gamePath)
           
        self.bgMenu = PhotoImage(file=self.menuPath)
        self.bgDescription = PhotoImage(file=self.descriptionPath)
        self.bgCombat = PhotoImage(file=self.combatPath)

    # Manages player and enemy damage for each point int the game.
    def SetDamage(self, enemy1, enemy2, enemy3):
        # Selects base player and enemy damaged based on the enemy type.
        if enemy1:
            self.enemyDamage = random.randint(13,19)
            self. playerDamage = random.randint(17,23)
        elif enemy2:
            self.enemyDamage = random.randint(21,27)
            self. playerDamage = random.randint(23,29)
        elif enemy3:
            self.enemyDamage = random.randint(26,32)
            self. playerDamage = random.randint(33,39)
        # Apply item values.
        if self.item2:
            self.playerDamage -= self.itemValue[0][1]
        if self.item3:
            self.playerDamage -= self.itemValue[1][0]
        if self.item4:
            self.enemyDamage += self.itemValue[1][1]
        if self.item6:
            self.enemyDamage -= self.itemValue[2][1]
    
    def SetDefense(self, enemy1, enemy2, enemy3):
        # Selects base defense based on the enemy type.
        if enemy1:
            self.defense = random.randint(10,15)
        elif enemy2:
            self.defense = random.randint(15,20)
        elif enemy3:
            self.defense = random.randint(25,30)
        # Apply item values.
        if self.item1:
            self.defense += self.itemValue[0][0]
        if self.item5:
            self.defense += self.itemValue[2][0]

    # Handles what happens when the fight window is exited by user.
    def OnFightWindowClose(self, fight_dialog):
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
        self.title = self.menu.title("Menu.")
        custom_fontLabel = ("Helvetica", 25, "bold")
        custom_fontButton = ("Helvetica", 10, "bold")
        my_canvas = Canvas(self.menu, width=500, height=500)
        my_canvas.pack(fill="both", expand=True)
        self.image_item = my_canvas.create_image(0, 0, image=self.bgMenu, anchor='nw')
        # Creating and placing the menu title text to screen.
        my_canvas.create_text(340, 100, text="Welcome to Code Revolt:\nHyperion's Fall!", font=custom_fontLabel, fill="#017189", anchor="center")
        # Creating and placing the start and the description buttons to the screen.
        startButton = Button(self.menu, text="Start Game!", command=self.InsertGameWidgets, padx=53, pady=25, bg="#480653", fg="#7AF9F9", font=custom_fontButton)
        descriptionButton = Button(self.menu, text="Game Description.", command=self.InsertDescriptionWidgets, padx=32, pady=25, bg="#480653", fg="#7AF9F9", font=custom_fontButton)
        startButton_window = my_canvas.create_window(160, 250, anchor='nw', window=startButton)
        descriptionButton_window = my_canvas.create_window(160, 350, anchor='nw', window=descriptionButton)

    # Sets screen for the game to be played.
    def InsertGameWidgets(self):
        # Clear the menu window if it's not empty.
        for widget in self.menu.winfo_children():
            widget.destroy()
        # Setting the format of the window.
        self.title = self.menu.title("Playing The Game!")
        custom_font1 = ("Helvetica", 10, "bold")
        custom_font2 = ("Helvetica", 15, "bold")
        # Reseting Flags for begining of the game.
        self.ResetHealth()
        self.scenarioCount = 0
        self.SetImages()
        self.item1 = False
        self.item2 = False
        self.item3 = False
        self.item4 = False
        self.item5 = False
        self.item6 = False
        # Creating the canvas with the background image.
        self.my_canvas = Canvas(self.menu, width=500, height=500)
        self.my_canvas.pack(fill="both", expand=True)
        self.gamePath = "images/start.png"
        self.my_canvas.create_image(0, 0, image=self.bgGame, anchor='nw')
        # Creating and placing the back button to the screen.
        backButton = Button(self.menu, text="Exit game.", command=self.InsertMenuWidgets, padx=35, pady=12.5, fg="#7AF9F9", bg="#480653", font=custom_font1)
        backButton_window = self.my_canvas.create_window(287.5, 418.5, anchor='nw', window=backButton)
        # Creating text instructions for entering input.
        self.my_canvas.create_text(250, 50, text="Enter choice here:", font=custom_font2, fill="#02A5C8", anchor="center")
        # Creating and placing the text box to the screen.
        self.text_box = Text(self.menu, width=50, height=19, wrap=WORD, font=custom_font1, bg="#7AF9F9", fg="#480653")
        text_box_window = self.my_canvas.create_window(80, 100, anchor='nw', window=self.text_box)
        #Insert first scenario to the text box.
        self.text_box.insert(END, self.scenarios[0])
        # Disable text box.
        self.text_box.config(state=DISABLED)
        # Creating and placing the entry for user input to the screen.
        self.user_input = Entry(self.menu, font=custom_font1, width=50, bg="#7AF9F9", fg="#480653")
        user_input_window = self.my_canvas.create_window(80, 70, anchor='nw', window=self.user_input)
        # Creating and placing button to process user input.
        self.response_button = Button(self.menu, text="Display response.", padx=35, pady=12.5, fg="#7AF9F9", bg="#480653", font=custom_font1, command=lambda: self.ProcessUserInput(self.user_input.get().lower()))
        response_button_window = self.my_canvas.create_window(80, 418.5, anchor='nw', window=self.response_button)

    # Process user input and display a response
    def ProcessUserInput(self, user_input):
        # Sets the text box to enable and clears the previous text.
        self.text_box.config(state=NORMAL)
        self.text_box.delete(1.0, END)
        self.user_input.delete(0, END)
        notValid = False
        fight = False
        # Logic to decide if the game cycle has been completed or not.
        if self.scenarioCount < len(self.scenarios):
            # Check if the user input matches either of the choices for the current scenario.
            if user_input == self.scenarioChoice[self.scenarioCount][0]:    # Choice one.
                response_text = self.scenarioResponse[self.scenarioCount][0]
                self.text_box.insert(END, response_text + "\n")
                # Determines when the player will need to fight or they picked up an Item. Fight and Item pick up option will always be in column 0.
                if (self.scenarioCount == 1 and user_input == self.scenarioChoice[1][0]) or (self.scenarioCount == 4 and user_input == self.scenarioChoice[4][0]) or (self.scenarioCount == 9 and user_input == self.scenarioChoice[9][0]):
                    self.Fight()
                    fight = True
                elif self.scenarioCount == 0 and user_input == self.scenarioChoice[0][0]:
                    self.item1 = True                   
                elif self.scenarioCount == 3 and user_input == self.scenarioChoice[3][0]:
                    self.item3 = True
                elif self.scenarioCount == 7 and user_input == self.scenarioChoice[7][0]:
                    self.item5 = True
            elif user_input == self.scenarioChoice[self.scenarioCount][1]:    # Choice two.
                response_text = self.scenarioResponse[self.scenarioCount][1]
                self.text_box.insert(END, response_text + "\n")
                #Trap scenario to skip items 5 and 6.
                if self.scenarioCount == 6 and user_input == self.scenarioChoice[6][1]:
                    self.scenarioCount = self.scenarioCount + 1
                elif self.scenarioCount == 0 and user_input == self.scenarioChoice[0][1]:
                    self.item2 = True
                elif self.scenarioCount == 3 and user_input == self.scenarioChoice[3][1]:
                    self.item4 = True
                elif self.scenarioCount == 7 and user_input == self.scenarioChoice[7][1]:
                    self.item6 = True
                elif self.scenarioCount == 9 and user_input == self.scenarioChoice[9][1]:
                    self.scenarioCount = self.scenarioCount - 1
            else:   # invalid Option.
                response_text = f"You chose '{user_input}'. This is not a valid response. Please choose again."
                self.text_box.insert(END, response_text + "\n") 
                self.scenarioCount = self.scenarioCount - 1
                notValid = True
            # Increment scenarioCount.
            self.scenarioCount = self.scenarioCount + 1
            if fight and self.closeFight:
                self.SetImages()
            elif fight:
                self.menu.after(1500, self.SetImages)
            elif notValid == False:
                self.SetImages()
            if self.health > 0:
                # Determines wether to display the next scenario or the conclusion.
                if self.scenarioCount < len(self.scenarios):
                    self.text_box.insert(END, self.scenarios[self.scenarioCount])
                else:
                    self.text_box.insert(END, "The End!")
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
        fight_dialog.resizable(False, False)
        # Bind the closing of the window to a function
        fight_dialog.protocol("WM_DELETE_WINDOW", lambda: self.OnFightWindowClose(fight_dialog))
        custom_font1 = ("Helvetica", 10, "bold")
        self.health = 75
        enemy1 = False
        enemy2 = False
        enemy3 = False
        self.response_button.config(state=DISABLED)
        if self.scenarioCount == 1:
            self.enemyHealth = self.enemiesHealth[0]
            enemy1 = True
            enemy_num = 0
        elif self.scenarioCount == 4:
            self.enemyHealth = self.enemiesHealth[1]
            enemy2 = True
            enemy_num = 1
        elif self.scenarioCount == 9:
            self.enemyHealth = self.enemiesHealth[2]
            enemy3 = True
            enemy_num = 2
        my_canvas = Canvas(fight_dialog, width=500, height=250)
        my_canvas.pack(fill="both", expand=True)
        my_canvas.create_image(0, 0, image=self.bgCombat, anchor='nw')
        # Creating and placing the text box to the screen.
        self.fight_box = Text(fight_dialog, width=50, height=7, wrap=WORD, font=custom_font1, bg="#7AF9F9", fg="#480653")
        fight_box_window = my_canvas.create_window(70, 80, anchor='nw', window=self.fight_box)
        # Creating and placing the entry for user input to the screen.
        self.fight_input = Entry(fight_dialog, font=custom_font1, width=50, bg="#7AF9F9", fg="#480653")
        fight_input_window = my_canvas.create_window(70, 40, anchor='nw', window=self.fight_input)
        # Button to process the user input and close the window.
        process_button = Button(fight_dialog, text="Process", command=lambda: self.ProcessFight(self.fight_input.get().lower(),enemy1,enemy2,enemy3), padx=25, pady=10, fg="#7AF9F9", bg="#480653", font=custom_font1)
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
            fight_dialog.after(1500, lambda: fight_dialog.destroy())
            self.menu.after(1500, lambda: self.InsertMenuWidgets())
        if self.enemyHealth <= 0:
            self.fight_box.insert(END, f"You killed the {self.enemyName[enemy_num].lower()}!\n")
            self.fight_box.insert(END, f"Your health: {self.health}.\n")
            fight_dialog.update()  # Update the fight box
            fight_dialog.after(1500, lambda: fight_dialog.destroy())
        if self.run == True:
            fight_dialog.after(1500, lambda: fight_dialog.destroy())
        self.response_button.config(state=NORMAL)
    
    # Processes the user's input in the fight scenario with boolean flags for the while loop.
    def ProcessFight(self, fight_input, enemy1,enemy2,enemy3):
        self.fight_box.delete(1.0, END)
        self.fight_input.delete(0, END)
        # Only Executes if the player is alive.
        if self.health >= 1 and self.enemyHealth >= 1:
            # When the user selects 'attack' for the fight.
            if fight_input == "attack":
                # Sets proper player and enemy damage.
                self.SetDamage(enemy1,enemy2,enemy3)
                self.enemyHealth -= self.enemyDamage
                self.health -= self.playerDamage 
                # Flags proper boolean values.        
                self.attack = True
                self.defend = False
                self.run = False
                self.invalidResponse = False
                self.previousDefend = False
                # Increase health count to know we are no longer on our first turn.
                self.healthCount += 1
            # When the user selects 'defend' for the fight.    
            elif fight_input == "defend":
                # Sets proper defense value.
                self.SetDefense(enemy1,enemy2,enemy3)
                # Decides if the player has selected defend once before.
                if self.previousDefend == False:
                    self.health += self.defense     # Health is only increased if the previous input was not defend.
                    self.previousDefend = True
                    self.printDefendTwice = False
                else:
                    self.printDefendTwice = True
                # Flags proper boolean values. 
                self.defend = True
                self.attack = False
                self.run = False
                self.invalidResponse = False
                # Increase health count to know we are no longer on our first turn.
                self.healthCount += 1
            # When the user selects 'run' for the fight.
            elif fight_input == "run":
                # Flags proper boolean values. 
                self.invalidResponse = False
                self.run = True
                self.attack = False
                self.defend = False
            # When user selects an invalid response for the fight.
            else:
                # Flags proper boolean values. 
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
        custom_fontLabel = ("Helvetica", 12, "bold")
        custom_fontButton = ("Helvetica", 10, "bold")
        my_canvas = Canvas(self.menu, width=800, height=500)
        my_canvas.pack(fill="both", expand=True)
        my_canvas.create_image(0, 0, image=self.bgDescription, anchor='nw')
        # Creating and placing the description text to screen.
        my_canvas.create_text(250, 50, text="Welcome to our Description Page!", font=custom_fontLabel, fill="#02A5C8", anchor="center")
        my_canvas.create_text(250, 100, text="This is an old style text adventure game! Currently\nupon starting the game you are given a scenario in\nwhich you are given two options to choose from.\nAllowing you to shape your destiny.", font=custom_fontButton, fill="#7AF9F9", anchor="center")
        my_canvas.create_text(243, 175, text="After completing a scenario you will move\non to the next one until your journey is complete.\nThere are story, item, and fight scenarios that\noffer a variety of different options to the user.", font=custom_fontButton, fill="#7AF9F9", anchor="center")
        my_canvas.create_text(240, 225, text="Choices for the user to interact.", font=custom_fontLabel, fill="#02A5C8", anchor="center")
        my_canvas.create_text(260, 290, text="Within the divergent types of scenarios, each will\ngive you a type of choice that is different from\neach other. Story scenarios give the player a moral\nchoice. Item scenarios give the user a choice in the\ncreation of their fight stats. Fight scenarios will provide\nthe user the ability to fight or escape from an enemy.", font=custom_fontButton, fill="#7AF9F9", anchor="center")
        my_canvas.create_text(635, 50, text="How combat works.", font=custom_fontLabel, fill="#02A5C8", anchor="center")
        my_canvas.create_text(650, 138, text="When a fight scenario occurs the user is given a\nchoice to fight or escape. If the user chooses fight,\nwe begin combat! While in combat, the user is given\nthree choices: attack, defend, or run. Attacking allows\nyou to do damage to the enemy, but the enemy also\ndoes damage to you. Defending allows the player the\nabilty to heal, but you can only do it once before\nneeding to attack again. Running allows the user to\nescape the enemy after selecting to fight.", font=custom_fontButton, fill="#7AF9F9", anchor="center")
        my_canvas.create_text(635, 225, text="Alternate Conclusions!", font=custom_fontLabel, fill="#02A5C8", anchor="center")
        my_canvas.create_text(650, 263, text="Based on what choices are selected, you can have\none of two different conclusions. This game forces you\nmake tough calls that can impact your future!", font=custom_fontButton, fill="#7AF9F9", anchor="center")
        my_canvas.create_text(635, 305, text="Credits and mentions:", font=custom_fontLabel, fill="#02A5C8", anchor="center")
        my_canvas.create_text(635, 360, text="* Troy Unger - Lead Developer\n* Matt Sickles - Project Leader/Story Author\n* Gavin Barnard - Developer\n* Manuel Gardea - Developer\n* Adian Chapman - Developer", font=custom_fontButton, fill="#7AF9F9", anchor="center")
        # Creating and placing the back button to the screen.
        backButton = Button(self.menu, text="Back to menu.", command=self.InsertMenuWidgets, padx=32, pady=25, fg="#7AF9F9", bg="#480653", font=custom_fontButton)
        backButton_window = my_canvas.create_window(160, 380, anchor='nw', window=backButton)

# Main function.
def main():
    # Creates the menu window.
    menu = Tk()
    # Creates Game object to run the first object of the game.
    game_one = Game(menu)
    # Calling the main loop for the GUI to run.
    menu.mainloop()

# Calling main function.
main()