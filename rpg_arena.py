# The following program creates a battle arena for players
import random
import time


class Character:
    #Constructor
    def __init__ (self, name, strength, health, defense,):
        self.name= name
        self.strength= strength
        self.health= health
        self.defense= defense

    # Take Damage () Method
    def take_damage(self,damage):
        damage_taken=damage - self.defense
        self.health=damage_taken
        return damage_taken

    # Attack () Method
    def attack(self,target):
        damage = self.strength * 2
        damage_dealt= target.take_damage(damage)
        return damage_dealt

    # is_alive () method
    def is_alive(self):
        return self.health>0

# Extend a Class
class Rogue(Character):
    # Attack () Method
    def attack(self, target):
        dexterity = 20
        critical_hit = random.randint (0,100) < dexterity
        damage = self.strength * 2
        if critical_hit:
            damage *= 2
            print("***Critical Hit***")

        damage_dealt = target.take_damage(damage)
        return damage_dealt

#Arena Battle
def arena_battle(player,enemy):
    print(player.name + " vs. " + enemy.name)
    print(str(player.health) + " vs. " + str(enemy.health))

    while player.is_alive() and enemy.is_alive():
        print(player.name + ": " + str(player.health))
        print(enemy.name + ": " + str(enemy.health))

        damage=player.attack(enemy)
        print(player.name + " hits " + enemy.name + " for " + str(damage))

        damage=enemy.attack(player)
        print(enemy.name + " hits " + player.name + " for " + str(damage))

        time.sleep(1.5)

        #Declaring the winner
        if player.is_alive():
            print(player.name + " wins!")
        elif enemy.is_alive():
            print(enemy.name + " wins!")
        else:
            print("It's a draw!")
# Class Objects
player=Character("Beau",10,100,2)


enemy= Rogue("Katelyn",8,100,4)
