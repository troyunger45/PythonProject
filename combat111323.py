'''

How this code works:
1. Variables are all declared.
2. You will be prompted to input an armor, primary and secondary weapon, and a perk for both the player and an enemy.
3. Combat begins, and you pick different options depending on what keys are pressed. Just run the code and it'll make sense :D

PROBLEMS TO BE FIXED:

    GET STAMINA TO WORK (STAMINA IS SET AT THE ARMOR SELECTION BUT EITHER STAMINA DRAIN DOESN'T WORK OR AN EQUATION OR PLACEMENT IS WRONG)

    HAVE THE CODE LOOP BETWEEN PLAYER AND ENEMY TURNS UNTIL ONE OF THEM DIES (CURRENTLY THE ENEMY ENDING THEIR TURN CAUSES THE CODE TO SOFTLOCK)

    GAME WILL NOT QUIT WHEN PLAYER OR ENEMY PERISHES

Note: Crit chance and ammo have not been implemented yet so if you want to delete them that's fine, or if you wanna get them to work that'd be great!

AIDAN'S NOTES
- I'm going to change all player inputs into uppercase during the fight.
-I think that it's better not to ask the user to input a string of characters to make choices, especially if we're not going to have a system in place to catch mistakes. I changed the player armor choice.
- I think the player stamina may not have worked because the primary weapons don't assign a stamina drain for primary weapons. They assign a "staminaDrain" not a "staminaDrainPri", which the combat encounter works with.
- I replaced the entire combat encounter. Sorry about that.
- I added a "player_turn" boolean variable to replace the turn counter as the check for whose turn it is.

'''
import random

p_health = 100
p_damagePri = 0
p_damageSec = 0
p_stamina = 0
p_staminaDrainPri = 0
p_staminaDrainSec = 0
p_chanceToHitPri = 0
p_chanceToHitSec = 0
p_critChance = 0
p_piAmmo = 0
p_shAmmo = 0
p_asAmmo = 0

e_health = 100
e_damagePri = 0
e_damageSec = 0
e_stamina = 0
e_staminaDrainPri = 0
e_staminaDrainSec = 0
e_chanceToHitPri = 0
e_chanceToHitSec = 0
e_critChance = 0
#enemies will have unlimited ammo for now

critMult = 1.5

# Assign the player armor.
print("What armor should the player have? Enter your answer as a number from the list below.")
print("1. No armor")
print("2. Jogging outfit")
print("3. Light armor")
p_armor = input()
if p_armor == 1: #No armor
   p_stamina = 50
elif p_armor == 2: #Jogging outfit
     p_stamina =  70
elif p_armor == 3: #Light armor
    p_stamina = 40
    p_health = 115
else: #Default if the player enters an invalid input.
    p_stamina = 30
    p_health = 125
    
p_primary = input("What primary should the character have?")
if p_primary == "shotgun":
    p_damagePri = 100
    p_staminaDrain = 30
    p_chanceToHitPri = 80
    p_shAmmo = 10
else: #assault rifle
    p_damagePri = 65
    p_staminaDrain = 10
    p_chanceToHitPri = 80
    p_asAmmo = 15

p_sec = input("What sidearm should the character have?")
if p_sec == "switchblade":
    p_damageSec = 25
    p_staminaDrainPri = 10
    p_chanceToHitSec = 100
else: #pistol
    p_damageSec = 50
    p_staminaDrainPri = 10
    p_chanceToHitSec = 60
    p_piAmmo = 30

p_perk = input("Pick a perk: J for juggernaut (more health), C for commando (more damage w/ auto rifles), or G for gunslinger (more damage w/ pistols).")
if p_perk == "J":
    p_health = p_health + 25
elif p_perk == "C":
    p_damagePri = p_damagePri + 10
else:
    p_damageSec = p_damageSec + 20

print("You have {} stamina, {} health, and deal {} damage with your primary/{} with your secondary.".format(p_stamina,p_health,p_damagePri,p_damageSec))

e_armor = input("What armor should the enemy have?")
if e_armor == "no armor":
    e_stamina = 50
elif e_armor == "jogging outfit":
    e_stamina = 70
elif e_armor == "light armor":
    e_stamina = 40
    e_health = 115
else:
    e_stamina = 30
    e_health = 125

e_primary = input("What primary should the enemy have?")
if e_primary == "shotgun":
    e_damagePri = 100
    e_staminaDrainPri =30
    e_chanceToHitPri =80
else: #assault rifle
    e_damagePri = 65
    e_staminaDrainPri = 10
    e_chanceToHitPri = 80

e_sec = input("What sidearm should the enemy have?")
if e_sec == "switchblade":
    e_damageSec = 25
    e_staminaDrainSec = 10
    e_chanceToHitSec = 100
else: #pistol
    e_damageSec = 50
    e_staminaDrainSec = 10
    e_chanceToHitSec = 60

print("The enemy has {} stamina, {} health, and deals {} damage with their primary/{} with their secondary.".format(e_stamina,e_health,e_damagePri,e_damageSec))

turnCounter = 1
inCombat = True
player_turn = True

# Sorry about this, but it would be basically impossible for the to figure out exactly how the original code is supposed to work, so I just remade it. HOPEFULLY I made this relatively easy to understand, and easy to modify.

while inCombat == True: #Checks to see if combat has ended.
    print("--TURN " + str(turnCounter) + "--")
    print("You have " + str(p_health) + " remaining.")
    print("The enemy has " + str(e_health) + " remaining.")
    
    #Checks to see if it is the player's turn. If it is, the player takes their turn.
    if player_turn == True:
        print("It's your turn. What would you like to do?")
        print("P) Fire your primary weapon")
        print("S) Fire your secondary weapon")
        print("C) Check your stats")
        print("E) Will end your turn without doing anything")
        p_action = input()
        p_action = p_action.upper()
        p_stamina = p_stamina + 10 #Charging player stamina.
        
        #The player uses their primary weapon
        if p_action == "P":
            if p_stamina - p_staminaDrainPri >= 0:
               print("You shot at the enemy")
               if random.randint(0,100) < p_chanceToHitPri:
                   e_health = e_health - p_damagePri
                   print("You hit the enemy for " + str(p_damagePri) + " damage!")
               else:
                   print("You missed")
            else:
                print("You tried to fire your gun, but you fumbled")
                    
            
        
        player_turn = False
        
    #Enemy turn
    elif player_turn == False:
        print("It is the enemy's turn")
        print("The enemy shits his pants!")
        
        #This stuff happens after the enemy finishes their actions.
        player_turn = True
        turnCounter = turnCounter + 1
    #This stuff happens after a turn.
    if p_health <= 0:
        print("The player has died. Game over.")
        exit()
    elif e_health <= 0:
        print("The enemy has died. You win!")
        exit()
        

#This is the old combat encounter code.
'''
while(inCombat) == True:
    while(turnCounter%2) == 0:
        
        #Explains the players options and asks for their input.
        print("It's your turn. What would you like to do?")
        print("P) Fire your primary weapon")
        print("S) Fire your secondary weapon")
        print("C) Check your stats")
        print("E) Will end your turn without doing anything")
        p_action = input()
        p_action = p_action.upper()
        
        if p_action == "P":
            p_stamina = p_stamina - p_staminaDrainPri
            print("You have {} stamina remaining.".format(p_stamina))
            if p_stamina >= p_staminaDrainPri:
#this SHOULD have the player's stamina drain by the ammount set in each weapon, however this does not seem to work
                if random.randint(0,100)<p_chanceToHitPri:
                    e_health = e_health - p_damagePri
                    if e_health <= 0:
                        print("The enemy has perished, you win!")
                        inCombat = False
                        exit
                    else:
                        print("{} damage was done to the enemy, leaving them at {} health!".format(p_damagePri,e_health))
                else:
                    print("Your shot missed!")
            else:
                print("You don't have enough stamina for that!")
        elif p_action == "S":
            if p_stamina >= p_staminaDrainSec:
                p_stamina = p_stamina - p_staminaDrainSec
                if random.randint(0,100)<p_chanceToHitSec:
                    e_health = e_health - p_damageSec
                    if e_health <= 0:
                        print("The enemy has perished, you win!")
                        inCombat = False
                        quit
                    else:
                        print("{} damage was done to the enemy, leaving them at {} health!".format(p_damageSec,e_health))
                else:
                    print("Your shot missed!")
            else:
                print("You don't have enough stamina for that!")
        elif p_action == "C":
            print("Right now, you have {} health and {} stamina. The enemy has {} health and {} stamina.".format(p_health,p_stamina,e_health,e_stamina))
        else:
            print("You finish your turn.")
            print("It's the enemy's turn!")
            turnCounter =+ 1

    #ENEMY TURN: The enemy SHOULD attack until it has too little stamina. Once it checks that it does not have enough stamina for either weapon, it will end the turn.

    while(turnCounter%2) != 0:
        e_action = 0
        e_action = random.randint(1,2)
        if e_action == 1:
            e_stamina = e_stamina - e_staminaDrainPri
            if e_stamina >= e_staminaDrainPri:
                if random.randint(0,100)>e_chanceToHitPri:
                    p_health = p_health - e_damagePri
                    if p_health <= 0:
                        print("You have perished, the enemy wins.")
                        inCombat = False
                        quit
                    else:
                        print("{} damage was done to you, leaving you at {} health!".format(e_damagePri,p_health))
                        break
                else:
                    print("The enemy's shot missed!")
            else:
                e_action = e_action + 1
        if e_action == 2:
            if e_stamina >= e_staminaDrainSec:
                e_stamina = e_stamina - e_staminaDrainSec
                if random.randint(0,100)>e_chanceToHitSec:
                    p_health = p_health - e_damageSec
                    if p_health <= 0:
                        print("You have perished, the enemy wins.")
                        inCombat = False
                        exit
                    else:
                        print("{} damage was done to you, leaving you at {} health!".format(p_damageSec,e_health))
                        break
                else:
                    print("The enemy's shot missed!")
                    break
            else:
                e_action = e_action + 1
                break
        else:
            print("The enemy finished their turn.")
            turnCounter =+ 1
        
'''