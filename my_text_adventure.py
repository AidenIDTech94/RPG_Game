#The following project creates a text adventure game.
import random
def adventure():
    # Introduction
    print("\nWelcome to the Museum Heist")
    print("You're an agent who has been recently hired by a mysterious company to steal the Diamond of Power! "
          "\nBut, the area is full of guards in the way. It is time to put your skills to the test")

    # Player Choices
    print("1. Break the window of the roof and try to hide behind one of the garbage cans.")
    print("2. Bail out and steal a less valuable object from a nearby building.")
    player_choice =int(input("What do you want to do?"))


    if player_choice == 1:
        print("\nYou break through one of the roof windows and hid behind a garbage can."
              "\nYou managed to avoid being caught, but you saw many guards patrolling the area.")
        # Fork in the Road
        print("Your evasion skills allow you to avoid the traps in the way."
              "\n However, there is a fork in the road to get to the Diamond. "
              "\n You see a security door that requires a riddle."
              "\n Furthermore, you see a suspicious-looking vent in one of the walls that you can crawl into. "
              "\nmaybe only one of them would read to the right path...")
        print("1. Choose the security door route and try to guess the riddle to access the East Hall.")
        print("2. Navigate through the vents to the East Hall.")
        player_choice = int(input("What do you want to do? "))

        # Option 1
        if player_choice ==1:
            print("\n You decide to go to the security door which reads the following riddle: "
                  "\n'I am used on everyday devices. I give the info based on the what the users input into my system. "
                  "\nI'm a common language used in a device that has a board to type, access to worldwide web, and found in offices. "
                  "\nWhat am I? ")
            print("1. It is Python.")
            print("2. It is Java")
            player_choice = int(input("Which answer is it? "))
            # Correct Choice
            if player_choice ==1:
                print("You say it is Python and the computer system says,'How did you know.' It promptly opens the door."
                      "\n You continue into the East Hall in search of the Diamond of Power. ")
                # A predicament
                print("You see suits of medival armor in the East Hall of the Museum with more security guards going around the place."
                "\n You decides to head into the exhibition of 19th century artifacts and machinery. "
                "\n It is here where they spot a security guard.")
                print(" You see a see a statues that you could potentially hide behind. "
                      "\n You also had the urge to fight the security guard to avoid being alerted.")
                print("1. Disguse as one of the statues to manuver the security guard. ")
                print("2. Go face the enemy.")
                player_choice = int(input("What do you want to do? "))

                if player_choice ==1:
                    print("The player throws a rock at the guard who goes to investigate. "
                          "\nThe player hides behind one of the statues and isn't spotted. "
                          "\nOnce the coast is clear, you continue navigating the hallway."
                          "\nYou successfully stolen the Diamond of Power! You win!")

                else:
                    print("The enemy spots you after the player made the decision to fight the enemy to avoid getting your location being exposed. ")

                    battle_outcome = random.choice(["win", "flee","lose"])
                    if battle_outcome == "win":
                        print(
                            "\nYou deal enough damage to the enemy before it is able to deal too much damage. "
                            "\nTherefore, the enemy becomes unconcious and you continue moving on throughout the musuem in order to scout the Diamond of Power."
                            "\nYou navigate through the halls and eventually, you stole and escape with the Diamond of Power."
                            "\n You win! ")
                    elif battle_outcome == "win":
                        print(
                            "\nYou fled the battle and managed to avoid getting caught. ")
                        return

                    else:
                        print("\nThe enemy dealt a lot of damange and you were knocked unconcious."
                              "\nYou unfortunately end up in jail. Game Over! ")
                        return

            else:
                print("You say it is Java and the computer system says, 'Nope, that's the wrong answer."
                      "\n It launches you to the moon and you became famous for the wrong reasons."
                      "\n Game Over.")
                return
    else:
        print("After going through the vents, you end up falling into a pit that leads into a secret room. "
                "\nHere, you ended up being the subject of experiments which causes a game over. "
                "\n The game promptly tells you that you should have probably known that going through a suspicious vent would lead you to bad consequences. ")
        return




        print("\nYou tried to steal the object from a nearby building. However, you ended up getting busted. "
              "\nWhat's worse, you got a terrible mugshot. Game over.")
        return

adventure()
