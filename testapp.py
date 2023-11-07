import random

class Enemy:
    def __init__(self, name, max_HP, max_AP):
        self.name = name
        self.maxHP = max_HP
        self.maxAP = max_AP
        self.currentHP = max_HP
        
class Room:
    def __init__(self, enemy_difficulty, room_loot, enemy_quantity, hazard_chance):
        self.enemy_difficulty = enemy_difficulty
        self.room_loot = room_loot
        self.enemy_quantity = enemy_quantity
        self.hazard_chance = hazard_chance
        
enemies = [0]
room1 = Room(1,"Chocolate Coin",5,1)

name_list = ["Big rat", "Mystery Man", "Skeleton"]
while room1.enemy_quantity > 0:
    enemy1 = Enemy(name_list[random.randint(0,2)],random.randint(10*room1.enemy_difficulty,50*room1.enemy_difficulty),random.randint(5*room1.enemy_difficulty,20*room1.enemy_difficulty))
    room1.enemy_quantity = room1.enemy_quantity - 1
    print("Enemy Name: " + enemy1.name)
    print("Enemy Health: " + str(enemy1.maxHP))
    print("Enemy Action Points: " + str(enemy1.maxAP))